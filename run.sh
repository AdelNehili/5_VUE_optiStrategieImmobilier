#!/bin/bash

# Define variables for the processes
PYTHON_SCRIPT="app.py"

# Step 1: Kill any running Python script
echo "Stopping any running Python script..."
pkill -f $PYTHON_SCRIPT

# Step 2: Start the Python script in the background
echo "Starting the Python script..."
python3 $PYTHON_SCRIPT &

# Step 3: Navigate to the Vue.js project directory
cd ./my-portfolio

# Step 4: Start the Vue.js development server
echo "Starting the Vue.js development server..."
npm run serve

