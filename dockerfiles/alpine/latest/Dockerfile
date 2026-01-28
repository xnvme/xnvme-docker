FROM refenv/alpine-bash:latest
LABEL maintainer="os@safl.dk"
RUN mkdir -p /opt
COPY xnvme/toolbox /opt/toolbox
WORKDIR /opt
RUN bash -e ./toolbox/pkgs/alpine-latest.sh
WORKDIR /root
CMD ["bash"]