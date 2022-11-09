FROM debian:buster
LABEL maintainer "os@safl.dk"
RUN mkdir -p /root/xnvme
WORKDIR /root/xnvme
COPY xnvme .
RUN ./toolbox/pkgs/debian-buster.sh
WORKDIR /root
CMD ["bash"]