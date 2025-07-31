#!/usr/bin/env bash

set -euo pipefail
trap 'echo; echo "Aborted"; exit 0' INT

readonly DEFAULT_BASE_DIRECTORY="."
readonly DEFAULT_REFRESH_INTERVAL=5

output_file_path=""
base_directory="$DEFAULT_BASE_DIRECTORY"
blacklist_file_path=""
is_watch_mode_enabled=false
is_header_displayed=false
refresh_interval="$DEFAULT_REFRESH_INTERVAL"
redirected_output_file=""

print_usage_message() {
  cat <<EOF
Usage: $(basename "$0") [OPTIONS] [DIRECTORY]

Concatenate all file contents from the given directory into a single output file

Options:
  -o, --output FILE        Output file path (if not provided, prints to stdout)
  -b, --blacklist FILE     Path to file with ignore patterns (one per line)
  -w, --watch              Enable watch mode to regenerate output on changes
  -i, --interval SEC       Polling interval in seconds when in watch mode (default: '$DEFAULT_REFRESH_INTERVAL')
  -h, --help               Show this help message
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    -o|--output) output_file_path="$2"; shift 2;;
    -b|--blacklist) blacklist_file_path="$2"; shift 2;;
    -w|--watch) is_watch_mode_enabled=true; shift;;
    -i|--interval) refresh_interval="$2"; shift 2;;
    -h|--help) print_usage_message; exit 0;;
    -*) echo "Unknown option: '$1'" >&2; print_usage_message; exit 1;;
    *) base_directory="$1"; shift;;
  esac
done

base_directory=$(realpath "$base_directory")
output_destination="/dev/stdout"

if [[ -n "$output_file_path" ]]; then
  output_destination=$(realpath "$output_file_path")
else
  stdout_target=$(readlink -f /proc/$$/fd/1 2>/dev/null || echo "")

  if [[ -n "$stdout_target" && -f "$stdout_target" ]]; then
    redirected_output_file="$stdout_target"
  fi
fi

if [[ -n "$blacklist_file_path" && ! -r "$blacklist_file_path" ]]; then
  echo "Error: Cannot read blacklist file '$blacklist_file_path'" >&2
  exit 1
fi

previous_scanned_hash=""

while true; do
  find_prune_arguments=()
  ignore_patterns=()

  if [[ -n "$blacklist_file_path" ]]; then
    mapfile -t ignore_patterns < <(sed -e 's/^[[:space:]]\+//' -e 's/[[:space:]]\+$//' -e '/^#/d' -e '/^$/d' -e 's@/*$@@' "$blacklist_file_path")

    for pattern in "${ignore_patterns[@]}"; do
      find_prune_arguments+=(-path "$base_directory/$pattern" -prune -o)
    done
  fi

  if [[ -n "$output_file_path" ]]; then
    > "$output_destination"
  fi

  find_arguments=("$base_directory" "${find_prune_arguments[@]}" -type f)

  if [[ -n "$output_file_path" ]]; then
    find_arguments+=(! -path "$output_destination")
  elif [[ -n "$redirected_output_file" ]]; then
    find_arguments+=(! -path "$redirected_output_file")
  fi

  mapfile -t files < <(find "${find_arguments[@]}" | sort)

  for absolute_file_path in "${files[@]}"; do
    absolute_file_path=${absolute_file_path//\\//}
    relative_file_path=${absolute_file_path#"${base_directory}/"}

    if [[ -f "$absolute_file_path" ]] && grep -Iq . "$absolute_file_path"; then
      {
        echo "File: '$relative_file_path'"
        echo
        sed -e '$a\' "$absolute_file_path"
        echo
      } >> "$output_destination"
    fi
  done

  if ! $is_watch_mode_enabled; then
    [[ -n "$output_file_path" ]] && echo "Generated file: '$output_file_path'"
    break
  fi

  if ! $is_header_displayed; then
    [[ -n "$output_file_path" ]] && echo "Generated file: '$output_file_path'"
    echo "Watching '$base_directory' using polling every ${refresh_interval}s... (Ctrl+C to stop)"

    is_header_displayed=true
  fi

  current_scanned_hash=""

  until [[ "$current_scanned_hash" != "$previous_scanned_hash" ]]; do
    sleep "$refresh_interval"
    current_scanned_hash=$(find "$base_directory" -type f -exec stat -c '%Y' {} + 2>/dev/null | sha256sum | awk '{print $1}')
  done

  previous_scanned_hash="$current_scanned_hash"
done
