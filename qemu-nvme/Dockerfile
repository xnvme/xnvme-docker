FROM debian:trixie

WORKDIR /opt

COPY qemu qemu

RUN chmod +x qemu/bin/qemu-system-x86_64

RUN apt-get -qy update && \
	apt-get -qy \
		-o "Dpkg::Options::=--force-confdef" \
		-o "Dpkg::Options::=--force-confold" upgrade && \
	apt-get -qy autoclean

RUN apt-get -qy install \
	autoconf \
	bash-completion \
	bridge-utils \
	build-essential \
	cloud-image-utils \
	doxygen \
	git \
	graphviz \
	htop \
	libaio-dev \
	libarchive-dev \
	libcunit1-dev \
	libglib2.0-0t64 \
	libglib2.0-dev \
	libguestfs-tools \
	libisal-dev \
	liblzo2-dev \
	libncurses5-dev \
	libnuma-dev \
	libpixman-1-0 \
	libpixman-1-dev \
	libpmem-dev \
	libssl-dev \
	libtool \
	liburing-dev \
	libvirt-dev \
	libvirt0 \
	lshw \
	make \
	meson \
	nasm \
	openssh-server \
	openssl \
	patch \
	pipx \
	pkg-config \
	procps \
	python3 \
	python3-pip \
	python3-pyelftools \
	python3-venv \
	ssh \
	time \
	universal-ctags \
	uuid-dev \
	vim

RUN ln -s /usr/bin/python3 /usr/bin/python

# We want pipx to work...
RUN pipx ensurepath

# Install CIJOE
RUN pipx install cijoe==v0.9.58 --include-deps && \
	pipx inject cijoe matplotlib && \
	pipx inject cijoe numpy && \
	pipx install rst2pdf

# Setup SSH
RUN echo "PermitRootLogin yes" >> /etc/ssh/sshd_config && \
	mkdir -p /root/.ssh && \
	chmod 0700 /root/.ssh && \
	ssh-keygen -b 2048 -t rsa -f /root/.ssh/id_rsa -q -N "" && \
	cp /root/.ssh/id_rsa.pub /root/.ssh/authorized_keys

# Don't want any of that hassle
RUN echo -e "Host *\n  StrictHostKeyChecking no\n  NoHostAuthenticationForLocalhost yes\n  UserKnownHostsFile=/dev/null" > /root/.ssh/config && \
	chmod 0400 /root/.ssh/config

# This does not apply when SSH-ing to localhost, then ENV set by this is cleared
ENV PATH="/opt/qemu/bin:$PATH"
# So we also add it to /root/.profile
RUN echo 'PATH="/opt/qemu/bin:$PATH"' >> /root/.profile

# Check that the correct qemu is being called
RUN qemu-system-x86_64 --version

CMD ["bash"]
