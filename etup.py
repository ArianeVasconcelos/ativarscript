from setuptools import setup, find_packages

setup(
    name='ativarscript',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # Liste as dependências necessárias aqui
        'selenium',
        'requests',
        'unidecode',
        'selenium_dolphin',
    ],
)
