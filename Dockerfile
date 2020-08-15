
FROM python:3.7-buster

COPY hikepo.py /opt/local/hikepo

RUN python3 -m pip install -U "discord.py"

CMD ["/usr/local/bin/python", "/opt/local/hikepo"]
