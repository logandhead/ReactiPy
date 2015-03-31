var fs = require('fs'),
    argv = require('yargs').argv,
    React = require('react'),
    pathToSource = argv.pathToSource,
    DOM = React.DOM, body = DOM.body, div = DOM.div, script = DOM.script;

if (!pathToSource) {
    throw new Error('No path to the a source file provided, ex: `--path-to-source /path/to/some/file.js`');
}

if (!fs.existsSync(pathToSource)) {
    throw new Error('Cannot find source file "' + pathToSource + '"')
}

if (argv.reactProps) {
    argv.reactProps = JSON.parse(argv.reactProps);
}

var Component = React.createFactory(require(pathToSource)),
    props = argv.reactProps || {},
    containerId = argv.componentContainer,
    propsReference = argv.propsReference || 'APP_PROPS',
    renderedHtml;

if (argv.staticMarkup) {
    var componentHtml = {
        dangerouslySetInnerHTML: {
            __html: React.renderToString(Component(props))
        }
    };

    if (containerId) {
        componentHtml['id'] = containerId
    }
    renderedHtml = React.renderToStaticMarkup(div(null,
        div(componentHtml),
        script({
            dangerouslySetInnerHTML: {
                __html: 'var ' + propsReference + ' = ' + safeStringify(props) + '\n'

            }
        })
    ));
}
else {
    renderedHtml = React.renderToString(Component(props));
}

function safeStringify(obj) {
    return JSON.stringify(obj).replace(/<\/script/g, '<\\/script').replace(/<!--/g, '<\\!--')
}

console.log(renderedHtml);

