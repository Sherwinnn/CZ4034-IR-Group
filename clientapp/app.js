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


const solr_url = 'http://localhost:8983/solr';
const collection_name = 'restaurantCore'  


app.get('/', function(req,res){
    res.sendFile(path.join(__dirname+'/public/index.html'));
})


app.get('/search', (req, res) => {
	// console.log(req.query);
    const {q, category,
        neighbourhood, distance,
		name, sortBy, sortOrder} = req.query;
	
	let qObj = {}
	if (q.trim() !== "") {
		qObj.text = q
	} 
	if (category !== 'NONE') {
		qObj["categoryName"] = category
	}
	if (neighbourhood !== 'NONE') {
		qObj["neighborhood"] = neighbourhood
	}
	if (name.trim() !== '') {
		qObj["restaurant"] = name
	}
	
	console.log(qObj)
	
    let objQuery = client.query()
	.addParams({
        'indent': true,
    })
	.start(0)
	.rows(10677);

	if(Object.keys(qObj).length === 0) {
		objQuery.q("*:*");
	}else{
		objQuery.q(qObj);
	}	

	if (sortBy !== 'NONE') {
		sortObj = {};
		sortObj[`${sortBy}`] = sortOrder;
		objQuery.sort(sortObj);		
	}
	
	objQuery.params.push('debug=timing')

	if (distance !== 'NONE') {
		fq=encodeURIComponent("{!geofilt sfield=LatLong}");
		pt=encodeURIComponent("1.34,103.68");
		d=encodeURIComponent(distance);
		objQuery.params.push(`fq=${fq}`,`pt=${pt}`,`d=${d}`);
	}

	console.log(objQuery.params)
	

    client.search(objQuery, function (err, result) {
        if (err) {
            console.log(err);
            return;
        }
        console.log('Response: ', result);
        res.json(result);
    })
    
    
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})