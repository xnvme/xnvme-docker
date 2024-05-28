FROM fedora:41
LABEL maintainer "os@safl.dk"
RUN mkdir -p /opt
COPY xnvme/toolbox /opt/toolbox
WORKDIR /opt
RUN bash -e ./toolbox/pkgs/fedora-41.sh
WORKDIR /root
CMD ["bash"]