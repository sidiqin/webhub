from bottle import *
import bottle
import os


# db = MongoClient("mongodb://db_username:db_pwd@db_ip:db_port").db_name

application = default_app()

@error(500)
@error(505)
@error(404)
def errors(error):
	return error

@route("/")
def main():
	return template('index.html')

@route("/Leaderboards")
def Leaderboards():
	return template('Leaderboards.html')

@route("/Statistics")
def Statistics():
	return template('Statistics.html')


@route("/Heroes")
def Heroes():
	return template('Heroes.html')


@route("/Guides")
def Guides():
	return template('Guides.html')


@route("/About")
def About():
	return template('About.html')


@route('/favicon.ico')
def get_favicon():
	return server_static('favicon.ico')


@route('/robots.txt')
def serve_robots():
    return static_file('robots.txt', root='./static/')

# specifying the path for the files
@route('/<filepath:path>')
@route('/Leaderboards/<filepath:path>')
@route('/Statistics/<filepath:path>')
@route('/Heroes/<filepath:path>')
@route('/Guides/<filepath:path>')
@route('/About/<filepath:path>')
def server_static(filepath):
	return static_file(filepath, root='./static/')

if __name__ == '__main__':
	application.run(host='0.0.0.0', port=8080, debug=True, reloader=True,)
	