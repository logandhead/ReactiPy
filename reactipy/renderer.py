from .node_env import NodeEnv
from .exceptions import NpmDirectory, NodeInstallationException


class ReactiPy(NodeEnv):

    default_static_path = ''

    def __init__(self, static_path=None, node_env=None, npm_env=None):
        """
        :param static_path: Directory path that your react jsx/js components are in.
        :param node_env: (optional) Path to a node environment otherwise  a node environment will be created automatically
        :param npm_env: (optional) Path to a npm environment. ***This must be included if node_env is passed.***
        :return:
        """

        ### checks if node_env was included otherwise will install a new environment if the package one does not exist
        if node_env:
            self.node_env = node_env
            ### ensures that  npm_env was specified
            if npm_env:
                if not self.node_exist():
                    raise NodeInstallationException(
                        'The path to your specified node '
                        'environment does not exist.')
                else:
                    self.install_npm_requirements()
            else:
                raise NpmDirectory(
                    'You must specify the path to npm if you add a path for node'
                    ' rather than using the built in node/npm environments.')
        else:
            if not self.node_exist():
                self.install_node_environment()

    def render_component(self, path, props=None):

        pass
