FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /home/code
WORKDIR /home/code
ADD requirements.txt /home/code/
RUN pip install -r requirements.txt --proxy=http://apcy1px000.apc.nis-net.jp:8088
ADD . /home/code/