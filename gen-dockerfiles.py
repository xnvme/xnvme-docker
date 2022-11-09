#!/usr/bin/env python3
"""
    Generate a 'Dockerfile' for each distro defined in '.github/workflows/dcgen.yml'

    It uses a jinja2 template in 'dockerfile.template'
"""
from pathlib import Path
from jinja2 import Template
import yaml

def main():

    with Path(".github/workflows/dcgen.yml").open() as yfile:
        raw = yaml.safe_load(yfile)

    with Path("dockerfile.template").open() as tfile:
        template = Template(tfile.read())

    distros = raw["jobs"]["dockerize"]["strategy"]["matrix"]["container"]
    for distro in distros:
        path = Path("dockerfiles") / distro["os"] / distro["ver"] / "Dockerfile"
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w") as dfile:
            dfile.write(template.render(distro=distro))

if __name__ == "__main__":
    main()
