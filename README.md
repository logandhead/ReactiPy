# ReactiPy
Compile react components server side using Python 
```python
from reactipy.component import ReactComponent
import os


class HelloWorldComponent(ReactComponent):
    path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'components/helloworld.js')

component = HelloWorldComponent()

component.render(props=['Hello', 'World'])
```
Documentation
-------------

- [Installation](#installation)

Installation
------------

```bash
pip install reactipy
```
