Mongodb Scheme Design Tips
=========================

Concerns
----------

makes queries easy
makes queries fast
facilitates atomicity
facilitates sharding

http://www.slideshare.net/mongosf/schema-design-with-mongodb-dwight-merriman

http://cookbook.mongodb.org/patterns/count_tags/

图解map-reduce
http://www.slideshare.net/gabriele.lana/couchdb-vs-mongodb-2982288

Tips(from <<50 Tips & Tricks for mongodb developers>>)
-------------------------------------------------------------

my opinion: mongo just as a data store

Create hierarchical documents for faster scans

Do not embed fields that have unbound growth

Pre-populate anything you can

Design documents to be self-sufficient

Minimize disk access

Duplicate data for speed, reference data for integrity: embedded (denormalized) or referenced(normalized)

Use indexes to do more with less memory/Don’t always use an index/Create indexes that cover your queries

AND-queries should match as little as possible as fast as possible

OR-queries should match as much as possible as soon as possible



