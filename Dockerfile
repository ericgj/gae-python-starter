FROM python:3
RUN [ "./bin/init-virtualenv" ]
RUN [ "./bin/install", "./requirements.txt", "initial" ]
