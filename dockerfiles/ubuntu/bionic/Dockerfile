FROM ubuntu:bionic
LABEL maintainer "os@safl.dk"
RUN mkdir -p /root/xnvme
WORKDIR /root/xnvme
COPY xnvme .
RUN ./toolbox/pkgs/ubuntu-bionic.sh
WORKDIR /root
CMD ["bash"]