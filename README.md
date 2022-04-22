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
* run this to cross build: docker buildx build --platform linux/arm64 -t <name:version> -f Dockerfile .

# Visualization
* https://github.com/dheera/rosboard
