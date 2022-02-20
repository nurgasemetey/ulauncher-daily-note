import logging
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.CopyToClipboardAction import CopyToClipboardAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
from ulauncher.api.shared.action.OpenAction import OpenAction
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction
import os
from datetime import datetime

logger = logging.getLogger(__name__)


class DemoExtension(Extension):
    def __init__(self):
        super(DemoExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(ItemEnterEvent, ItemEnterEventListener())


class KeywordQueryEventListener(EventListener):
    def on_event(self, event, extension):
        items = []

        note = {
            "data": event.get_argument(),
        }

        items.append(
            ExtensionResultItem(
                icon="images/icon.png",
                name="Create note",
                description="Enter to create note",
                on_enter=ExtensionCustomAction(note, keep_app_open=True),
            )
        )

        return RenderResultListAction(items)


def save_note(note, directory, filename_format, file_extension):
    file_path = get_file_path(directory, filename_format, file_extension)
    f = open(file_path, "a")
    f.write("%s\n" % note)
    f.close()


def get_file_path(directory, filename_format, file_extension):
    home = os.path.expanduser("~")
    directory_store = "%s/notes" % home
    if not os.path.exists(directory_store):
        os.makedirs(directory_store)
    if directory:
        directory_store = directory
    filename = datetime.today().strftime(filename_format)
    return directory_store + "/" + filename + file_extension


class ItemEnterEventListener(EventListener):
    def on_event(self, event, extension):
        note = event.get_data()
        save_note(
            note["data"],
            extension.preferences["directory"],
            extension.preferences["filename_format"],
            extension.preferences["file_extension"],
        )
        file_path = get_file_path(
            extension.preferences["directory"],
            extension.preferences["filename_format"],
            extension.preferences["file_extension"],
        )
        return RenderResultListAction(
            [
                ExtensionResultItem(
                    icon="images/open.png",
                    name="Open note",
                    description="Enter to open file or Escape to close",
                    on_enter=OpenAction(file_path),
                )
            ]
        )


if __name__ == "__main__":
    DemoExtension().run()
