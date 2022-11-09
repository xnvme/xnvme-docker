FROM gentoo/stage3:latest
LABEL maintainer "os@safl.dk"
RUN mkdir -p /root/xnvme
WORKDIR /root/xnvme
COPY xnvme .
RUN bash ./toolbox/pkgs/gentoo-latest.sh
WORKDIR /root
RUN rm -rf /root/xnvme