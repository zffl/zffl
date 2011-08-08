t = db.test;
t.drop();

t.insert({name:'zffl'});
t.insert({name:'asdf'});
t.insert({name:'jklm'});
t.insert({name:'qwrqewr'});

db.system.js.insert( { _id : "deletebyname" , value : function( value ){ return db.test.remove({name:value}) } } );
//db.eval("deletebyname('zffl')");
//db.test.find();
