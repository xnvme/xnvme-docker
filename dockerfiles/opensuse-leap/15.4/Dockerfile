FROM opensuse/leap:15.4
LABEL maintainer "os@safl.dk"
RUN mkdir -p /opt
COPY xnvme/toolbox /opt/toolbox
WORKDIR /opt
RUN bash -e ./toolbox/pkgs/opensuse-leap-15.4.sh
WORKDIR /root
CMD ["bash"]