FROM nginx:1.19.2
COPY ./Docker/nginx/uwsgi_params /etc/nginx/uwsgi_params
RUN apt-get update
COPY ./Docker/nginx/conf /etc/nginx/conf.d
EXPOSE 80