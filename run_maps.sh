#!/bin/bash

INPUT_DIR="/data/Twitter dataset"
OUTPUT_DIR="outputs"
MAX_PROCESSES=20

mkdir -p "$OUTPUT_DIR"
count=0

for file in "$INPUT_DIR"/*.zip; do
    python3 src/map.py --input_path="$file" --output_folder="$OUTPUT_DIR" &
    ((count++))

    # Wait for background processes if limit is reached
    if [[ $count -ge $MAX_PROCESSES ]]; then
        wait
        count=0
    fi
done

# Wait for any remaining background jobs
wait

echo "All map tasks completed."

