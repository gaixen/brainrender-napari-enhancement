# brainrender-napari-enhancement

This napari plugin allows users to load and visualize publicly available atlas-registered mouse brain data in a graphical interface.

## Installation
```bash
pip install -e .
```

## Usage
```python
import napari
from brainrender_napari import load_mouse_data

viewer = napari.Viewer()
load_mouse_data(viewer)  # Loads and renders sample data
```

## Features
- Dataset selection via dropdown
- 3D rendering of anatomical structures
- Napari dock widget built with `magicgui`

## Requirements
- Python >= 3.8
- napari
- brainrender
- bg-atlasapi
- magicgui

## License
MIT

## Sample Code Snippet (widget.py)
```python
from magicgui import magic_factory
from napari.types import Viewer
from brainrender import Scene
from brainrender.atlas_specific import get_atlas

@magic_factory(call_button='Load Atlas Data')
def load_brain_data(viewer: Viewer, species: str = 'mouse'):
    atlas = get_atlas(species)
    scene = Scene(atlas_name=atlas.name)
    for region in ['TH', 'MB', 'CB']:  # Example regions
        scene.add_brain_region(region)
    scene.render()
