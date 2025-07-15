#!/bin/bash
set -e

bash install.sh
docker run -p 8000:8000 fastapi-feedback
