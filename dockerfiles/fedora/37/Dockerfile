FROM fedora:37
LABEL maintainer "os@safl.dk"
RUN mkdir -p /root/xnvme
WORKDIR /root/xnvme
COPY xnvme .
RUN bash -e ./toolbox/pkgs/fedora-37.sh
WORKDIR /root
CMD ["bash"]