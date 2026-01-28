FROM opensuse/tumbleweed:latest
LABEL maintainer="os@safl.dk"
RUN mkdir -p /opt
COPY xnvme/toolbox /opt/toolbox
WORKDIR /opt
RUN bash -e ./toolbox/pkgs/opensuse-tumbleweed-latest.sh
WORKDIR /root
CMD ["bash"]