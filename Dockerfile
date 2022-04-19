FROM rkchil/jetson_nano_ros:1.0

RUN apt-get -y update
#RUN apt-get -y upgrade

COPY rover /rover

WORKDIR /rover

RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .
RUN pip3 install --upgrade pip
RUN pip install -r requirements.txt
 

