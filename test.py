import os

from reactipy.renderer import ReactiPy
if __name__ == '__main__':
    r = ReactiPy()
    p = os.path.join(os.path.abspath(os.curdir), 'reactipy', 'js', 'helloworld.jsx')
    print p
    nc = r.register_component(p, 'hi')
    items = [
        { 'name': 'Web Development', 'price': 300 },
        { 'name': 'Design', 'price': 400 }
    ]
    tt = nc.render(items=items)
    print tt
