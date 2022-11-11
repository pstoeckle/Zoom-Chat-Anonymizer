FROM python:3.9-buster

ARG COMMIT=""
ARG TAG=""

LABEL author="Patrick Stöckle <patrick.stoeckle@posteo.de>"
LABEL edu.tum.i4.mod-python-scripts.commit=${COMMIT}
LABEL edu.tum.i4.mod-python-scripts.tag=${TAG}

ENV COMMIT=${COMMIT}
ENV TAG=${TAG}

ENV PATH="${PATH}:/home/pandoc_user/.local/bin"

WORKDIR /

RUN apt-get update -qq \
    && apt-get upgrade -y \
    && apt-get autoremove -y -qq \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --no-cache-dir --upgrade pip==21.3.1 \
    && wget -q https://github.com/jgm/pandoc/releases/download/2.13/pandoc-2.13-1-amd64.deb \
    && dpkg -i ./*.deb \
    && rm ./*.deb \
    && useradd --create-home --shell /bin/bash pandoc_user

WORKDIR /home/pandoc_user
USER pandoc_user

COPY --chown=pandoc_user dist dist

RUN pip install --no-cache-dir  dist/*.whl \
    && rm -rf dist \
    && zoom-chat-anonymizer --version
