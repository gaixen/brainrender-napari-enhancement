from setuptools import setup

setup(
    name='brainrender-napari-enhancement',
    version='0.1',
    author='Soham',
    description='A napari plugin to visualize atlas-registered brain data',
    packages=['brainrender_napari'],
    install_requires=[
        'napari',
        'brainrender',
        'bg-atlasapi',
        'magicgui'
    ],
    entry_points={
        'napari.plugin': [
            'brainrender-napari-enhancement = brainrender_napari'
        ]
    },
)