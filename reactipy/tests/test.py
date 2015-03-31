from reactipy.component import ReactComponent
import os


class HelloWorldComponent(ReactComponent):
    path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'components/helloworld.js')

component = HelloWorldComponent()

print component.render(props=['Hello', 'World'])
