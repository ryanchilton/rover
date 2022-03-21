FROM nvcr.io/nvidia/l4t-base:r32.6.1

RUN apt-get -y update
#RUN apt-get -y upgrade

RUN DEBIAN_FRONTEND=noninteractive TZ=America/New_York apt-get install -y python3-venv build-essential libhdf5-dev python3-dev vim python-rospy

RUN apt-get install python3-venv

COPY rover /rover

WORKDIR /rover

RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .
RUN pip3 install --upgrade pip
RUN pip install -r requirements.txt
 

