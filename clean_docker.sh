#!/bin/bash

# Fetch all Docker image IDs
image_ids=$(docker images -q)

# Check if there are any images
if [ -z "$image_ids" ]; then
  echo "No Docker images found."
  exit 0
fi

# Loop through each image ID and remove it
for image_id in $image_ids; do
  echo "Removing Docker image ID: $image_id"
  docker rmi -f $image_id
done

echo "All Docker images have been removed."
