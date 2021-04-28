var http = require('http');
 
http.createServer(function(req, res){
    console.log("Req came from " + req.client.remoteAddress + ":" + req.client.remotePort);
    console.log("Req served at " + req.client.localAddress + ":" + req.client.localPort);
    req.on('data', function(data){
        res.end(data);
    });
    if(req.method.toUpperCase() == 'GET'){
        res.end('hello from ' + req.client.remoteAddress + ":" + req.client.remotePort + '\n'
        + " to " + req.client.localAddress + ":" + req.client.localPort);
    }else {
    	res.end('NOT FOUND');
	}

}).listen(8893);