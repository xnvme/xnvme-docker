FROM archlinux:latest
LABEL maintainer "os@safl.dk"
RUN mkdir -p /root/xnvme
WORKDIR /root/xnvme
COPY xnvme .
RUN bash ./toolbox/pkgs/archlinux-latest.sh
WORKDIR /root
RUN rm -rf /root/xnvme