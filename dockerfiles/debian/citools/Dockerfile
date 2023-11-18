FROM ghcr.io/xnvme/xnvme-deps-debian-bullseye:next

LABEL maintainer "os@safl.dk"

WORKDIR /root

RUN apt-get -qy install \
	apt-utils \
	software-properties-common \
	sudo \
	wget

RUN wget -O - https://apt.llvm.org/llvm-snapshot.gpg.key | apt-key add -

RUN add-apt-repository "deb http://apt.llvm.org/bullseye/ llvm-toolchain-bullseye-14 main"

RUN apt-get -qy update

RUN apt-get -qy install clang-format-14

RUN update-alternatives --install /usr/bin/clang-format clang-format /usr/bin/clang-format-14 100

RUN apt-get -qy install \
    shellcheck \
    txt2man \
    clang-tools

RUN pip3 install pre-commit

RUN pip3 install breathe Jinja2 kmdo sphinx sphinx_rtd_theme sphinxcontrib-bibtex

RUN apt-get -qy install \
	doxygen \
	exuberant-ctags \
	graphviz

CMD ["bash"]