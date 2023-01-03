FROM  debian
#RUN /bin/bash -c 'source $HOME/.bashrc; '

RUN apt update
RUN apt upgrade -y
RUN apt install python3 -y
RUN apt install python3-pip -y
RUN apt install ipmitool -y
RUN apt install nano -y
RUN apt install cron -y

ENV TZ="America/New_York"

# Adding crontab to the appropriate location
#ADD cronjob /etc/cron.d/cronjob

# Giving permission to crontab file
#RUN chmod 0644 /etc/cron.d/cronjob

# Running crontab
#RUN crontab /etc/cron.d/cronjob

#RUN touch /var/log/cron.log
#CMD cron && tail -f /var/log/cron.log

WORKDIR /usr/app/src

COPY dellStartStop.py ./
#COPY  dellStartBackup.py ./
#COPY job.sh ./

#RUN chmod +x job.sh

#ENTRYPOINT [ "cron", "-f"]
#ENTRYPOINT [ "python3", "./dellStartBackup.py"]
ENTRYPOINT [ "/usr/bin/python3", "./dellStartStop.py"]