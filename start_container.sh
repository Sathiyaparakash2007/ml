#!/bin/bash
set -e
docker run -d --name ml-app --restart always -p 80:5000 ml-app:latest
