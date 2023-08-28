FROM debian:bookworm
LABEL maintainer "os@safl.dk"
RUN mkdir -p /root/xnvme
WORKDIR /root/xnvme
COPY xnvme .
RUN bash -e ./toolbox/pkgs/debian-bookworm.sh
WORKDIR /root
CMD ["bash"]