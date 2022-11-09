FROM refenv/alpine-bash:latest
LABEL maintainer "os@safl.dk"
RUN mkdir -p /root/xnvme
WORKDIR /root/xnvme
COPY xnvme .
RUN bash ./toolbox/pkgs/alpine-latest.sh
WORKDIR /root
RUN rm -rf /root/xnvme