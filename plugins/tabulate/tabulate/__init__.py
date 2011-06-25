# Copyright (c) 2011 Hugo Henriques Maia Vieira
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from gettext import gettext as _

import gtk
import gedit

from table import Table, DifferentNumberOfColumnsError, WhiteSpacesError

# Menu item example, insert a new item in the Tools menu
ui_str = """<ui>
  <menubar name="MenuBar">
    <menu name="EditMenu" action="Edit">
      <placeholder name="EditOps_6">
        <menuitem name="Tabulate" action="Tabulate"/>
      </placeholder>
    </menu>
  </menubar>
</ui>
"""
class TabulateWindowHelper:
    def __init__(self, plugin, window):
        self._window = window
        self._plugin = plugin

        # Insert menu items
        self._insert_menu()

    def deactivate(self):
        # Remove any installed menu items
        self._remove_menu()

        self._window = None
        self._plugin = None
        self._action_group = None

    def _insert_menu(self):
        # Get the GtkUIManager
        manager = self._window.get_ui_manager()

        # Create a new action group
        self._action_group = gtk.ActionGroup("TabulateActions")
        self._action_group.add_actions([("Tabulate",
                                         None,
                                         _("Tabulate"),
                                         '<Control>t',
                                         _("Tabulate the text block"),
                                         self.on_tabulate_activate)])

        # Insert the action group
        manager.insert_action_group(self._action_group, -1)

        # Merge the UI
        self._ui_id = manager.add_ui_from_string(ui_str)

    def _remove_menu(self):
        # Get the GtkUIManager
        manager = self._window.get_ui_manager()

        # Remove the ui
        manager.remove_ui(self._ui_id)

        # Remove the action group
        manager.remove_action_group(self._action_group)

        # Make sure the manager updates
        manager.ensure_update()

    def update_ui(self):
        self._action_group.set_sensitive(self._window.get_active_document() != None)

    # Menu activate handlers
    def on_tabulate_activate(self, action):
        doc = self._window.get_active_document()
        bounds = doc.get_selection_bounds()
        if not doc or not bounds:
            return
        text = doc.get_text(*bounds)
        try:
            table = Table(text)
            text_tabulated = table.organize()
            doc.delete_interactive(*bounds, default_editable=True)
            doc.insert(bounds[0], text_tabulated)
        except WhiteSpacesError:
            return
        except DifferentNumberOfColumnsError:
            message = gtk.MessageDialog(None, 0, gtk.MESSAGE_WARNING, gtk.BUTTONS_OK,
                                        'Wrong number of columns. Check the selected block.')
            message.run()
            message.destroy()


class TabulatePlugin(gedit.Plugin):
    def __init__(self):
        gedit.Plugin.__init__(self)
        self._instances = {}

    def activate(self, window):
        self._instances[window] = TabulateWindowHelper(self, window)

    def deactivate(self, window):
        self._instances[window].deactivate()
        del self._instances[window]

    def update_ui(self, window):
        self._instances[window].update_ui()

