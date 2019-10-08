import datetime
import sublime, sublime_plugin
 
class TimestampCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    timestamp = "[%s]\t" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
    snippet = "Packages/User/cpp_template.sublime-snippet"
    self.view.run_command("insert_snippet", {"name": snippet, "DATE": timestamp})

