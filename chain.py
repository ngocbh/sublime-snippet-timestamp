
# uasge:
# window.run_command("chain",{"commands":[["select_all"],["copy"]]})
# or
# {
#   "keys": ["super+shift+option+d"], 
#   "command": "chain", 
#   "args": {
#     "commands": [
#       ["select_all"],
#       ["copy"],
#       ["new_file"],
#       ["paste"],
#       ["save"]
#     ]
#   }
# }

import sublime
import sublime_plugin

class ChainCommand(sublime_plugin.WindowCommand):
    def run(self, commands):
        window = self.window
        for command in commands:
            command_name = command[0]
            command_args = command[1:]
            window.run_command(command_name, *command_args)