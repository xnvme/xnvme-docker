FROM opensuse/tumbleweed:latest
LABEL maintainer "os@safl.dk"
RUN mkdir -p /root/xnvme
WORKDIR /root/xnvme
COPY xnvme .
RUN bash -e ./toolbox/pkgs/opensuse-tumbleweed-latest.sh
WORKDIR /root
CMD ["bash"]