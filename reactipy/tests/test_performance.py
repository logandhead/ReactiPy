import os
import time
import unittest
from reactipy.component import ReactComponent

def median(l):
    half = int(len(l) / 2)
    l.sort()
    if len(l) % 2 == 0:
        return (l[half-1] + l[half]) / 2.0
    else:
        return l[half]


class HelloWorldComponent(ReactComponent):
    path = os.path.join(os.path.abspath(''), 'reactipy/tests/components/helloworld.js')


class TestReactiPyPerformance(unittest.TestCase):
    def test_performance(self):
        print('running reactipy performance test')
        render_component_times = []
        render_watched_component_times = []
        rendered_components = []

        iteration_count = 25
        component = HelloWorldComponent(container='hi', props_reference='APP_VARS')

        for i in range(iteration_count):
            start = time.time()
            rendered_components.append(
                 component.render(name='world')
            )
            end = time.time()
            render_component_times.append(end - start)

        for i in range(iteration_count):
            start = time.time()
            rendered_components.append(
                 component.render_to_string(name='world')
            )
            end = time.time()
            render_watched_component_times.append(end - start)


        print('Total time taken to render a component {iteration_count} times: {value}'.format(
            iteration_count=iteration_count,
            value=sum(render_component_times)
        ))
        print('Times: {value}'.format(value=render_component_times))
        print('Max: {value}'.format(value=max(render_component_times)))
        print('Min: {value}'.format(value=min(render_component_times)))
        print('Mean: {value}'.format(value=sum(render_component_times) / len(render_component_times)))
        print('Median: {value}'.format(value=median(render_component_times)))

        print('\nTotal time taken to render a watched component {iteration_count} times: {value}'.format(
            iteration_count=iteration_count,
            value=sum(render_watched_component_times)
        ))
        print('Times: {value}'.format(value=render_watched_component_times))
        print('Max: {value}'.format(value=max(render_watched_component_times)))
        print('Min: {value}'.format(value=min(render_watched_component_times)))
        print('Mean: {value}'.format(value=sum(render_watched_component_times) / len(render_watched_component_times)))
        print('Median: {value}'.format(value=median(render_watched_component_times)))
