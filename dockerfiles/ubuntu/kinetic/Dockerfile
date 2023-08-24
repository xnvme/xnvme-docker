FROM ubuntu:kinetic
LABEL maintainer "os@safl.dk"
RUN mkdir -p /root/xnvme
WORKDIR /root/xnvme
COPY xnvme .
RUN bash ./toolbox/pkgs/ubuntu-kinetic.sh
WORKDIR /root
CMD ["bash"]