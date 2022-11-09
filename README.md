# xnvme-docker

Docker Images tailored for xNVMe

* Utilize the same "installation-instructions" as described in the xNVMe docs
* Provide tags for the xNVMe next branch
  - Update these daily
* Provide tags for releases
  - Preferably update these at the point in time where the release of xNVMe is made

## Maintenance Notes

When changes are made to Linux distribution support for xNVMe, that is, new distros added, or
current distributions removed, then:

* The content of the folder ``dockerfiles`` needs to be updated.
* The workflow needs adjustment ``.github/workflows/dcgen.yml``

Do so by:

* Match the distributions in ``xnvme-docker/.github/workflows/dcgen.yml``
* Match the distributions in ``xnvme/.github/workflows/verify.yml`` for build-linux
