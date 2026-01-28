FROM archlinux:latest
LABEL maintainer="os@safl.dk"
RUN mkdir -p /opt
COPY xnvme/toolbox /opt/toolbox
WORKDIR /opt
RUN bash -e ./toolbox/pkgs/archlinux-latest.sh
WORKDIR /root
CMD ["bash"]