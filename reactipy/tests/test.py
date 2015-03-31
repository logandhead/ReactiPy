from reactipy.component import ReactComponent
import os

# Define your component
class MyComponent(ReactComponent):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        'components/helloworld.js')
    props = {'items': ['Home', 'Services', 'About', 'Contact us']}
    props_reference = 'test123'


component = MyComponent()
print component.render()




