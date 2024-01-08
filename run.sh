#!/bin/bash

while [ -f "state.running" ] || [ ! -f "state" ]; do
    python3 main.py
    rm core.python3.*
    sleep 1
done

echo "Script completed."
