//////////////////////////
// NodeJS Socket Server
//////////////////////////
// Require the network module
var net = require('net');
var renderer = require('./renderer');
var server = net.createServer(function(socket) {
    // The socket has been opened
    // Events

    socket.setEncoding("utf8");
    socket.on('connect', function(a) {
        // This Code will be run when a new connection is opened
    });
    socket.on('data', function(data) {
        // Code here will be run when some d
        // ata arrives
        renderer(JSON.parse(data)).then(function(resp) {
            socket.write(resp);
        })
    });
    socket.on('end', function() {
        // Code here will be run when the socket closes
    });
});

// Start the server listening
server.listen(5432, function() {
    console.log('Server listening on port: ' + 5432);
});