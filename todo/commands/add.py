from __future__ import absolute_import

import os
import sys
import json

from todo.commands.base import Command
from todo.utils.styles import Fore, Style


class AddCommand(Command):
    def run(self):
        for item in self.get_titles_input():
            new_item = {"completed": False, "title": item}
            self.update_project(new_item)


Add = AddCommand()
