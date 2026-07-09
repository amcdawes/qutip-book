#!/usr/bin/env bash
set -euo pipefail

SOURCE_DIR="${1:-$HOME/notebooks/QMlabs}"
SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"
BOOK_DIR="$(cd -- "${SCRIPT_DIR}/.." >/dev/null 2>&1 && pwd)"
DEST_DIR="${BOOK_DIR}/features"
RUN_LOG="${BOOK_DIR}/SYNC_FROM_QMLABS_LAST_RUN.md"

if ! command -v uv >/dev/null 2>&1; then
  echo "ERROR: uv is required but was not found on PATH." >&2
  exit 1
fi

if [[ ! -d "${SOURCE_DIR}" ]]; then
  echo "ERROR: source directory not found: ${SOURCE_DIR}" >&2
  exit 1
fi

if [[ ! -d "${DEST_DIR}" ]]; then
  echo "ERROR: destination directory not found: ${DEST_DIR}" >&2
  exit 1
fi

map_name() {
  local stem="$1"
  local normalized

  # Keep a stable naming convention aligned to existing book paths.
  normalized="${stem//&/and}"
  normalized="${normalized//[^A-Za-z0-9()]/_}"
  normalized="${normalized//__/_}"
  while [[ "${normalized}" == *"__"* ]]; do
    normalized="${normalized//__/_}"
  done
  normalized="${normalized#_}"
  normalized="${normalized%_}"

  echo "${normalized}.md"
}

upstream_sha=""
if git -C "${SOURCE_DIR}" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  upstream_sha="$(git -C "${SOURCE_DIR}" rev-parse --short=12 HEAD)"
fi

converted=()
skipped_duplicates=()

declare -A seen_targets=()

shopt -s nullglob
for src in "${SOURCE_DIR}"/*.ipynb; do
  base="$(basename "${src}" .ipynb)"
  target_file="$(map_name "${base}")"
  target_path="${DEST_DIR}/${target_file}"

  if [[ -n "${seen_targets[${target_file}]:-}" ]]; then
    skipped_duplicates+=("${base}.ipynb -> ${target_file} (duplicate target of ${seen_targets[${target_file}]})")
    continue
  fi
  seen_targets["${target_file}"]="${base}.ipynb"

  echo "Converting: ${base}.ipynb -> ${target_file}"
  uv run --with jupytext jupytext --to myst "${src}" -o "${target_path}" >/dev/null
  converted+=("${base}.ipynb -> ${target_file}")
done

{
  echo "# QMlabs Sync Report"
  echo
  echo "- Date (UTC): $(date -u +"%Y-%m-%dT%H:%M:%SZ")"
  echo "- Source directory: ${SOURCE_DIR}"
  if [[ -n "${upstream_sha}" ]]; then
    echo "- Upstream commit: ${upstream_sha}"
  else
    echo "- Upstream commit: not a git working tree"
  fi
  echo "- Converted notebooks: ${#converted[@]}"
  echo "- Skipped duplicate targets: ${#skipped_duplicates[@]}"
  echo
  if [[ ${#converted[@]} -gt 0 ]]; then
    echo "## Converted"
    for line in "${converted[@]}"; do
      echo "- ${line}"
    done
    echo
  fi
  if [[ ${#skipped_duplicates[@]} -gt 0 ]]; then
    echo "## Skipped Duplicates"
    for line in "${skipped_duplicates[@]}"; do
      echo "- ${line}"
    done
    echo
  fi
} >"${RUN_LOG}"

echo
echo "Sync complete."
echo "Converted: ${#converted[@]}"
echo "Skipped duplicates: ${#skipped_duplicates[@]}"
echo "Report: ${RUN_LOG}"
