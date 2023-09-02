FROM debian:trixie
LABEL maintainer "os@safl.dk"
RUN mkdir -p /opt
COPY xnvme/toolbox /opt/toolbox
WORKDIR /opt
RUN bash -e ./toolbox/pkgs/debian-trixie.sh
WORKDIR /root
CMD ["bash"]