FROM opensuse/tumbleweed:latest
LABEL maintainer "os@safl.dk"
RUN mkdir -p /root/xnvme
WORKDIR /root/xnvme
COPY xnvme .
RUN ./toolbox/pkgs/opensuse-tumbleweed-latest.sh
WORKDIR /root
CMD ["bash"]