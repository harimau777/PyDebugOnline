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

      res.send('Trace successful');
    });
});

server.post('/code/file', upload.single('file'), (req, res) => {
  var path = './' + req.file.path.match(/\/temp\/.+/)[0];
  trace.getTrace(path, 'file')
    .then((data) => {
      traceData = data;
      lineNumber = 0;

      res.send('Trace successful');
    });
});

server.get('/step', (req, res) => {
  res.send(JSON.stringify(traceData[lineNumber]));
  lineNumber++;
});

//Start server:
server.listen(1337, () => console.log('Server listening on port 1337.'));
