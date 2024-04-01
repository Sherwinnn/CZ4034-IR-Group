The following instruction set is meant for Solr v8.11.3 on a Windows machine


cd solr-8.11.3

### Start Solr in standalone mode
bin\solr start -p 8983

### Create a Core
bin\solr create_core -c restaurantCore -d server/solr/configsets/restaurant_configs -p 8983 -V

### Post documents to Core
java -Dc=restaurantCore -jar example\exampledocs\post.jar data\docs_to_post.xml

Explore using http://localhost:8983/solr/#/