'use strict';

const express = require('express');

// Constants
const PORT = 8080;
const HOST = '0.0.0.0';

// App
const app = express();
app.get('/', (req, res) => {
  res.send('alibaba-Hello World!!!\n');
});

app.get('/maman', (req, res) => {
  res.send('or_maman\n');
});

app.listen(PORT, HOST);
console.log(`Running on http://${HOST}:${PORT}`);
