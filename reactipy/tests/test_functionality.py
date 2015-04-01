import unittest
import os

from reactipy.component import ReactComponent
from reactipy.node_env import NodeEnv


class HelloWorldComponent(ReactComponent):
    path = os.path.join(os.path.abspath(''),
                        'reactipy/tests/components/helloworld.js')


class TestReactiPyFunctionality(unittest.TestCase):

    def test_node_env(self):
        self.assertEqual(NodeEnv().node_exist(), True, 'node does not exist')


    def test_render(self):
        component = HelloWorldComponent()
        rendered = component.render(name='world')
        self.assertEqual(len(str(rendered)) > 0, True,
                         'did not render component')

    def test_render_to_string(self):
        component = HelloWorldComponent()
        rendered = component.render_to_string(name='world')
        self.assertEqual(len(str(rendered)) > 0, True,
                         'did not render component')




