from .node_env import NodeEnv
from .exceptions import NpmDirectory, NodeInstallationException, \
    ReactComponentNotFound
from .component import ReactComponent
import os, sys


class ReactiPy(NodeEnv):
    root_dir = None
    components = []

    def __init__(self, root_dir=None, node_env=None, npm_env=None):
        """
        :param root_dir: Directory path that your react jsx/js components are in.
        :param node_env: (optional) Path to a node environment otherwise  a node environment will be created automatically
        :param npm_env: (optional) Path to a npm environment. ***This must be included if node_env is passed.***
        :return:
        """
        ### checks if node_env was included otherwise will install a new environment if the package one does not exist
        if node_env:
            self.node_env = node_env
            self.install_npm_requirements()
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


    def register_component(self, file, name='test'):

        comp_path = os.path.join(self.root_dir, file) if self.root_dir else file

        if not os.path.exists(comp_path):
            raise ReactComponentNotFound(comp_path + '  could not be found')

        new_component = ReactComponent(name, comp_path)
        self.components.append(new_component)

        return new_component


