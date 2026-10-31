# xnvme-docker

**Archived.** The per-distribution dependency images now come from the
[xNVMe repository](https://github.com/xnvme/xnvme) itself, and nothing here is
built or maintained any more.

## What replaced it

xNVMe's `distro-deps` workflow builds one image per Linux distribution from
`toolbox/pkgs/Dockerfile`, running the distribution's
`toolbox/pkgs/<os>-<ver>.sh`, and publishes it as:

    ghcr.io/xnvme/xnvme/distro-deps-<os>-<ver>:main

The images are rebuilt whenever `main` changes, and xNVMe's CI builds and
verifies in them.

For the development and CI environment, the host container with the tools,
the guest images, and the rigs that boot QEMU guests, see
[xnvme-devenv](https://github.com/xnvme/xnvme-devenv).

## Why

The images were built from the `toolbox/pkgs` scripts on xNVMe's
`dockerize-for-*` branches, so a change to a distribution's dependencies had
to land in two repositories and on a side branch before CI could use it, and
the distribution list was kept in sync by hand in both places. Building the
images in the repository that owns the scripts removes both.

## The old images

The images published here, `ghcr.io/xnvme/xnvme-deps-<os>-<ver>:main`, remain
on the GitHub Container Registry and can still be pulled, but are no longer
rebuilt, so their packages go out of date.
