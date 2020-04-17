FROM  python:3.7-alpine

ADD src /app/
COPY Pipfile /app/
WORKDIR /app
ENV PIPENV_PIPFILE=/app/Pipfile

RUN pip3 install pipenv && \
    pipenv install --dev && \
    pipenv lock -r > requirements.txt && \
    apk --update add curl && \
    rm -rf /var/lib/apt/lists/* && \
    rm /var/cache/apk/*

CMD [ "pipenv","run","python3","-u","/app/traffic_g.py" ]