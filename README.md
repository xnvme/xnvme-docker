# xnvme-docker

Docker images tailored for xNVMe, distributed as GitHUB Packages via the GitHUB Container Registry.
See the list of Docker images [here](https://github.com/orgs/xnvme/packages?repo_name=xnvme-docker).

The Docker images contain the build and runtime requirements for xNVMe on Linux. That is, the tools
and libraries needed to build and run xNVMe.

* Utilize the same "installation-instructions" as described in the xNVMe docs
  - A convenient side-effect is that the instructions are continously "tested"
* Updated every 12th hour

## Usage

The Docker images generated here are intended to be used by the xNVMe GitHUB actions. However, they
can of course be utilized manually, for example::

    docker run -it ghcr.io/xnvme/xnvme-deps-alpine-latest:main bash

## Container types

Three kinds of images are produced, each from its own template in ``templates/``:

* **deps** (``distro.template``) — one per Linux distribution; runs the distro's
  ``toolbox/pkgs/<os>-<ver>.sh`` install-script from the xNVMe repository. Published as
  ``ghcr.io/xnvme/xnvme-deps-<os>-<ver>:main``.
* **citools** (``citools.template``) — based on the fedora deps image, adds CI tooling
  (clang-format, pre-commit, shellcheck, doxygen, kmdo, ...). Published as
  ``ghcr.io/xnvme/xnvme-deps-fedora-citools:main``.
* **packaging** (``packaging-debian.template``) — Debian with the packaging toolchain
  (debhelper, devscripts, lintian, ...). Published as
  ``ghcr.io/xnvme/xnvme-deps-debian-packaging:main``.

## Use in xNVMe CI

The consumer is the [verify.yml](https://github.com/xnvme/xnvme/blob/main/.github/workflows/verify.yml)
workflow in the xNVMe repository. As of June 2026 the jobs map to images as follows:

| verify.yml job        | Image                                              |
|-----------------------|----------------------------------------------------|
| ``source-archive``    | ``xnvme-deps-alpine-latest:main``                  |
| ``source-format-check`` | ``xnvme-deps-fedora-citools:main``               |
| ``test-gen-targets``  | ``xnvme-deps-citools-latest:main`` (stale, see below) |
| ``build-rust``        | ``xnvme-deps-debian-trixie:main``                  |
| ``build-python``      | ``xnvme-deps-debian-trixie:main``                  |
| ``build-linux``       | ``xnvme-deps-<os>-<ver>:main`` (17-distro matrix)  |
| ``packaging-debian``  | ``xnvme-deps-debian-packaging:main``               |
| ``verify``, ``docgen`` | ``ghcr.io/safl/nosi/ubuntu-2604-docker:latest`` (from [nosi](https://github.com/safl/nosi), not built here) |
| ``verify-physical``   | plain ``debian:trixie`` (not built here)           |

Notes:

* ``xnvme-deps-citools-latest:main`` is a **stale** package from November 2023; the citools
  image was since renamed (``citools/latest`` → ``debian/citools`` → ``fedora/citools``) and the
  old name is no longer rebuilt. The ``test-gen-targets`` job should be pointed at
  ``xnvme-deps-fedora-citools:main`` instead.
* Built here but currently unused by verify.yml: ``debian-bullseye`` and ``rockylinux-10.1``
  (the matrix uses ``rockylinux-9.7``).
* The distro-matrix in ``build-linux`` is maintained by hand in verify.yml — keep it in sync
  with the matrix in ``.github/workflows/dockerize.yml`` here.

### Buildtime / Motivation for this

Generating the Docker-images and deploying them to the GitHUB container registry takes about 20
minutes. The actual "build-time" varies by Linux Distribution from 1-18 minutes. The build-time is
spend on updating distro-package-repositories, installing packages, building and installing other
tools/libraries from source.

For bleeding edge distros, it takes about a minute, except for Gentoo which builds everything from
source, this takes about 18mintes. The others vary based on a variety of factors. In some cases the
build fails because distro-repositories time out, become unavailable, and in other ways "fail". To
avoid these and reduce the time on xNVMe CI jobs, then these Docker images are provided.

The CI still have to wait for Windows, MacOS, and FreeBSD. It also does not help for the CI-jobs
doing "verification" with emulated NVMe devices. However, it makes a lot more convenient when
debugging build-issues on the various distributions, and for the basic 'build-linux' jobs, reduces
time spent by about 16min.

## Maintenance (deps)

When changes are made to Linux distribution support for xNVMe, that is, new distros added, or
current distributions removed, then:

* Adjust the workflow ``.github/workflows/dockerize.yml``
  - it has the list of Linux distributions it is generating Docker images for
  - the list is also used by the ``gen-dockerfiles.py``
* Adjust the Dockerfile in ``dockerfiles/*``
  - Remove all: ``rm -rf dockerfiles``
  - Generate them: ``python3 gen-dockerfiles.py``
* Commit and push the changes
* New "packages" need to change visibility from ``private`` to ``public``
  - Go to the landing packge for the Docker Image / package
  - Click on Package Settings
  - Scroll to the bottom and blick on "Change Visilibility"

## Wishlist

* Generate images for arm64
* Tag/label matching xNVMe releases
