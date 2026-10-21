#!/usr/bin/env bash
set -Eeuo pipefail

cd "$(dirname "$0")"

BOOK="Maths Pure 2 & 3-clean_no_badges_covered_margins-p1-p352pages"
DB_DIR="$PWD/backend/data"
DB_PATH="$DB_DIR/progress.db"
BACKEND_LOG="$PWD/backend/backend.log"
BACKEND_PID=""

log() {
    printf '\n[%s] %s\n' "$(date '+%H:%M:%S')" "$*"
}

run() {
    log "RUN: $*"
    "$@"
    log "DONE: $*"
}

cleanup() {
    if [[ -n "$BACKEND_PID" ]] && kill -0 "$BACKEND_PID" 2>/dev/null; then
        log "Stopping backend (PID $BACKEND_PID)"
        kill "$BACKEND_PID" 2>/dev/null || true
        wait "$BACKEND_PID" 2>/dev/null || true
    fi
}

trap 'rc=$?; log "ERROR: command failed (exit $rc) at line $LINENO"; exit "$rc"' ERR
trap cleanup EXIT
trap 'exit 130' INT
trap 'exit 143' TERM

log "Starting frontend update"
log "Repository: $PWD"
log "Book: $BOOK"

log "Step 1/5: Normalise sections and regenerate split/index.json"
run python -u ./scripts/fix_sections.py

log "Step 2/5: Export frontend data"
run python -u ./scripts/export_data.py "$BOOK" --out frontend-data

log "Step 3/5: Sync data into frontend"
run bash -c 'cd frontend && npm run sync-data'

log "Step 4/5: Prepare database and start backend"

mkdir -p "$DB_DIR"

# Keep the database in backend/data so it persists between runs.
export PROGRESS_DB="$DB_PATH"

if ! curl -fsS http://127.0.0.1:8000/openapi.json >/dev/null 2>&1; then
    log "Starting FastAPI backend on 127.0.0.1:8000"
    python -m uvicorn main:app \
        --app-dir backend \
        --host 127.0.0.1 \
        --port 8000 \
        >"$BACKEND_LOG" 2>&1 &
    BACKEND_PID=$!

    # Wait for the API to become ready, failing if it exits or times out.
    for _ in {1..30}; do
        if curl -fsS http://127.0.0.1:8000/openapi.json >/dev/null 2>&1; then
            break
        fi

        if ! kill -0 "$BACKEND_PID" 2>/dev/null; then
            log "Backend exited during startup. Last log lines:"
            tail -n 40 "$BACKEND_LOG"
            exit 1
        fi

        sleep 1
    done

    if ! curl -fsS http://127.0.0.1:8000/openapi.json >/dev/null 2>&1; then
        log "Backend did not become ready. Last log lines:"
        tail -n 40 "$BACKEND_LOG"
        exit 1
    fi

    log "Backend ready; log: $BACKEND_LOG"
else
    log "Backend already responds on port 8000; reusing it"
fi

log "Step 5/5: Start frontend development server"
cd frontend
log "Starting npm run dev (press Ctrl+C to stop)"
npm run dev
