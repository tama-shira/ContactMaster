FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /home/code
WORKDIR /home/code
ADD requirements.txt /home/code/
RUN pip install -r requirements.txt
ADD . /home/code/
