#!/usr/bin/env python 
import ConfigParser
configLocation = "./pyQ.cfg"

from bottle import route,run,post,get,delete,static_file,request,response

messages = []

def readConfig():
        global _host
        global _port

        print "Reading Config File..."
        config = ConfigParser.RawConfigParser()
        config.read(configLocation)

        _host = str(config.get("pyQ","host"))
        _port = str(config.get("pyQ","port"))

@get('/')
def index():
    return '''
	<!DOCTYPE html>
	<html>
        <head>
                <meta charset="UTF-8">
                <title>pyQ</title>
        </head>
        <body >
                <h1>pyQ</h1>
        </body>
	</html>
	'''

@get('/message')
def getMessage():
	if len(messages) == 0:
		return "\n"
	else:
		return messages.pop() + "\n"	

@post('/message')
def postMessage():
	messages.append(request.query.message)
	return "Added\n"

if __name__ == "__main__":
	readConfig()
	run(host='localhost', port=8080, debug=True)
