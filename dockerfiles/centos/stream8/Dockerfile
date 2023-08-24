FROM tgagor/centos:stream8
LABEL maintainer "os@safl.dk"
RUN mkdir -p /root/xnvme
WORKDIR /root/xnvme
COPY xnvme .
RUN bash ./toolbox/pkgs/centos-stream8.sh
WORKDIR /root
CMD ["bash"]