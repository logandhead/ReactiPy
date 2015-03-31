from reactipy.settings import NODE_ENV, REACTIPY_JS
import reactipy.exceptions as exceptions
import json
import subprocess


class ReactComponent(object):
    static = True
    props = None
    container = None
    cmd = None
    props_reference = 'hello'

    def __init__(self):
        self.build_input()

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


    def render(self):
        try:
            pipe = subprocess.Popen(self.cmd, stdout=subprocess.PIPE)
            pipe.wait()
            results = pipe.communicate()[0]
            return results
        except exceptions.NodeCompileError:
            return None


    def addProps(self, newProps):
        self.props = newProps
        self.build_input()






