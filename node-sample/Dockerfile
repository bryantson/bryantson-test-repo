FROM ghcr.io/bryantson/nodejs:10

WORKDIR /src

COPY ["package.json","./"]

RUN install

CMD ["node","server.js"]
