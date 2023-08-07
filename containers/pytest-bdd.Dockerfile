FROM python:3.11.4 
RUN pip install pytest
RUN pip install pytest-bdd
RUN mkdir /var/code
WORKDIR /var/code
RUN apt-get install git -y
RUN git clone https://github.com/FeynmanFan/pytest-bdd
ENTRYPOINT ["tail", "-f", "/dev/null"]
