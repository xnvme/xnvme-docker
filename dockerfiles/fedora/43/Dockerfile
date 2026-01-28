FROM fedora:43
LABEL maintainer "os@safl.dk"
RUN mkdir -p /opt
COPY xnvme/toolbox /opt/toolbox
WORKDIR /opt
RUN bash -e ./toolbox/pkgs/fedora-43.sh
WORKDIR /root
CMD ["bash"]