#!/bin/bash
set -e
cd /home/ec2-user/ml-app
docker build -t ml-app:latest .
