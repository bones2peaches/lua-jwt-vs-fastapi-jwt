# Use the official OpenResty image as the base
FROM openresty/openresty:alpine
RUN apk add --no-cache curl \
    perl \
    nginx-mod-http-headers-more \ 
    apache2-utils

# Install lua-resty-jwt using opm
RUN opm get SkyLothar/lua-resty-jwt


COPY ./nginx.conf /usr/local/openresty/nginx/conf/nginx.conf


COPY ./scripts /usr/local/openresty/nginx/lua/
EXPOSE 80 


CMD ["/usr/local/openresty/bin/openresty", "-g", "daemon off;"]