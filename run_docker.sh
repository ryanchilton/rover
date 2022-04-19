#!/bin/bash

docker run -it --rm --device /dev/i2c-1 --privileged --name rover rover:1.0 /bin/bash
