FROM node:22-alpine AS build

WORKDIR /app

COPY frontend/package*.json ./
RUN npm ci

COPY frontend/ ./
COPY frontend-data/ /frontend-data/

RUN npm run build

FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html
# reverse-proxy /api/* to the backend container (see compose)
COPY frontend/nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
