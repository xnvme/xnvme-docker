#!/usr/bin/env python3
"""
    Generate a 'Dockerfile' for each distro defined in '.github/workflows/dockerize.yml'

    Each matrix-entry is rendered using 'templates/distro.template'.
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
    template = Template(
        (Path.cwd() / "templates" / "distro.template").read_text(), keep_trailing_newline=True
    )

    for distro in get_distros():
        path = Path("dockerfiles") / distro["os"] / distro["ver"] / "Dockerfile"
        path.parent.mkdir(parents=True, exist_ok=True)

        with path.open("w") as dfile:
            dfile.write(template.render(distro=distro))


if __name__ == "__main__":
    main()
