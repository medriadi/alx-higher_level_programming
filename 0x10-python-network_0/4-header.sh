#!/bin/bash

# Check if URL argument is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# URL provided as argument
url=$1

# Send GET request with curl, including custom header
response=$(curl -X GET -H "X-School-User-Id: 98" "$url")

# Display response body
echo "$response"
