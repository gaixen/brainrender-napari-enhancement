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
