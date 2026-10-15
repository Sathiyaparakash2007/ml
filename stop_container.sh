#!/bin/bash
docker stop ml-app 2>/dev/null || true
docker rm ml-app 2>/dev/null || true
