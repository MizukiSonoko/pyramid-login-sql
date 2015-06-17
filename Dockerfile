FROM debian

MAINTAINER  mizuki <mizuki.sonoko@gmail.com>

RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get install -y build-essential
RUN apt-get install -y python-dev
RUN apt-get install -y wget

WORKDIR /tmp
RUN wget https://raw.github.com/pypa/pip/master/contrib/get-pip.py 
RUN python get-pip.py

RUN pip install PyMySQL3
RUN pip install SQLAlchemy
RUN pip install Pyramid
RUN pip install docutils

RUN mkdir pyramid_login
RUN mkdir pyramid_login/pyramidlogin
RUN mkdir pyramid_login/pyramidlogin/templates
RUN mkdir pyramid_login/pyramidlogin/scripts
RUN mkdir pyramid_login/pyramidlogin/static
RUN mkdir pyramid_login/pyramid_login.egg-info

ADD pyramid-login/*.ini /pyramid_login/
ADD pyramid-login/*.py  /pyramid_login/
ADD pyramid-login/*.txt  /pyramid_login/

ADD pyramid-login/pyramid_login.egg-info/* /pyramid_login/pyramid_login.egg-info/

COPY pyramid-login/pyramidlogin/*.py  /pyramid_login/pyramidlogin/
COPY pyramid-login/pyramidlogin/templates/*.mako  /pyramid_login/pyramidlogin/templates/
COPY pyramid-login/pyramidlogin/scripts/*.py  /pyramid_login/pyramidlogin/scripts/
COPY pyramid-login/pyramidlogin/static/*  /pyramid_login/pyramidlogin/static/

EXPOSE 6543

WORKDIR /pyramid_login
RUN python setup.py develop
RUN /usr/local/bin/initialize_pyramid-login_db development.ini


