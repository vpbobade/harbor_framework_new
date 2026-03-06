#!/bin/bash

docker compose -f environment/docker-compose.yml up -d --build

sleep 10

curl -f http://localhost:8000/health
