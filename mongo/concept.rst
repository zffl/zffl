Basic concept
======================

Comparision between Relational database & Mongodb
--------------------------------------------------------

============  ============
relation db    Mongo 
============  ============
Database       Database
Table          Collection
Row|Record     Document
DataReader     Cursor
Sp             Js Func
Aggregation    Mapreduce
Join           Embed&link
============  ============

Collection Cool Features
----------------------------

schme-free:
::

  db.test.insert({"greeting" : "Hello, world!"})
  db.test.insert({"foo" : 5})

subcollection:
::

  db.blog
  db.blog.comment
  db.blog.author

data types:
::

  Array {"things" : ["pie", 3.14]}
  Embedded Document {"name" : "John Doe","address" : {"street" : "123 Park Street","city" : "Anytown","state" : "NY"}
  DBRef stu = { name : 'Joe', classes : [ new DBRef('courses', x._id) ] }
  .. _Python: http://www.mongodb.org/display/DOCS/Database+References

capped colletion:
::

  like round-robin database tool
  auto-FIFO age-out feature
  db.createCollection("mycoll", {capped:true, size:100000})

Storing functions server-side(demo/storefunction.js)
---------------------------------

::

  db.system.js.insert( { _id : "deletebyname" , value : function( value ){ return db.test.remove({name:value}) } } );
  //db.eval("deletebyname('zffl')");

http://www.mongodb.org/display/DOCS/Server-side+Code+Execution

Map Reduce
------------

