FROM rkchil/jetson_nano_ros:3.0

RUN apt-get -y update
#RUN apt-get -y upgrade

RUN mkdir /code
WORKDIR /code
RUN git clone https://github.com/dusty-nv/jetson-utils
RUN mkdir jetson-utils/build
WORKDIR /code/jetson-utils/build
RUN cmake ..
RUN build



COPY rover /rover

WORKDIR /rover

RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .
RUN pip3 install --upgrade pip
RUN pip install -r requirements.txt
 

