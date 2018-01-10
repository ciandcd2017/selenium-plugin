FROM ubuntu:17.04 AS build

RUN mkdir Selenium
WORKDIR Selenium


RUN apt-get -y --force-yes update
RUN apt-get -y install wget
RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.17.0/geckodriver-v0.17.0-linux64.tar.gz
RUN mkdir bin
RUN tar xvzf geckodriver-v0.17.0-linux64.tar.gz -C bin
RUN apt-get install python-pip -y
RUN pip install -U Selenium


FROM ubuntu:17.04

RUN apt-get -y update
RUN apt-get -y install firefox
RUN apt-get -y install xvfb
RUN apt-get install -y python-minimal
COPY --from=build /Selenium/bin/ /Selenium/bin
COPY --from=build /usr/local/lib/python2.7/dist-packages /usr/local/lib/python2.7/dist-packages
WORKDIR Selenium

ENTRYPOINT ["scripts/init.sh"]

