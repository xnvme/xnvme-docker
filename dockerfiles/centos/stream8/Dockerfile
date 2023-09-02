FROM tgagor/centos:stream8
LABEL maintainer "os@safl.dk"
RUN mkdir -p /opt
COPY xnvme/toolbox /opt/toolbox
WORKDIR /opt
RUN bash -e ./toolbox/pkgs/centos-stream8.sh
WORKDIR /root
CMD ["bash"]