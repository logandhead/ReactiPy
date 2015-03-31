from .settings import NODE_ENV, REACTIPY_JS
import exceptions as exceptions
import json
import subprocess


class ReactComponent(object):
    path = None
    static = True
    props = None
    container = None
    cmd = None
    props_reference = 'hello'

    def __init__(self, container=None, props_reference=None):
        # As we use the subclass's name to generate a number of client-side
        # variables, we disallow directly calling the ReactComponent class
        if self.__class__ is ReactComponent:
            raise ('Components must inherit from ReactComponent')
        # Sanity check
        if self.get_path() is None:
            raise ('Path not specified')

        self.container = container
        self.props_reference = props_reference

    def render(self, **kwargs):
        if kwargs:
            self.props = kwargs

        return self.compile_component()

    def render_to_string(self, **kwargs):
        if kwargs:
            self.props = kwargs

        self.static = False
        string_html = self.compile_component()
        self.static = True

        return string_html

    def build_input(self):
        self.cmd = [NODE_ENV, REACTIPY_JS,
                    '--path-to-source', self.path,
                    '--static-markup', '1' if self.static else '0',

                    '--props-reference', str(self.props_reference)]

        if self.props:
            self.cmd.append('--react-props')
            self.cmd.append(json.dumps(self.props))

        if self.container:
            self.cmd.append('--component-container')
            self.cmd.append(self.container)

    def compile_component(self):
        self.build_input()
        try:
            pipe = subprocess.Popen(self.cmd, stdout=subprocess.PIPE)
            pipe.wait()
            results = pipe.communicate()[0]
            return results
        except exceptions.NodeCompileError:
            return None

    def get_path(self):
        return self.path







