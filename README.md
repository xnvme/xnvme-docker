# xnvme-docker

Docker Images tailored for xNVMe, distributed as GitHUB Packages via the GitHUB Container Registry.
See the list of Docker Images [here](https://github.com/orgs/xnvme/packages?repo_name=xnvme-docker).

The Docker Images contain the build and runtime requirements for xNVMe. That is, the tools and
libraries needed to build and run xNVMe.

* Utilize the same "installation-instructions" as described in the xNVMe docs
* Provide tags for the xNVMe next branch
  - Update these daily
* Provide tags for releases
  - Preferably update these at the point in time where the release of xNVMe is made

## Usage

The docker image generated here are intended to be used by the xNVMe GitHUB actions. However, they
can of course be utilized manually, for example::

    docker run -it ghcr.io/xnvme/xnvme-deps-alpine-latest:next bash

## Maintenance Notes

When changes are made to Linux distribution support for xNVMe, that is, new distros added, or
current distributions removed, then:

* The content of the folder ``dockerfiles`` needs to be updated.
* The workflow needs adjustment ``.github/workflows/dcgen.yml``

Do so by:

* Match the distributions in ``xnvme-docker/.github/workflows/dcgen.yml``
* Match the distributions in ``xnvme/.github/workflows/verify.yml`` for build-linux
