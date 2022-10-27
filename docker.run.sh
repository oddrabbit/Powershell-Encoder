#!/bin/bash

docker build -t powershell_encoder .
docker run -v /:/app/mnt powershell_encoder $@
