FROM rkchil/jetson_nano_ros:5.0

RUN apt-get -y update

# needed for jetson-utils/display
RUN apt-get install -y libglew-dev

# install jetson-utils
RUN mkdir /code
WORKDIR /code
RUN git clone https://github.com/dusty-nv/jetson-utils
RUN mkdir jetson-utils/build
WORKDIR /code/jetson-utils/build
RUN cmake .. -DENABLE_NVMM=False
RUN make install

# install python dependenies
COPY rover /rover

WORKDIR /rover

RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .
RUN pip3 install --upgrade pip
RUN pip install -r requirements.txt
 

