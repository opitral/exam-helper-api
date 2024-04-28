const http = require('http');
const { exec } = require('child_process');

const server = http.createServer((req, res) => {
    var yourscript = exec('sh deploy.sh', (error, stdout, stderr) => {
        console.log(stdout);
        console.log(stderr);

        if (error !== null) {
            console.log(`exec error: ${error}`);
        }
    });
    res.end('success');
});

server.listen(5232, '0.0.0.0');
