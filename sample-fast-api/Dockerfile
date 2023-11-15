FROM xxx/docker-virtual/python:3.12-alpine AS base-image

ENV PORT=443

RUN apk update && \
    apk upgrade && \
    apk add --no-cache \
    openssl \
    bash \

WORKDIR /app

RUN mkdir -p keystore

RUN openssl req \
    -x509 \
    -newkey rsa:2048 \
    -keyout keystore/key.pem \
    -out keystore/cert.pem \
    -days 365 \
    -nodes \
    -subj "/C=US/ST=ShortHills/L=New Jersey/O=Kuppa/OU=Home/CN=$HOSTNME.local"

FROM base-image AS deps-image

# Copy keystore from the base layer
COPY --from=base-image /app/keystore /app/keystore

ENV PIP_INDEX_URL="https://xxxxxx/artifactory/api/pypi/pypi-virtual/simple"

WORKDIR /app

COPY Pipfile Pipfile.lock ./

ENV PIPENV_VENV_IN_PROJECT=1
RUN pip install --upgrade pip pipenv==2023.10.3

RUN pipenv install --deploy --extra-pip-args="--no-cache-dire"

COPY ./src /app/src

RUN pipenv run test

FROM base-image AS runner-image

COPY --from=deps-image /app /app
ENV PATH="/app/.venv/bin:$PATH"

COPY start.sh /app/start.sh
RUN chmod +x /app/start.sh

EXPOSE $PORT

ENTRYPOINT ["/app/start.sh"]