FROM node:16-alpine as build

WORKDIR /app
COPY ./ui /app
RUN npm install
RUN npm run build

FROM nginx:stable-alpine

COPY ./ui/docker/default.conf.template /etc/nginx/templates/default.conf.template
COPY --from=build /app/dist/ /usr/share/nginx/html/

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
