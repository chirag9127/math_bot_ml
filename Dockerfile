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
# RUN easy_install pip

# Add and install Python modules
# ADD requirements.txt /src/requirements.txt
# RUN cd /src; pip install -r requirements.txt

RUN wget https://repo.continuum.io/miniconda/Miniconda3-4.2.12-Linux-x86_64.sh \
	&& chmod u+x Miniconda3-4.2.12-Linux-x86_64.sh \
	&& ./Miniconda3-4.2.12-Linux-x86_64.sh -b -p /usr/local/miniconda -f \
	&& rm Miniconda3-4.2.12-Linux-x86_64.sh
ENV PATH=/usr/local/miniconda/bin:$PATH

# RUN conda create --name math_bot_ml_36 python=3.6
# RUN ["/bin/bash", "-c", "source activate math_bot_ml_36"]
RUN conda install flask
RUN conda install keras
RUN conda install theano

# Bundle app source
ADD . /src

# Expose
EXPOSE  5000

# Run
CMD ["python", "/src/application.py"]
