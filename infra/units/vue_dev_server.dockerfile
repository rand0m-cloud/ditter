FROM node:18-alpine

ENV PORT=3000

WORKDIR /app
ENTRYPOINT npm i && npx vite --host 0.0.0.0 --port $PORT