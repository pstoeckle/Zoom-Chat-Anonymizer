FROM python:3.9-buster

RUN apt-get update && apt-get upgrade -y
RUN pip install --upgrade pip
RUN wget -q https://github.com/jgm/pandoc/releases/download/2.13/pandoc-2.13-1-amd64.deb
RUN dpkg -i *.deb
RUN rm *.deb
RUN useradd --create-home --shell /bin/bash pandoc_user

# Install python lib.
COPY dist dist
RUN pip install dist/*.whl

ENV HOME=/home/pandoc_user
USER pandoc_user
WORKDIR /home/pandoc_user
