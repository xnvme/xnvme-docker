FROM tgagor/centos:stream9
LABEL maintainer "os@safl.dk"
RUN mkdir -p /root/xnvme
WORKDIR /root/xnvme
COPY xnvme .
RUN bash ./toolbox/pkgs/centos-stream9.sh
WORKDIR /root
RUN rm -rf /root/xnvme