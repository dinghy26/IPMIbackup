FROM  ubuntu:latest
RUN /bin/bash -c 'source $HOME/.bashrc; '

RUN apt update
RUN apt upgrade -y
RUN apt install python3 -y
RUN apt install python3-pip -y
RUN apt install ipmitool -y
RUN pip install proxmoxmanager
RUN pip install pyYAML

WORKDIR /usr/app/src

COPY  dellStartBackup.py ./
COPY  dellSetUp.yaml ./

