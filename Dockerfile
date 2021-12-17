FROM python:3.9-buster


ARG COMMIT=""
ARG COMMIT_SHORT=""
ARG BRANCH=""
ARG TAG=""

LABEL author="Patrick Stöckle <patrick.stoeckle@tum.de>"
LABEL edu.tum.i4.mod-python-scripts.commit=${COMMIT}
LABEL edu.tum.i4.mod-python-scripts.commit-short=${COMMIT_SHORT}
LABEL edu.tum.i4.mod-python-scripts.branch=${BRANCH}
LABEL edu.tum.i4.mod-python-scripts.tag=${TAG}

ENV COMMIT=${COMMIT}
ENV COMMIT_SHORT=${COMMIT_SHORT}
ENV BRANCH=${BRANCH}
ENV TAG=${TAG}

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

COPY dist dist

RUN chown pandoc_user dist

USER pandoc_user

RUN pip install --no-cache-dir  dist/*.whl \
    && rm -rf dist

ENV PATH="${PATH}:/home/pandoc_user/.local/bin"

RUN zoom-chat-anonymizer --version

