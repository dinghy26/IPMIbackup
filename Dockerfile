FROM  ubuntu:latest
RUN /bin/bash -c 'source $HOME/.bashrc; '

RUN apt update
RUN apt upgrade -y
RUN apt install python3 -y
RUN apt install python3-pip -y
RUN apt install ipmitool -y
RUN apt install nano -y
RUN pip install pyYAML
RUN apt install cron -y

ENV TZ="America/New_York"


# Add the cron job
RUN crontab -l | { cat; echo "0 21 * * * bash /usr/app/src/dellStartBackup.py"; } | crontab -
RUN crontab -l | { cat; echo "0 2 * * * bash /usr/app/src/dellStartBackup.py"; } | crontab -

WORKDIR /usr/app/src

COPY  dellStartBackup.py ./
COPY  dellSetUp.yaml ./

# run cron
CMD cron


