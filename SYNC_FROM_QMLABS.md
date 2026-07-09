# Sync from QMlabs

This runbook defines the reproducible workflow for importing notebook content from the upstream QMlabs repository into this book.

## Goal

- Keep QMlabs notebooks as upstream computational source.
- Import those notebooks into `features/*.md` as a baseline.
- Allow book markdown to diverge afterward for standalone authoring.

## Upstream source

Default source path expected by the sync script:

- `$HOME/notebooks/QMlabs`

You can pass a different path as the first argument.

## One-command sync

From this folder (`qutip-book/`):

```bash
bash scripts/sync_from_qmlabs.sh
```

Or with explicit source path:

```bash
bash scripts/sync_from_qmlabs.sh /path/to/QMlabs
```

## What the script does

1. Finds top-level `*.ipynb` notebooks in QMlabs.
2. Converts each notebook to MyST markdown with `jupytext` via `uv`.
3. Writes outputs into `features/` with stable normalized filenames.
4. Skips duplicate target names deterministically (first source wins).
5. Writes a sync report to `SYNC_FROM_QMLABS_LAST_RUN.md` including:
   - UTC timestamp
   - source path
   - upstream git commit (if available)
   - converted list
   - duplicate-skip list

## Validate after sync

Run a non-executing build first:

```bash
uv run jupyter book build --pdf
```

If you want notebook outputs generated during build:

```bash
uv run jupyter book build --execute --pdf
```

Note: outputs are injected at build time by execution and cached in `_build/execute`; they are not stored directly in the MyST source text.

## Suggested commit policy

1. Commit the sync as its own commit (easy to review).
2. Then do content-editing commits separately.
3. Keep `SYNC_FROM_QMLABS_LAST_RUN.md` in the sync commit as provenance.
