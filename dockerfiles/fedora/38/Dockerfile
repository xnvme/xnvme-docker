FROM fedora:38
LABEL maintainer "os@safl.dk"
RUN mkdir -p /opt
COPY xnvme/toolbox /opt/toolbox
WORKDIR /opt
RUN bash -e ./toolbox/pkgs/fedora-38.sh
WORKDIR /root
CMD ["bash"]