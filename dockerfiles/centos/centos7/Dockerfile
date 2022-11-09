FROM centos:centos7
LABEL maintainer "os@safl.dk"
RUN mkdir -p /root/xnvme
WORKDIR /root/xnvme
COPY xnvme .
RUN ./toolbox/pkgs/centos-centos7.sh
WORKDIR /root
CMD ["bash"]