# Rover
nvidia Jetson + camera + omni-directional platform

# Project Resources
* [Using I2C on the Jetson Nano](https://www.jetsonhacks.com/2019/07/22/jetson-nano-using-i2c/)
* [Battery Power Options](https://www.jetsonhacks.com/2021/07/16/nvidia-jetsons-on-battery-power/)
* [DC Motor Driver](https://www.adafruit.com/product/3243)

# Cross building
* enable buildx in docker by enabling experimental mode
* install qemu for arm64
* run this to register qemu interpreters: "docker run --rm --privileged multiarch/qemu-user-static --reset -p yes"
* run this to cross build: docker buildx build --platform linux/arm64 -t <name:version> -f Dockerfile r
* If compiling CUDA code, make sure to enable access to the CUDA compiler (nvcc) when running docker build: https://github.com/dusty-nv/jetson-containers#docker-default-runtime
* Ran into this error and solution: https://forums.developer.nvidia.com/t/docker-isnt-working-after-apt-upgrade/195213/6

# Remote camera stream
* gst-launch-1.0 -v udpsrc port=1234  caps = "application/x-rtp, media=(string)video, clock-rate=(int)90000, encoding-name=(string)H264, payload=(int)96" !  rtph264depay ! decodebin ! videoconvert ! autovideosink 

# Testing
## On robot
```
./run_docker.sh
jupyter notebook --allow-root
```

## On remote computer
```
ssh -N -f -L localhost:8888:localhost:8888 rover@192.168.4.97
```
then open localhost:8888 in browser