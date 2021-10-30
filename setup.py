from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in gcm/__init__.py
from gcm import __version__ as version

setup(
	name="gcm",
	version=version,
	description="Management modules for a Gliding Club",
	author="Lucas James",
	author_email="lucas.james@ldjcs.com.au",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
