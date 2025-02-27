ARG PYTHON_VERSION=3.8
FROM python:${PYTHON_VERSION}
ARG FMC_ANSIBLE_VERSION=v1.0.2
ARG FMC_ANSIBLE_FOLDER=fmc-ansible

RUN apt-get update && \
    apt-get install -yq sshpass && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN wget https://github.com/CiscoDevNet/FMCAnsible/archive/${FMC_ANSIBLE_VERSION}.tar.gz && \
    tar -xvf ${FMC_ANSIBLE_VERSION}.tar.gz

RUN mkdir /${FMC_ANSIBLE_FOLDER}/ && \
    export FMC_SOURCE_FOLDER=`find ./ -maxdepth 1 -type d -name '*FMCAnsible-*'` && \
    mv $FMC_SOURCE_FOLDER/requirements.txt /${FMC_ANSIBLE_FOLDER} && \
    mv $FMC_SOURCE_FOLDER/ansible.cfg  /${FMC_ANSIBLE_FOLDER}

RUN pip install --no-cache-dir -r /${FMC_ANSIBLE_FOLDER}/requirements.txt

ENV PYTHONPATH="$PYTHONPATH:/${FMC_ANSIBLE_FOLDER}/"
WORKDIR /${FMC_ANSIBLE_FOLDER}
ENTRYPOINT ["ansible-playbook"]
