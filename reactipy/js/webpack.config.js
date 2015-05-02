var path = require('path');
var webpack = require('webpack');

var webpackConfig = function (pathToSource, tmpFile) {
    return {
        entry: pathToSource,
        output: {
            path: path.dirname(tmpFile),
            filename: path.basename(tmpFile),
            library: "./",
            libraryTarget: "umd"
        },
        module: {
            loaders: [
                {
                    test: /\.jsx?$/,
                    exclude: /node_modules/,
                    loader: 'babel-loader'
                }
            ]

        }
    };
};

module.exports = webpackConfig;