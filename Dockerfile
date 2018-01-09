FROM alexchcodefresh/selenium-plugin:v1

RUN apt-get clean

ENTRYPOINT ["scripts/init.sh"]

