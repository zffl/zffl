Query language
======================

------------
Find query
------------

mongo query language
-----------------------

::

  $query - the evaluation or "where" expression
  $orderby - sort order desired
  $hint - hint to query optimizer
  $explain - if true, return explain plan results instead of query results
  $snapshot - if true, "snapshot mode"

query document
-----------------

::

  query condition: $lt, $lte, $gt, $gte, $ne
  or query: single key($in, $nin), multi key($or), $not
  
  

grammmer in pymongo
----------

::

  find([spec=None[, fields=None[, skip=0[, limit=0[, timeout=True[, snapshot=False[, tailable=False[, sort=None[, max_scan=None[, as_class=None[, slave_okay=False[, **kwargs]]]]]]]]]]]])

example(demo/search.js)
---------

::

  //query conditions
  t.find({},{content:0}); // exclude boring content
  t.find({},{_id:0,title:1,tags:1});
  t.find({"viewCount":{"$gte" : 200, "$lte" : 400}},{content:0});
  t.find({"tags":{$in:['python','mongodb']}},{content:0});
  t.find({"tags":{$nin:['python']}},{content:0}); // python go to the devil
  t.find({"tags":{$all:['python','mongodb']}},{content:0});
  t.find({"$or":[{"tags":{$in:['python','mongodb']}},{"viewCount":{"$gte" : 10000}}]},{content:0}) // my interest or popular
  t.find({"likes":null},{content:0}) //scheme changed
  t.find({"title":/^how\sto/gi},{content:0}) // i just want to find how to do something.
  t.find({"author.name":"ryan fang"},{content:0})
  t.find({"$where":function(){if(this.viewCount/this.likes < 100){return true;}}},{content:0}) // simple query does not work, but slow.

  //query cursors
  t.find().limit(2).skip(2).sort({viewCount:1,publishDate:-1})

  //update

  blog = t.findOne({"title":'How to build a website by webpy&mongodb?'})
  blog.viewCount = blog.viewCount + 1;
  //delete blog.author;
  t.update({"title":'How to build a website by webpy&mongodb?'},blog)

  t.update({"title":'How to build a website by webpy&mongodb?'}, {"$inc" : {"viewCount" : 1}})
  t.update({"title":'How to build a website by webpy&mongodb?'}, {"$set" : {"title" : "How to build a website by webpy & mongodb?" }})




