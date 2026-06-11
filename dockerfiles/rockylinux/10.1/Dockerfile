FROM rockylinux/rockylinux:10.1
LABEL maintainer="os@safl.dk"
RUN mkdir -p /opt
COPY xnvme/toolbox /opt/toolbox
WORKDIR /opt
RUN bash -e ./toolbox/pkgs/rockylinux-10.1.sh
WORKDIR /root
CMD ["bash"]
