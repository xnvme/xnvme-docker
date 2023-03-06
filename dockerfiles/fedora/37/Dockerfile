FROM fedora:37
LABEL maintainer "os@safl.dk"
RUN mkdir -p /root/xnvme
WORKDIR /root/xnvme
COPY xnvme .
RUN bash ./toolbox/pkgs/fedora-37.sh
WORKDIR /root
RUN rm -rf /root/xnvme