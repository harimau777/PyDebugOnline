const child_process = require('child_process');

//NOTE: Implement a timeout that will kill the child process if it is taking too long
module.exports.getTrace = (code, type) => {
  //Construct the docker command:
  var dockerCmd = 'docker run --rm -v "$PWD/python":/shared -w /shared python:2 python traceCode.py' + 
    {
      'string' : ' -s "' + code + '"',
      'file' : ' -f ' + code
    }[type];

  return new Promise ((resolve, reject) => {
    child_process.exec(dockerCmd, (err, stdout, stdin) => {
      var lines = stdout.split('\n');
      lines.pop();

      var jsonLines = lines.map((line) => JSON.parse(line));

      resolve(jsonLines);
    });
  });
};
