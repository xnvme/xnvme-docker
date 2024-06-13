FROM ghcr.io/xnvme/xnvme-deps-fedora-40:next

LABEL maintainer "os@safl.dk"

WORKDIR /root

RUN dnf -y install --allowerasing \
	clang-tools-extra \
	ctags \
	curl \
	git \
	make \
	pre-commit \
    shellcheck \
    txt2man \
	pipx \
	pre-commit \
	doxygen \
	graphviz

RUN pipx install kmdo poetry

CMD ["bash"]