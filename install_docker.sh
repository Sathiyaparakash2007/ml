#!/bin/bash
set -e

if ! command -v docker &> /dev/null; then
  dnf install -y docker
fi

systemctl enable docker
systemctl start docker
mkdir -p /home/ec2-user/ml-app
