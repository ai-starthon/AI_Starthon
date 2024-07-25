#nsml: nsml/default_ml:cuda9_torch1.0
from distutils.core import setup

setup(
    name='koreanfood',
    version='1.0',
    install_requires=['torch==2.2.0',
                      'torchvision==0.2.1',
                      'tqdm']
)
