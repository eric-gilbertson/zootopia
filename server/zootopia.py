import web
import json
import urllib
import os
from collections import deque
import datetime

playlist = deque([], maxlen=25)

render = web.template.render('templates/')

urls = (
    '/', 'index',
    '/logsong', 'logsong',
    '/songs', 'songs',
    '/images/(.*)', 'images' #this is where the image folder is located....
)

class Song(object):
    def __init__(self, artist, title):
        self.artist = artist
        self.title = title
        self.date = datetime.datetime.now()

    def toDict(self):
        ret_val = {'date':self.date.strftime("%H:%M:%S"), 'artist':self.artist, 'title':self.title}
        return ret_val

class index:
    def GET(self):
        return render.index(playlist)

class images:
    def GET(self, name):
        ext = name.split(".")[-1]

        cType = {
            "png": "images/png",
            "jpg": "images/jpeg",
            "gif": "images/gif",
            "ico": "images/x-icon"}

        file_path = None
        if name == 'current-song.jpg':
            file_path = './images/albumart/art-00.jpg'
        elif name in os.listdir('images'):  # Security
            file_path = 'images/{0}'.format(name)

        if file_path:
            web.header("Content-Type", cType[ext])  # Set the Header
            return open(file_path, "rb").read()  # Notice 'rb' for reading images
        else:
            raise web.notfound()

class songs:
    def GET(self):
        params = web.input()
        web.header('Content-Type', 'application/json')
        web.header('Access-Control-Allow-Origin', '*')
        songs = []
        for song in playlist:
            songs.append(song.toDict())

        return json.dumps(songs)

class logsong:
    def GET(self):
        params = web.input()
        print "log song: {}:{}".format(params.artist, params.title)
        song = Song(params.artist, params.title)
        playlist.appendleft(song)
        return 'success'


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
