from .settings import NODE_ENV,  REACTIPY_JS, NODE_ACTIVATE_PATH
import exceptions as exceptions
import json
from subprocess import Popen, PIPE, STDOUT
import os


class ReactComponent(object):
    path = None
    static = True
    props = None
    container = 'hellow'
    cmd = None
    props_reference = 'App_Props'
    name = None

    def __init__(self, name, path):
        # As we use the subclass's name to generate a number of client-side
        # variables, we disallow directly calling the ReactComponent class
        self.name = name
        self.path = path

    def render(self, **kwargs):
        if kwargs:
            self.props = kwargs

        rendered = self._compile_component()
        return rendered

    def render_to_string(self, **kwargs):
        if kwargs:
            self.props = kwargs

        self.static = False
        string_html = self._compile_component()
        self.static = True

        return string_html

    def _build_input(self):
        self.cmd = [
                    NODE_ENV, REACTIPY_JS,
                    '--path-to-source', self.path,
                    '--static-markup', '1' if self.static else '0',
                    '--props-reference', str(self.props_reference)]

        if self.props:
            self.cmd.append('--react-props')
            self.cmd.append(json.dumps(self.props))

        if self.container:
            self.cmd.append('--component-container')
            self.cmd.append(self.container)

    def _compile_component(self):
        self._build_input()
        self.process = Popen(self.cmd, stdout=PIPE, stdin=PIPE)
        self.process.wait()
        print self.process.communicate()



def get_path(self):
    return self.path







