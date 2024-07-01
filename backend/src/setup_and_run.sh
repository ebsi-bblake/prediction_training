#!/bin/bash
echo "setup_and_run.sh script started successfully"
# Exit immediately if a command exits with a non-zero status
set -e

# Run data collection
python src/data_collection.py

# Run data preprocessing
python src/data_preprocessing.py

# Run model training
python src/model_training.py

# Start the gRPC server
python grpc/server.py

echo "setup_and_run.sh script executed successfully"