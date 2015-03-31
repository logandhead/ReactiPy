# ReactiPy
Compile React Components Server Side using Python 
```python
from reactipy.component import ReactComponent
import os

# Define your component
class MyComponent(ReactComponent):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        'components/helloworld.js')
    props = {'items': ['Home', 'Services', 'About', 'Contact us']}
    props_reference = 'test123'


component = MyComponent()
component.render() //renders html 
```
Documentation
-------------

- [Installation](#installation)

Installation
------------

```bash
pip install reactipy
```

