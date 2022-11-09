FROM debian:bookworm
LABEL maintainer "os@safl.dk"
RUN mkdir -p /root/xnvme
WORKDIR /root/xnvme
COPY xnvme .
RUN bash ./toolbox/pkgs/debian-bookworm.sh
WORKDIR /root
CMD ["bash"]