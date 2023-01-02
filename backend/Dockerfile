FROM python:alpine3.17
WORKDIR /home/emily/music-backend
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000