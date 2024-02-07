FROM alpine

RUN apk update
RUN apk add nginx nginx-mod-http-headers-more

EXPOSE 80 443
RUN rm /etc/nginx/nginx.conf
COPY nginx.conf /etc/nginx/
CMD ["nginx" , "-g" , "daemon off;"]