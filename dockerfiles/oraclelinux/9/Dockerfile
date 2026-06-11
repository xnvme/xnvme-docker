FROM oraclelinux:9
LABEL maintainer="os@safl.dk"
LABEL org.opencontainers.image.source="https://github.com/xnvme/xnvme-docker"
RUN mkdir -p /opt
COPY xnvme/toolbox /opt/toolbox
WORKDIR /opt
RUN bash -e ./toolbox/pkgs/oraclelinux-9.sh
WORKDIR /root
CMD ["bash"]
