const express = require('express');
const server = new express;
const compression = require('compression');
const bodyParser = require('body-parser');
const multer = require('multer');
const upload = multer({dest: 'python/temp/'});
const trace = require('./traceCode.js');
const fs = require('fs');

let traceData; //Holds the result of a trace
let lineNumber = 0; //Holds our position as we step through the trace

//Use gzip compression
server.use(compression());

//Use body parser:
server.use(bodyParser.json());

//Serve static content:
server.use(express.static(__dirname + '/../client'));

//Routes:
server.post('/code/string', (req, res) => {
  trace.getTrace(req.body.code, 'string')
    .then((data) => {
      traceData = data;
      lineNumber = 0;

      res.status(200).send('Trace successful');
    })
    .catch(() => res.status(500).send('Error'));
});

server.post('/code/file', upload.single('file'), (req, res) => {
  var path = './' + req.file.path.match(/\/temp\/.+/)[0];
  trace.getTrace(path, 'file')
    .then((data) => {
      traceData = data;
      lineNumber = 0;

      fs.unlink(__dirname + '/../' + req.file.path, (err) => err ? console.log(err) : console.log('Temporary file deleted'));

      res.status(200).send('Trace successful');
    })
    .catch(() => res.status(500).send('Error'));
});

server.get('/step', (req, res) => {
  res.status(200).send(JSON.stringify(traceData[lineNumber]));
  lineNumber++;
});

server.use((req, res) => res.status(404).send('Route not found'))

//Start server:
server.listen(1337, () => console.log('Server listening on port 1337.'));
