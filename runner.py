from bottle import *
import bottle
import os

application = default_app()

@error(500)
@error(505)
@error(404)
def errors(error):
	return error

@route("/")
def main():
	return template('index.html')

@route("/leaderboards")
def leaderboards():
	return template('leaderboards.html')

@route("/heroes")
def heroes():
	return template('heroes.html')

@route("/items")
def items():
	return template('items.html')

@route("/contact me")
def contact_me():
	return template('contact me.html')



@route('/favicon.ico')
def get_favicon():
	return server_static('dota.ico')


@route('/robots.txt')
def serve_robots():
    return static_file('robots.txt', root='./static/')

# specifying the path for the files
@route('/<filepath:path>')
def server_static(filepath):
	return static_file(filepath, root='./static/')

if __name__ == '__main__':
	application.run(reloader=True, host="0.0.0.0", port=int(os.environ.get("PORT", 9090)))
	