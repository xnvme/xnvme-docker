FROM fedora:35
LABEL maintainer "os@safl.dk"
RUN mkdir -p /root/xnvme
WORKDIR /root/xnvme
COPY xnvme .
RUN bash ./toolbox/pkgs/fedora-35.sh
WORKDIR /root
RUN rm -rf /root/xnvme