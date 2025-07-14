#!/usr/bin/env bash

set -euo pipefail

output_file="output.txt"
root_directory="."
blacklist_file=""
watch_mode=false
watch_command=""
refresh_interval=1
watch_shown=false

function print_usage_message() {
  cat <<EOF
Usage: $(basename "$0") [OPTIONS] [DIRECTORY]

Concatenate all file contents from the given directory into a single output file.

Options:
  -o, --output FILE        Output file path (default: output.txt)
  -b, --blacklist FILE     Path to file with ignore patterns (one per line)
  -w, --watch              Enable watch mode to regenerate output on changes
  -h, --help               Show this help message
EOF
  exit 0
}

function print_watch_dependency_error() {
  cat <<EOF
-w|--watch mode requires either 'inotifywait' (Linux) or 'fswatch' (macOS).

To install:
  Debian/Ubuntu/WSL        → sudo apt install inotify-tools
  macOS                    → brew install fswatch
EOF
  exit 1
}

function watch_with_polling() {
  local last_hash=""

  if ! $watch_shown; then
    echo "Generated file: $output_file"
    echo "Watching '$root_directory' using polling every ${refresh_interval}s... (Ctrl+C to stop)"
    watch_shown=true
  fi

  while true; do
    current_hash=$(find "$root_directory" -type f -exec stat -c '%Y' {} + 2>/dev/null | sha256sum | awk '{print $1}')

    if [[ "$current_hash" != "$last_hash" ]]; then
      last_hash="$current_hash"
      break
    fi

    sleep "$refresh_interval"
  done
}

function watch_with_inotifywait() {
  if ! $watch_shown; then
    echo "Generated file: $output_file"
    echo "Watching '$root_directory' using inotifywait... (Ctrl+C to stop)"
    watch_shown=true
  fi

  inotifywait -r -e modify,create,delete,move "$root_directory" > /dev/null 2>&1
}

function watch_with_fswatch() {
  if ! $watch_shown; then
    echo "Generated file: $output_file"
    echo "Watching '$root_directory' using fswatch... (Ctrl+C to stop)"
    watch_shown=true
  fi

  fswatch -r -o "$root_directory" | head -n 1 > /dev/null
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    -o|--output) output_file="$2"; shift; shift ;;
    -b|--blacklist) blacklist_file="$2"; shift; shift ;;
    -w|--watch) watch_mode=true; shift ;;
    -h|--help) print_usage_message ;;
    -*) echo "Unknown option: $1"; exit 1 ;;
    *) root_directory="$1"; shift ;;
  esac
done

output_file=$(realpath "$output_file")
root_directory=$(realpath "$root_directory")

if $watch_mode; then
  if [[ "$root_directory" == /mnt/* ]]; then
    watch_command="polling"
  elif command -v inotifywait &>/dev/null; then
    watch_command="inotifywait"
  elif command -v fswatch &>/dev/null; then
    watch_command="fswatch"
  else
    watch_command="polling"
  fi
fi

while true; do
  prune_expressions=()

  if [[ -n "$blacklist_file" ]]; then
    mapfile -t ignore_patterns < <(sed -e 's/^[[:space:]]\+//' -e 's/[[:space:]]\+$//' -e '/^#/d' -e '/^$/d' -e 's@/*$@@' "$blacklist_file")

    for pattern in "${ignore_patterns[@]}"; do
      pattern_abs=$(realpath -m "${root_directory}/${pattern#/}")
      prune_expressions+=( -path "$pattern_abs" -prune -o )
    done
  fi

  : > "$output_file"

  find_arguments=( "$root_directory" "${prune_expressions[@]}" -type f ! -path "$output_file" -print )
  mapfile -t files < <(find "${find_arguments[@]}" | sort)

  for filepath in "${files[@]}"; do
    filepath=${filepath//\\//}
    relative_path=${filepath#"${root_directory}/"}

    if [[ -f "$filepath" ]]; then
      {
        echo "File: $relative_path"
        echo
        cat "$filepath"
        echo
      } >> "$output_file"
    fi
  done


  if ! $watch_mode; then
    echo "Generated file: $output_file"
    break
  fi

  case "$watch_command" in
    inotifywait) watch_with_inotifywait ;;
    fswatch) watch_with_fswatch ;;
    polling) watch_with_polling ;;
    *) echo "Unknown watch command: $watch_command"; exit 1 ;;
  esac
done
