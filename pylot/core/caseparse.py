from string import Template
from engine import Request
import random
from string import Template

def load_cases():
    cases = []
    
    #case 1
    def postdata1():
        return ''
    def url1():
        return 'http://localhost'
    req = Request(url1,'POST',postdata1)
    req.verify = 'asdf'
    cases.append(req)

    return cases
