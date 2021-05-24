FROM ghcr.io/bryantson/node:10

WORKDIR /app

COPY ["package.json","package-lock.json*","./"]

RUN npm install

COPY . .

CMD ["npm","start"]
