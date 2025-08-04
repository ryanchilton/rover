FROM dustynv/ros:humble-ros-core-l4t-r32.7.1

RUN curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
# RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys F42ED6FBAB17C654

RUN apt-get -y update

# needed for jetson-utils/display
#RUN apt-get install -y libglew-dev

# install python dependenies
COPY rover /rover

WORKDIR /rover

# Note: Don't use python venv because ros2 is installed in the system python
COPY requirements.txt .
RUN pip3 install --upgrade pip
RUN pip install -r requirements.txt
 

