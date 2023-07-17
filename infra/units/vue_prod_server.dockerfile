FROM node:18-alpine as builder

WORKDIR /app
ADD ./ditterapp /app
RUN npm i && npm run build-only

FROM nginx:1.25

COPY --from=builder /app/dist /content