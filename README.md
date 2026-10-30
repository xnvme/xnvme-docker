# xnvme-docker

Docker images with the build and runtime dependencies of xNVMe, one per Linux distribution,
distributed via the GitHub Container Registry. See the list of images
[here](https://github.com/orgs/xnvme/packages?repo_name=xnvme-docker).

This repository has one purpose: the per-distribution images that xNVMe's CI builds and tests
xNVMe on. For the development and CI environment, the host container with the tools, the guest
images and the rigs that boot QEMU guests with emulated or passed-through devices, see
[xnvme-devenv](https://github.com/xnvme/xnvme-devenv).

* Each image installs its dependencies with the distribution's ``toolbox/pkgs/<os>-<ver>.sh``
  script from the xNVMe repository, the same script xNVMe's documentation tells users to run,
  so the documented installation instructions are continuously tested
* Rebuilt every 12th hour and on every push to ``main``
* Published as ``ghcr.io/xnvme/xnvme-deps-<os>-<ver>:main``

## Usage

The images are intended for xNVMe's GitHub Actions. They can also be used by hand, for example
to debug a build problem on a given distribution:

    docker run -it ghcr.io/xnvme/xnvme-deps-alpine-latest:main bash

## Use in xNVMe CI

| xNVMe workflow and job                | Image                                             |
|---------------------------------------|---------------------------------------------------|
| ``build.yml``, the Linux build matrix | ``xnvme-deps-<os>-<ver>:main``, one per distro    |
| ``verify.yml``, ``source-archive``    | ``xnvme-deps-alpine-latest:main``                 |
| ``verify.yml``, ``ffi-python``        | ``xnvme-deps-debian-trixie:main``                 |
| ``verify.yml``, ``ffi-rust``          | ``xnvme-deps-debian-trixie:main``                 |

The other jobs run in xnvme-devenv's host container.

The Linux build matrix is listed by hand in the ``matrices`` job of xNVMe's ``verify.yml``. Keep
it in sync with the matrix in ``.github/workflows/dockerize.yml`` here. ``rockylinux-10.1`` is
built here but not yet in xNVMe's matrix.

## Why

Installing the dependencies takes from about a minute on most distributions to about 18 minutes
on Gentoo, which builds everything from source. Distribution package repositories also time out
or become unavailable now and then. Building the images here, every 12 hours, takes that time
and those failures out of every xNVMe CI run.

## Maintenance

The Dockerfiles under ``dockerfiles/`` are generated: never edit them by hand. When xNVMe adds
or drops a Linux distribution:

* Edit the matrix in ``.github/workflows/dockerize.yml``
* Regenerate the Dockerfiles with ``rm -rf dockerfiles`` and ``python3 gen-dockerfiles.py``
  (needs ``jinja2`` and ``pyyaml``)
* Commit both; the ``gen-check`` job fails when the committed Dockerfiles differ from the
  generated ones
* The matching ``toolbox/pkgs/<os>-<ver>.sh`` must exist on xNVMe's ``dockerize-for-main``
  branch, which the images are built from
* A new package on ghcr.io may start as ``private``. Make it public in the package's settings,
  under "Change Visibility"

## Wishlist

* Generate images for arm64
* Tag/label matching xNVMe releases
