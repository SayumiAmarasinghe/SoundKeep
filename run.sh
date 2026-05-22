#!/usr/bin/env bash
set -euo pipefail

# --- Configuration for SoundKeep ---
# Updated tdo match the "sound-keep" folder shown in your VS Code
APP_DIR="$HOME/sound-keep"
APP_FILE="fav-songs.py"
PY="$APP_DIR/.venv/bin/python"

cd "$APP_DIR"

# 1. Sync code with GitHub
echo "Syncing code..."
git fetch --all
git reset --hard origin/main

# 2. Ensure virtual environment exists
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python3.12 -m venv .venv
fi

# 3. Update dependencies
echo "Updating dependencies..."
"$PY" -m pip install -U pip
"$PY" -m pip install -r requirements.txt

# 4. Stop previous process
echo "Stopping old process..."
pkill -f "$PY $APP_FILE" || true

# 5. Start Flask server on port 3000
echo "Starting Flask server on port 3000..."
nohup "$PY" "$APP_FILE" > log.txt 2>&1 &

echo "Started successfully."
echo "Tail logs with: tail -n 200 -f $APP_DIR/log.txt"