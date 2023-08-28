FROM opensuse/leap:15.3
LABEL maintainer "os@safl.dk"
RUN mkdir -p /root/xnvme
WORKDIR /root/xnvme
COPY xnvme .
RUN bash -e ./toolbox/pkgs/opensuse-leap-15.3.sh
WORKDIR /root
CMD ["bash"]