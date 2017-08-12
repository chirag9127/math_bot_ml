FROM ubuntu:16.04

RUN apt-get update && \
		apt-get install -y \
			groovy \
			python \
		python-pip \
		make \
		git \
		ssh \
		bzip2

# Install Python Setuptools
RUN apt-get install -y python-setuptools

# Install pip
RUN easy_install pip

# Add and install Python modules
ADD requirements.txt /src/requirements.txt
RUN cd /src; pip install -r requirements.txt

# Bundle app source
ADD . /src

# Expose
EXPOSE  5000

# Run
CMD ["python", "/src/application.py"]
