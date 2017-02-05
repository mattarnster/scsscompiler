import sublime, sublime_plugin
from subprocess import Popen, PIPE, STDOUT
from sys import platform

if platform == 'win32':
    scss = 'scss.bat'
else:
    scss = '/usr/local/bin/scss'

class scsscompileCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    for region in self.view.sel():
            if not region.empty():
                # Get the selected text
                s = self.view.substr(region)
                p = Popen([scss], stdout=PIPE, stdin=PIPE, stderr=PIPE)
                stdout_data = p.communicate(input=bytes(s, 'UTF-8'))[0]
                # print(stdout_data)
                stdout_data = str(stdout_data).replace('\\n', '\n').replace('\\r', '')
                stdout_data = stdout_data[2:-2]
                self.view.replace(edit, region, stdout_data)