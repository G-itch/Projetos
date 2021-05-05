/*const express = require('express')
const {spawn} = require('child_process');
const app = express()
const port = 3000
app.get('/',(req, res) => {

    var dataToSend;
    const python = spawn('python',['1.py']);
    python.stdout.on('data',function (data) {
            console.log('Pipe data from python script ...');
            dataTosend = data.toString();
        });
    python.on('close',(code) => {
    console.log(`child process close all stdio with code ${code}`);
    res.send(dataToSend)
    });
    
})
app.listen(port, () => console.log(`example ${port}!`))*/

const express = require('express')
const {spawn} = require('child_process');
const app = express()
const port = 3000
app.get('/', (req, res) => {
 
 var dataToSend;
 // spawn new child process to call the python script
 const python = spawn('python', ['1.py']);
 // collect data from script
 python.stdout.on('data', function (data) {
  console.log('Pipe data from python script ...');
  dataToSend = data.toString();
 });
 // in close event we are sure that stream from child process is closed
 python.on('close', (code) => {
 console.log(`child process close all stdio with code ${code}`);
 // send data to browser
 res.send(dataToSend)
 });
})
app.listen(port, () => console.log(`Example app listening on port 
${port}!`))
app.post('\Arduino Controller js\App.js',function (req,res){
    res.send("OI")
})