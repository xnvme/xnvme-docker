FROM debian:bullseye
LABEL maintainer="os@safl.dk"
RUN mkdir -p /opt
COPY xnvme/toolbox /opt/toolbox
WORKDIR /opt
RUN bash -e ./toolbox/pkgs/debian-bullseye.sh
WORKDIR /root
CMD ["bash"]