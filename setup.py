from setuptools import setup, find_packages
setup(
    name="wix_utils",
    version="0.1",
    license="MIT",
    packages=find_packages(),
    install_requires=[],
    extras_require={
        'download': ["requests"]
    },
    project_urls={
        'Source': 'https://github.com/metamorph-inc/wix-utils',
    },
)
