FROM ubuntu:17.04

RUN mkdir Selenium
WORKDIR Selenium


RUN apt-get -y --force-yes update
RUN apt-get -y --force-yes install firefox
RUN apt-get -y --force-yes install xvfb xfonts-100dpi xfonts-75dpi xfonts-cyrillic xorg dbus-x11
RUN apt-get -y install wget
RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.17.0/geckodriver-v0.17.0-linux64.tar.gz
RUN mkdir bin
RUN tar xvzf geckodriver-v0.17.0-linux64.tar.gz -C bin
RUN apt-get install python-pip -y
RUN pip install -U Selenium
RUN apt-get clean

ENTRYPOINT ["scripts/init.sh"]

