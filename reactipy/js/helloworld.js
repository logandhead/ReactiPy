var React = require('react');
var HelloWorld = React.createClass({displayName: 'HelloWorld',
    render: function() {
        return React.createElement("span", null, "asdf ", this.props.name);
    }
});


module.exports = HelloWorld;