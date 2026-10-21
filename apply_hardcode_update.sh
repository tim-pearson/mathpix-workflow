#!/usr/bin/env bash
set -Eeuo pipefail

cd "$(dirname "$0")"

BOOK="Maths Pure 2 & 3-clean_no_badges_covered_margins-p1-p352pages"

log() {
    printf '\n[%s] %s\n' "$(date '+%H:%M:%S')" "$*"
}

run() {
    log "RUN: $*"
    "$@"
    log "DONE: $*"
}

trap 'rc=$?; log "ERROR: command failed (exit $rc) at line $LINENO"; exit "$rc"' ERR

log "Starting frontend update"
log "Repository: $PWD"
log "Book: $BOOK"

log "Step 1/4: Normalise sections and regenerate split/index.json"
run python -u ./scripts/fix_sections.py

log "Step 2/4: Export frontend data"
run python -u ./scripts/export_data.py "$BOOK" --out frontend-data

log "Step 3/4: Sync data into frontend"
run bash -c 'cd frontend && npm run sync-data'

log "Step 4/4: Start frontend development server"
cd frontend
log "Starting npm run dev (press Ctrl+C to stop)"
exec npm run dev
