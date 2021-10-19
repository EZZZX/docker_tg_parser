FROM python:latest
WORKDIR /app
ADD requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD [ "python3", "tg_bot.py"]
