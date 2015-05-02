var fs = require('fs');
var argv = require('yargs').argv;
var path = require('path');
var webpack = require('webpack');
var crypto = require('crypto');
var React = require('react');
var _ = require('lodash');
var Promise = require('promise');
var pathToSource = argv.pathToSource;
var Component = require('./component');
var webpackConfig = require('./webpack.config');


if (!pathToSource) {
    handleError('No path to the a source file provided, example: `--path-to-source /path/to/some/file.js`');
}

if (!fs.existsSync(pathToSource)) {

    handleError('Cannot find source file "' + pathToSource + '"')
}

if (argv.reactProps) {
    argv.reactProps = JSON.parse(argv.reactProps);
}


function createHash(value) {
    return crypto.createHash('md5').update(value).digest('hex')
}

function getFileStats(fpath) {
    return new Promise(function (fullfill, reject) {
        fs.stat(fpath, function (e, s) {
            if (e) {
                reject(e);
            }
            fullfill(s);
        });
    });
}

function existFile(filePath) {
    return new Promise(function (fullfill, reject) {
        fs.exists(filePath, function (exists) {
            fullfill(exists)
        });
    })
}

function generateModHashName(fp, date) {
    return path.dirname(fp) + '/' + path.basename(fp) + '_mod_' + createHash(date.toString())
}

function handleError(err) {
    console.error(err);
    throw new Error(err);
}

function renderComponent(config) {
    try {
        var comp = new Component(require('/.' + packFilePath), argv);
        comp.renderHtml().then(function (html) {


            process.stdout.write(html);
            getFileStats(pathToSource).then(function (s) {
                var filePath = generateModHashName(compFilePath, s.mtime);
                fs.writeFile(filePath, html);
            });

        }, handleError);
    }
    catch(exc){
        handleError(exc);
    }
}

function packComponent(config) {
    return new Promise(function (fulfill, reject) {
        webpack(config).run(function (a, s) {
            if (a)
                reject(a);
            else {
                fulfill(config, s)
            }
        });
    });
}

var folder = '/tmp/';
var compFileKey = crypto.createHash('md5').update(argv.toString()).digest('hex');
var compFilePath = folder + 'cp-' + compFileKey;
var packFilePath = folder + 'pf-' + crypto.createHash('md5').update(pathToSource).digest('hex');

var fname = _.find(fs.readdirSync(path.dirname(compFilePath)), function (item) {
    return _.contains(item, compFileKey);
});


function init() {
    if (fname) {

        var modHash = fname.split('_mod_')[1];
        getFileStats(pathToSource).then(function (s) {

            return modHash == createHash(s.mtime.toString()) ? false : true
        }).then(function (changed) {
            if (changed) {

                var packFilePath = folder + 'pf-' + crypto.createHash('md5').update(pathToSource).digest('hex');
                packComponent(webpackConfig(pathToSource, packFilePath))
                    .then(renderComponent, handleError)
            }
            else {
                process.stdout.write(fs.readFileSync(path.dirname(compFilePath) + '/' + fname, "utf-8"));
            }
        })
    }
    else {
        var config = webpackConfig(pathToSource, packFilePath);

        existFile(packFilePath).then(function (exists) {

            if (exists) {
                renderComponent(config)
            }
            else {

                packComponent(config).then(function () {
                    renderComponent(config);
                }, handleError)
            }
        });
    }

}

init();





