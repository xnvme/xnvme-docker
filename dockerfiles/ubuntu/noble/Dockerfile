FROM ubuntu:noble
LABEL maintainer="os@safl.dk"
LABEL org.opencontainers.image.source="https://github.com/xnvme/xnvme-docker"
RUN mkdir -p /opt
COPY xnvme/toolbox /opt/toolbox
WORKDIR /opt
RUN bash -e ./toolbox/pkgs/ubuntu-noble.sh
WORKDIR /root
CMD ["bash"]
