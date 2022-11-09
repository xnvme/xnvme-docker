FROM centos:centos7
LABEL maintainer "os@safl.dk"
RUN mkdir -p /root/xnvme
WORKDIR /root/xnvme
COPY xnvme .
RUN bash ./toolbox/pkgs/centos-centos7.sh
WORKDIR /root
RUN rm -rf /root/xnvme