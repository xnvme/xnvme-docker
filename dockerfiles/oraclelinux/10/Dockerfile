FROM oraclelinux:10
LABEL maintainer="os@safl.dk"
RUN mkdir -p /opt
COPY xnvme/toolbox /opt/toolbox
WORKDIR /opt
RUN bash -e ./toolbox/pkgs/oraclelinux-10.sh
WORKDIR /root
CMD ["bash"]