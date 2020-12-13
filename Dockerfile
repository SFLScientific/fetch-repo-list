FROM python:3.8.6-slim

RUN pip install PyGithub==1.54 --no-cache

COPY . /src

ENTRYPOINT ["/src/entrypoint.sh"]
