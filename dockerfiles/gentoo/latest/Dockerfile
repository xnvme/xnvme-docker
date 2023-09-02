FROM gentoo/stage3:latest
LABEL maintainer "os@safl.dk"
RUN mkdir -p /opt
COPY xnvme/toolbox /opt/toolbox
WORKDIR /opt
RUN bash -e ./toolbox/pkgs/gentoo-latest.sh
WORKDIR /root
CMD ["bash"]