FROM node:19-alpine3.16

RUN mkdir /client

COPY ./client/package.json /client/

EXPOSE 3000

WORKDIR /client

COPY ./docker/local/client/start /start

RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

COPY ./client /client

RUN npm i -g pnpm;

ENV PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=true

CMD  pnpm install; pnpm dev
