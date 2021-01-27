from typing import TYPE_CHECKING
from amulet_map_editor.api.opengl.mesh.selection import RenderSelectionGroup
from ..events import EVT_SELECTION_CHANGE

from .base_behaviour import BaseBehaviour

if TYPE_CHECKING:
    from amulet_map_editor.programs.edit.api.canvas import EditCanvas


class StaticSelectionBehaviour(BaseBehaviour):
    """Adds the logic for a static selection."""

    def __init__(self, canvas: "EditCanvas"):
        super().__init__(canvas)
        self._selection = RenderSelectionGroup(
            self.canvas.context_identifier,
            self.canvas.renderer.opengl_resource_pack,
        )

    def bind_events(self):
        self.canvas.Bind(EVT_SELECTION_CHANGE, self._update_selection)

    def _update_selection(self, evt):
        """Update the render selection based on the updated selection."""
        self._selection.selection_group = self.canvas.selection_.selection_group
        evt.Skip()

    def draw(self):
        self._selection.draw(self.canvas.camera.transformation_matrix, self.canvas.camera.location)
