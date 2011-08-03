import bson
import random
import struct
import select
import socket

__ZERO = "\x00\x00\x00\x00"

MAX_INT32 = 2147483647
MIN_INT32 = -2147483648

def __pack_message(operation, data):
    """Takes message data and adds a message header based on the operation.
    Returns the resultant message string.
    """
    request_id = random.randint(MIN_INT32, MAX_INT32)
    message = struct.pack("<i", 16 + len(data))
    message += struct.pack("<i", request_id)
    message += __ZERO  # responseTo
    message += struct.pack("<i", operation)
    return (request_id, message + data)

def _msg_build_insert(collection_name, docs, check_keys=True):
    """Get an **insert** message.
    """
    max_bson_size = 0
    data = __ZERO
    if isinstance(docs, dict):
        docs = [docs]
    data += bson._make_c_string(collection_name)
    encoded = [bson.BSON.encode(doc, check_keys) for doc in docs]
    if not encoded:
        raise Exception("cannot do an empty bulk insert")
    max_bson_size = max(map(len, encoded))
    data += "".join(encoded)
    
    (request_id, insert_message) = __pack_message(2002, data)
    return (request_id, insert_message, max_bson_size)

def connect(host, port):
    s = socket.socket(socket.AF_INET)
    s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    s.settimeout(20.0)
    s.connect((host, port))
    s.settimeout(20.0)
    return s

def _send_message(message):
        sock = connect('localhost',27017)
        try:
            (request_id, data, max_doc_size) = message#not sure
            sock.sendall(data)
            #dismiss response,include err msg.
            return None
        except (Exception, socket.error), e:
            pass

def insert():
    __full_name = u"%s.%s" % ('test', 'test')
    msg = _msg_build_insert(__full_name,{"test": "insert"})
    _send_message(msg)
    
if __name__ == "__main__":
    insert()