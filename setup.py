import os

from setuptools import setup
from setuptools.extension import Extension
import sphinx.apidoc
from sphinx.setup_command import BuildDoc


class BuildDocApiDoc(BuildDoc, object):
    # inherit from object to enable 'super'
    user_options = []
    description = "sphinx"

    def run(self):
        # metadata contains information supplied in setup()
        metadata = self.distribution.metadata
        # package_dir may be None, in that case use the current directory.
        src_dir = (self.distribution.package_dir or {"": ""})[""]
        src_dir = os.path.join(os.getcwd(), src_dir)
        # Run sphinx by calling the main method, '--full' also adds a conf.py
        sphinx.apidoc.main(
            [
                "",
                "-f",
                "-H",
                metadata.name,
                "-A",
                metadata.author,
                "-V",
                metadata.version,
                "-R",
                metadata.version,
                "-T",
                "-o",
                os.path.join("doc", "source", "modules"),
                src_dir,
            ]
        )
        super(BuildDocApiDoc, self).run()


name = "my_project"
version = "0.1"
release = "0.1.0"

setup(
    name=name,
    author="koreyou",
    version=version,
    packages=[
        "my_project",
    ],
    license="Creative Commons BY",
    cmdclass={"build_sphinx": BuildDocApiDoc},
    command_options={
        "build_sphinx": {
            "project": ("setup.py", name),
            "version": ("setup.py", version),
            "release": ("setup.py", release),
        }
    },
    setup_requires=["sphinx"],
)
