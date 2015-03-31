import os
ROOT = os.path.dirname(os.path.abspath(__file__))
NODE_ENVIRONMENT_DIRECTORY = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'env')
NODE_ENV = os.path.join(NODE_ENVIRONMENT_DIRECTORY, 'bin', 'node')
NPM_ENV = os.path.join(NODE_ENVIRONMENT_DIRECTORY, 'bin', 'npm')
NPM_PACKAGES = os.path.join(os.path.join(ROOT))
NODE_ACTIVATE_PATH = os.path.join(NODE_ENVIRONMENT_DIRECTORY, 'bin', 'activate')

REACTIPY_JS = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                          'reactipy.js')
PACKAGE_DEPENDENCIES = 'PACKAGE_DEPENDENCIES'
SERVER_PROTOCOL = '0.0.0.0'
SERVER_ADDRESS = '0.0.0.0'
SERVER_PORT = '8080'