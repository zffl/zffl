Client driver
======================

Communicate with Server Demo
---------------------------------

Document to insert:
::

  {"test": "insert"}

Pack message:

::

  def __pack_message(operation, data):
      return (request_id, message + data)

Transform to bson & Build message:

::

  def _msg_build_insert(collection_name, docs, check_keys=True):
      return (request_id, insert_message, max_bson_size)

Send message to server:

::

  '''
  '4\x00\x00\x00\xcbl\xb42\x00\x00\x00\x00\xd2\x07\x00\x00\x00\x00\x00\x00test.test\x00\x16\x00\x00\x00\x02test\x00\x07\x00\x00\x00insert\x00\x00'
  '''
  def _send_message(message):
      sock.sendall(data)

Mongo Wire Protocol
----------------------

Message Header:

::

  struct MsgHeader {
      int32   messageLength; // total message size, including this
      int32   requestID;     // identifier for this message
      int32   responseTo;    // requestID from the original request
                             //   (used in reponses from db)
      int32   opCode;        // request type - see table below
  }
  //for insert message, the opCode is 2002.

OP_INSERT Message

::

  struct {
      MsgHeader header;             // standard message header
      int32     flags;              // bit vector - see below
      cstring   fullCollectionName; // "dbname.collectionname"
      document* documents;          // one or more documents to insert into the collection
  }




Pymongo Programming Model
-----------------------------

Connection.Collection.Cursor: a typical mongo client driver model

::

  db.test.insert/remove/update/drop/rename/*_index/find_*
  Cursor where/limit/skip/sort


Mongoengine Programming Model
----------------------------------

ORM like

::

  import web, datetime
  from mongoengine import *

  connect('findwq')

  class Tag(Document):
      Name = StringField()
      Children = ListField(ReferenceField('Tag'))
      
  class Topic(Document):
      Title = StringField()
      Description = StringField()
      Version = IntField(default=1)
      CreateDate = DateTimeField(default=datetime.datetime.now())
      Answers = ListField(ReferenceField('Answer'))
      
  class Answer(Document):
      Content = StringField()
      CreateDate = DateTimeField(default=datetime.datetime.now())
      
  def init():
      tag = Tag(Name='Computer Language')
      tag.save()
      
      tagC = Tag(Name='C',Children=[tag])
      tagC.save()
      
      
  if __name__ == '__main__':
      init()


