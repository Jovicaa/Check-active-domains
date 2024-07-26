#!/bin/sh

# Install nmap & python
apk update
apk add --no-cache python3
apk add nmap
apk add nmap-scripts
