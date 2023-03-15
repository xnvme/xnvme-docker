FROM debian:bullseye

WORKDIR /opt

COPY qemu qemu

RUN chmod +x qemu/bin/qemu-system-x86_64

RUN apt-get -qy update && \
	apt-get -qy \
		-o "Dpkg::Options::=--force-confdef" \
		-o "Dpkg::Options::=--force-confold" upgrade && \
	apt-get -qy autoclean && \
	apt-get -qy install aptitude

RUN aptitude -q -y -f install \
	libaio-dev \
	libglib2.0-0 \
	libglib2.0-dev \
	libguestfs-tools \
	liblzo2-dev \
	libpmem-dev \
	libvirt-dev \
	libvirt0

RUN aptitude -q -y -f install \
	libpixman-1-0 \
	libpixman-1-dev

RUN aptitude -q -y -f install \
	bridge-utils \
	cloud-image-utils \
	git \
	htop \
	lshw \
	openssh-server \
	procps \
	ssh \
	time \
	vim

RUN aptitude -q -y -f install \
	python3 \
	python3-pip

RUN ln -s /usr/bin/python3.8 /usr/bin/python

# Install cijoe and the packages example and qemu packages
RUN pip install cijoe cijoe-pkg-qemu || true
RUN pip3 install cijoe cijoe-pkg-qemu || true

# Setup SSH
RUN echo "PermitRootLogin yes" >> /etc/ssh/sshd_config
RUN systemctl enable ssh
RUN service ssh restart
RUN mkdir -p /root/.ssh
RUN chmod 0700 /root/.ssh
RUN ssh-keygen -b 2048 -t rsa -f /root/.ssh/id_rsa -q -N ""
RUN cp /root/.ssh/id_rsa.pub /root/.ssh/authorized_keys

# Don't want any of that hastle
RUN echo "Host *" >> /root/.ssh/config
RUN echo "  StrictHostKeyChecking no" >> /root/.ssh/config
RUN echo "  NoHostAuthenticationForLocalhost yes" >> /root/.ssh/config
RUN echo "  UserKnownHostsFile=/dev/null" >> /root/.ssh/config
RUN chmod 0400 /root/.ssh/config

# This does not apply when SSH-ing to localhost, then ENV set by this is cleared
ENV PATH="/opt/qemu/bin:$PATH"
# So we also add it to /root/.profile
RUN echo 'PATH="/opt/qemu/bin:$PATH"' > /root/.profile

# Check that the correct qemu is being called
RUN qemu-system-x86_64 --version

CMD ["bash"]
