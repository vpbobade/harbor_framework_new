#!/bin/bash

response=$(curl -s http://localhost:8000/health)

if [[ "$response" == *"ok"* ]]; then
  echo "PASS"
  exit 0
else
  echo "FAIL"
  exit 1
fi
