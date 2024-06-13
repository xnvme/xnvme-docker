FROM debian:bookworm
LABEL maintainer "os@safl.dk"
RUN mkdir -p /opt
COPY xnvme/toolbox /opt/toolbox
WORKDIR /opt
RUN bash -e ./toolbox/pkgs/debian-bookworm.sh

RUN apt-get -qyf install \
  autotools-dev \
  build-essential \
  debhelper \
  devscripts \
  dh-make \
  dh-python \
  gcc \
  git \
  libaio-dev \
  liburing-dev \
  lintian \
  meson \
  sudo \
  neovim \
  python3

WORKDIR /root
CMD ["bash"]