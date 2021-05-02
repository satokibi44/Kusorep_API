FROM nginx:1.19.2
COPY ./Kusorep_API/nginx/uwsgi_params /etc/nginx/uwsgi_params
RUN apt-get update
COPY ./Kusorep_API/nginx/conf /etc/nginx/conf.d
EXPOSE 80