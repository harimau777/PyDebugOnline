const express = require('express');
const server = new express;
const redis = require('redis');
const redisClient = redis.createClient();

//Redis database:
redisClient.on('connect', () => {
  console.log("Connected to Redis database.");
});

//Serve static content:
server.use(express.static(__dirname + '/../client');

//Routes:
app.post('/code', (req, res) => {
  const body = req.body;

  redisClient.set('code', body, (err, reply) => {
    if (err) {
      //Handle error
    }

    console.log('Stored code in Redis database.');
  });

  //Send code to debugger

  res.send('Code uploaded successfully');
});

app.get('/step', (req, res) => {
  const debugMsg = '___get message from debugger___';
  res.send(debugMsg);
});

//Start server:
server.listen(1337, () => console.log('Server listening on port 1337.');

