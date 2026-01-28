FROM rockylinux:9.6
LABEL maintainer "os@safl.dk"
RUN mkdir -p /opt
COPY xnvme/toolbox /opt/toolbox
WORKDIR /opt
RUN bash -e ./toolbox/pkgs/rockylinux-9.6.sh
WORKDIR /root
CMD ["bash"]