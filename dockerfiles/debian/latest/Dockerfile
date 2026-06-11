FROM ghcr.io/xnvme/xnvme-deps-debian-trixie:main

LABEL maintainer="os@safl.dk"
LABEL org.opencontainers.image.source="https://github.com/xnvme/xnvme-docker"

WORKDIR /root

# CI tooling: formatting, linting, docs and man-page generation
RUN apt-get -qy update && apt-get -qy install \
	clang-format \
	curl \
	doxygen \
	git \
	graphviz \
	make \
	pipx \
	pre-commit \
	shellcheck \
	txt2man \
	universal-ctags

# Debian packaging tooling
RUN apt-get -qy install \
	autotools-dev \
	build-essential \
	debhelper \
	devscripts \
	dh-make \
	dh-python \
	lintian \
	sudo

RUN pipx install kmdo poetry
ENV PATH="/root/.local/bin:${PATH}"

CMD ["bash"]
