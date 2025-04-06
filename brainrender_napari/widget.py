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
