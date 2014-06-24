#!/usr/bin/env python 
from bottle import route,run,post,get,delete,static_file,request,response

messages = []

@get('/')
def index():
    return '''
	<!DOCTYPE html>
	<html>
        <head>
                <meta charset="UTF-8">
                <title>pyQ</title>
                <style>
                        div
                        {
                        	margin: 0 auto;
                        	width: 1280px;
                        }
                </style>
        </head>
        <body >
                <div><h1>pyQ</h1></div>
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
	run(host='localhost', port=8080, debug=True)
