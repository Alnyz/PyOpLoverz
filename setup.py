from setuptools import setup, find_packages

with open("README.md", "r") as fp:
	long_desrib = fp.read()
	
install_require = [
					"requests",
					"bs4",
					"lxml"]

#package = ["pyoploverz"]

setup(
	name="pyoploverz",
	version="0.0.1",
	description="Unofficial wrapper anime from oploverz.in",
	author="Dyseo",
	author_email="katro.coplax@gmail.com",
	long_description=long_desrib,
	long_description_content_type="text/markdown",
	url="https://github.com/dyseo/PyOpLoverz",
	packages=find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3.6",
		"Programming Language :: Python :: 3.7",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
		"Topic :: Software Development :: Libraries :: Python Modules",
		"Topic :: Utilities",
		"Topic :: Internet",
	]
)
