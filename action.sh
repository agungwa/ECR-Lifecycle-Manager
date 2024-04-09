#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 4 ]; then
    echo "Usage: $0 <param1 : $1> <param2: $2> <param3: $3> <param4: $4>"
    exit 1
fi

# Extract parameters
param1=$1
param2=$2
param3=$3
param4=$4

echo "content of directory"
ls

# Execute Python script with parameters
# python action.py "$param1" "$param2" "$param3" "$param4"