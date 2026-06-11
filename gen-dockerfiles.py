#!/usr/bin/env python3
"""
    Generate a 'Dockerfile' for each distro defined in '.github/workflows/dockerize.yml'

    Each matrix-entry is rendered using 'templates/<kind>.template', where 'kind'
    defaults to 'distro'. The only other kind is 'citools'; CI and Debian
    packaging tooling on top of a deps-image.
"""
from pathlib import Path
from jinja2 import Template
import yaml


def get_distros():
    """Returns a list of distributions to generate docker images for."""

    with Path(".github/workflows/dockerize.yml").open() as yfile:
        raw = yaml.safe_load(yfile)

    return raw["jobs"]["dockerize"]["strategy"]["matrix"]["container"]


def main():
    templates = {
        p.stem: Template(p.open().read())
        for p in (Path.cwd() / "templates").glob("*.template")
    }

    for distro in get_distros():
        path = Path("dockerfiles") / distro["os"] / distro["ver"] / "Dockerfile"
        path.parent.mkdir(parents=True, exist_ok=True)

        template = templates[distro.get("kind", "distro")]

        with path.open("w") as dfile:
            dfile.write(template.render(distro=distro))


if __name__ == "__main__":
    main()
