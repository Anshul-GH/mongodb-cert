import bottle


@bottle.route('/')
def home_page():
    mythings = ['apples', 'oranges', 'bananas', 'peaches']
    return bottle.template('hello_world', username='Anshul', things=mythings)


bottle.debug(True)
bottle.run(host='localhost', port=8080)