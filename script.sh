#!/usr/bin/env bash

set -euo pipefail

output_file="output.txt"
root_directory="."
blacklist_file=""

while getopts "o:b:i:" flag; do
  case "${flag}" in
    o) output_file="${OPTARG}" ;;
    b) blacklist_file="${OPTARG}" ;;
    *) exit 1 ;;
  esac
done

shift $((OPTIND - 1))

if [ "$#" -gt 1 ]; then
  exit 1
elif [ "$#" -eq 1 ]; then
  root_directory="$1"
fi

prune_expressions=()

if [ -n "$blacklist_file" ]; then
  mapfile -t ignore_patterns < <(sed -e 's/^[[:space:]]\+//; s/[[:space:]]\+$//' -e '/^#/d' -e '/^$/d' -e 's@/*$@@' "$blacklist_file")

  for pattern in "${ignore_patterns[@]}"; do
    pattern=${pattern#/}
    prune_expressions+=( -path "${root_directory}/${pattern}" -prune -o )
  done
fi

: > "$output_file"

find_arguments=( "$root_directory" "${prune_expressions[@]}" -type f ! -path "${root_directory}/${output_file}" -print )

mapfile -t files < <(find "${find_arguments[@]}" | sort)

for filepath in "${files[@]}"; do
  filepath=${filepath//\\//}
  relative_path=${filepath#"${root_directory}/"}

  {
    echo "File: $relative_path"
    echo
    cat "$filepath"
    echo
  } >> "$output_file"
done

echo "Generated file: $output_file"