var React = require('React');
var DOM = React.DOM, body = DOM.body, div = DOM.div, script = DOM.script;
var Promise = require('promise');

var Component = function (ref, argv) {
    this.component = React.createFactory(ref);
    this.props = argv.reactProps || {};
    this.propsReference = argv.propsReference || 'APP_PROPS';
    return this;
};
Component.prototype.renderHtml = function () {
    var self = this;

    return new Promise(function (fulfill, reject) {
        try {
            var componentHtml = {
                dangerouslySetInnerHTML: {
                    __html: React.renderToString(self.component(self.props))
                }
            };

            var renderedHtml = React.renderToStaticMarkup(div(null,
                div(componentHtml),
                script({
                    dangerouslySetInnerHTML: {
                        __html: 'var ' + self.propsReference + ' = ' + self.safeStringify(self.props) + '\n'

                    }
                })
            ));
            fulfill(renderedHtml);
        }
        catch (exception) {
            reject('Could not render component to html: ' + exception);
        }
    });
};

Component.prototype.safeStringify = function (obj) {
    return JSON.stringify(obj).replace(/<\/script/g, '<\\/script').replace(/<!--/g, '<\\!--')
};

module.exports = Component;
