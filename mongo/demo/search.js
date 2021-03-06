t = db.test;
t.drop();

var content = 'abcdefghijklmnopqrstuvwxyz';
function gernerateContent(value){
  var count = Math.random()*100>>0;
  var half = count/2>>0;
  var result = '';
  for(var i = 0; i< count; i++){
    if(i == half){
      result += value;
    }
    result += content;
  }
  return result;
}

t.insert({ title: "mongodb from beginner to advanced for a python programmer", content: gernerateContent('beginer guide..'), tags: [ 'mongodb', 'nosql', 'python' ], publishDate: new Date("01/01/2007"),viewCount: 100,author:{name:"ryan fang",email:'zffl@yahoo.cn'}});
t.insert({ title: "How to build a website by webpy&mongodb?", content: gernerateContent('website'), tags: [ 'python', 'webpy', 'mongodb' ], publishDate: new Date("12/12/2009"),viewCount: 300, author:{name:"ryan fang",email:'zffl@yahoo.cn'}});
t.insert({ title: "How to implement a event based high performance web framework?", content: gernerateContent('blal bla'), tags: [ 'gevent', 'tornado', 'libev' ] ,publishDate: new Date("09/09/2011"),viewCount: 10000, author:{name:"ryan fang",email:'zffl@yahoo.cn'}});
t.insert({ title: "pypy, a fast python vm with jit support.", content: gernerateContent('blal bla'),tags: [ 'vm','python' ], likes: 1001, publishDate: new Date("10/09/2011"),viewCount: 10000, author:{name:"some one else",email:'abc@gmail.com'}}); // site update, add likes function, stolen from facebook

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

