#!/bin/bash

docker run -it --rm --privileged --runtime nvidia --security-opt  seccomp=unconfined --network host  -v /tmp/.X11-unix/:/tmp/.X11-unix -v /tmp/argus_socket:/tmp/argus_socket -v /etc/enctune.conf:/etc/enctune.conf -e DISPLAY=$DISPLAY rkchil/rover:5.0 /bin/bash
