FROM ubuntu:focal
LABEL maintainer "os@safl.dk"
RUN mkdir -p /root/xnvme
WORKDIR /root/xnvme
COPY xnvme .
RUN bash ./toolbox/pkgs/ubuntu-focal.sh
WORKDIR /root
RUN rm -rf /root/xnvme