FROM debian:bullseye
LABEL maintainer "os@safl.dk"
RUN mkdir -p /root/xnvme
WORKDIR /root/xnvme
COPY xnvme .
RUN bash ./toolbox/pkgs/debian-bullseye.sh
WORKDIR /root
CMD ["bash"]