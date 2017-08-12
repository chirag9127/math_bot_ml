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

RUN wget https://repo.continuum.io/miniconda/Miniconda3-4.2.12-Linux-x86_64.sh \
	&& chmod u+x Miniconda3-4.2.12-Linux-x86_64.sh \
	&& ./Miniconda3-4.2.12-Linux-x86_64.sh -b -p /usr/local/miniconda -f \
	&& rm Miniconda3-4.2.12-Linux-x86_64.sh

ENV PATH=/usr/local/miniconda/bin:$PATH
ADD . /src

RUN [ "conda", "env", "create", "-f", "src/environment.yml" ]

# Expose
EXPOSE  5000

ENTRYPOINT [ "/bin/bash", "-c" ]
CMD [ "source activate math_bot_ml_36 && exec python src/application.py" ]
