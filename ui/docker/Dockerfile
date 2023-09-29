FROM nginx:stable-alpine

COPY ./docker/default.conf.template /etc/nginx/templates/default.conf.template
COPY ./dist/ /usr/share/nginx/html/

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
