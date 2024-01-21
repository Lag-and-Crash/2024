FROM php:7.4-apache

RUN apt-get update && apt-get install -y dnsutils

COPY ./index.php /var/www/html/

RUN sed -i 's/80/8080/g' /etc/apache2/sites-available/000-default.conf /etc/apache2/ports.conf
RUN echo "PidFile /dev/shm/apache2.pid" >> /etc/apache2/ports.conf

COPY ./flag.txt /flag.txt

CMD ["apache2-foreground"]