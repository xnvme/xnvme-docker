FROM fedora:36
LABEL maintainer "os@safl.dk"
RUN mkdir -p /root/xnvme
WORKDIR /root/xnvme
COPY xnvme .
RUN bash ./toolbox/pkgs/fedora-36.sh
WORKDIR /root
RUN rm -rf /root/xnvme