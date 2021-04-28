const http = require('http');

const options = {
    hostname:'172.18.0.3',
    port:8893,
    path:'/',
    method:'GET',
}

http.createServer(function(req, res){
    console.log("Req came from " + req.client.remoteAddress + ":" + req.client.remotePort);
    console.log("Req served at " + req.client.localAddress + ":" + req.client.localPort);
    req.on('data', function(data){
        res.end('post');
    });
    if(req.method.toUpperCase() == 'GET'){
        const req_send = http.request(options, function(res_send){
            // console.log('STATUS: ' + res.statusCode); 
            // console.log('HEADERS: ' + JSON.stringify(res.headers)); 
            res_send.on('data', function(d){
                
                res.end('hello from ' + req.client.remoteAddress + ":" + req.client.remotePort + '\n'
                + " to " + req.client.localAddress + ":" + req.client.localPort + "\n" + d);
            });
        });

        req_send.on('error', e=>{
            console.log('problem with request: ' + e.message);
        });
        
        req_send.end();
        
    }else {
    	res.end('NOT FOUND');
    }
    
}).listen(8894);