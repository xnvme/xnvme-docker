FROM debian:bookworm
LABEL maintainer "os@safl.dk"
RUN mkdir -p /opt
COPY xnvme/toolbox /opt/toolbox
WORKDIR /opt
RUN bash -e ./toolbox/pkgs/debian-bookworm.sh
WORKDIR /root
CMD ["bash"]