#!/bin/bash
docker run --name identicon -P -v $(pwd)/app:/app identicon
