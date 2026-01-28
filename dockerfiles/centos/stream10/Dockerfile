FROM quay.io/centos/centos:stream10
LABEL maintainer="os@safl.dk"
RUN mkdir -p /opt
COPY xnvme/toolbox /opt/toolbox
WORKDIR /opt
RUN bash -e ./toolbox/pkgs/centos-stream10.sh
WORKDIR /root
CMD ["bash"]