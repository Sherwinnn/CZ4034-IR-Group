const express = require('express')
const path = require('path')
const app = express()
const port = 3000
const solr = require('nolr');

const client = new solr({
    host: '127.0.0.1',
    port: '8983',
    core: 'restaurantCore',
    protocol: 'http'
});

app.use(express.urlencoded({ extended: true }));
app.use(express.static('public'));


app.get('/', function(req,res){
    res.sendFile(path.join(__dirname+'/public/index.html'));
})

app.get('/search', (req, res) => {
    const query = req.query.q;
    console.log(req.query.q);
    let objQuery = client.query()
    .q({text: query })
    .addParams({
        wt:'json',
        indent: true,
        rows:10
    });
    
    client.search(objQuery, function (err, result) {
        if (err) {
            console.log(err);
            return;
        }
        console.log('Response: ', result.response);
        res.json(result.response.docs);
    })
    
    
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})