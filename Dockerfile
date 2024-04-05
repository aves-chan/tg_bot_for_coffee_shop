FROM ubuntu:latest
LABEL authors="vsevolodanisuk"

ENTRYPOINT ["top", "-b"]