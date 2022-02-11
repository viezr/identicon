#!/bin/bash
docker run --name identicon -e "ENV=DEV" -p 5000:5000 -v $(pwd)/app:/app identicon
