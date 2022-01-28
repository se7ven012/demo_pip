from setuptools import setup

def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]

install_reqs = parse_requirements('requirements.txt')

setup(
    name='demo_pip',
    version='0.0.1',
    description='Demo python package',
    url='git@github.com:se7ven012/demo_pip.git',
    author='Zhaoyi',
    author_email='meng.zhaoyi@pluang.com',
    license='unlicense',
    packages=['demo_pip'],
    install_requires=install_reqs,
    zip_safe=False
)