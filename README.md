# ReactiPy

### Deprecated --- I currently do not have the time to maintain this project. Please message me if you would like to take over this project*
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
- [ReactComponent](#reactcomponent)


Installation
------------

```bash
pip install reactipy

```

ReactComponent
--------------


###  Define Component

Define a react component that includes a path pointing to the path of the React Component. JSX is not supported so make sure to compile your jsx templates to js.

```python
from reactipy.component import ReactComponent


class HelloWorldComponent(ReactComponent):
    path = 'path/to/component.js'

```

*** You must specify a path when defining a React Component ***


###  Create Instance
Create an instance of the component and optionally specifiy a container which will output an id on the component and props_name which will be a global variable that has all the props specified in json


```python

component = HelloWorldComponent(container='helloworld', props_name='HELLO_PROPS')

```
Arguments:

- `container`: [optional] the id of the container.
- `props_name`:[optional] the props variable name.


### Render Component

Render a component to html on the initial request for faster page loads
and to allow search engines to crawl your pages for SEO purposes.

```python

component.render(info=['hello', 'world])

```
Arguments:

- `kwargs`: [optional] the props 


