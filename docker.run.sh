#!/bin/bash

docker build -t powershell_encoder .
docker run powershell_encoder $@
