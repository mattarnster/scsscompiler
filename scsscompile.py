import sublime, sublime_plugin, re
from subprocess import Popen, PIPE, STDOUT
from sys import platform

if platform == 'win32':
    scss = 'scss.bat'
else:
    scss = '/usr/local/bin/scss'

class scsscompileCommand(sublime_plugin.TextCommand):
  def run(self, edit, minify = False):
    for region in self.view.sel():  
            if not region.empty():
                # Get the selected text  
                s = self.view.substr(region)
                p = Popen([scss], stdout=PIPE, stdin=PIPE, stderr=PIPE)
                stdout_data = p.communicate(input=bytes(s, 'UTF-8'))[0]
                # print(stdout_data)
                stdout_data = str(stdout_data).replace('\\n', '\n').replace('\\r', '')
                stdout_data = stdout_data[2:-2]
                if minify:
                    stdout_data = str(stdout_data).replace('\n', '').replace('\r', '').replace(' ', '')
                    stdout_data = re.sub(r'\/\*.+\*\/', '', stdout_data)
                    stdout_data = re.sub(r'\;\}', '}', stdout_data)
                self.view.replace(edit, region, stdout_data)