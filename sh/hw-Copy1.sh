#!/bin/bash

# Function to check for the presence of -d or --debug in the arguments
contains_debug_flag() {
    for arg in "$@"; do
        if [[ "$arg" == "-d" || "$arg" == "--debug" ]]; then
            return 0  # Found the debug flag
        fi
    done
    return 1  # Debug flag not found
}

# Extract script name without path or extension
# STEM=$(basename "$0" .sh)

# STEM='hw'
# STEM=$(basename "$(dirname "$0")" | cut -d'-' -f1)
# echo $STEM

SCRIPT_PATH="$(realpath "${BASH_SOURCE[0]}")"
SCRIPT_DIR="$(dirname "$SCRIPT_PATH")"
SCRIPT_DIR="$(dirname "$SCRIPT_DIR")"
DIR_NAME="$(basename "$SCRIPT_DIR")"
STEM="${DIR_NAME%%-*}"

PYTHON_SCRIPT="$STEM"

if [ -d "$STEM" ]; then
    if [ -f "$STEM/__init__.py" ]; then
        if [ -f "$STEM/__main__.py" ]; then
            # Run the directory as a module
            python3 -m "$STEM" "$@"
        elif [ -f "$STEM/__init__.py" ]; then
            # Attempt to import the module
            python3 -c "import $STEM"
        fi
    else
        # Run the script inside the directory
        if [ -f "$STEM/$STEM.py" ]; then
            python3 "$STEM/$STEM.py" "$@"
        else
            echo "No valid Python entry point found in $STEM"
            exit 1
        fi
    fi
else
    echo "Directory $STEM does not exist."
    exit 1
fi

