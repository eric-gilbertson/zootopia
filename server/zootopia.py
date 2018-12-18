import web
import json
import urllib
import os
from collections import deque
import datetime

playlist = deque([], maxlen=4)

render = web.template.render('templates/')

urls = (
    '/', 'index',
    '/logsong', 'logsong',
    '/images/(.*)', 'images' #this is where the image folder is located....


)

class Song(object):
    def __init__(self, artist, title):
        self.artist = artist
        self.title = title
        self.date = datetime.datetime.now()


class index:
    def GET(self):
        return render.index(playlist)

class images:
    def GET(self, name):
        ext = name.split(".")[-1]  # Gather extension

        cType = {
            "png": "images/png",
            "jpg": "images/jpeg",
            "gif": "images/gif",
            "ico": "images/x-icon"}

        if name in os.listdir('images'):  # Security
            web.header("Content-Type", cType[ext])  # Set the Header
            return open('images/%s' % name, "rb").read()  # Notice 'rb' for reading images
        else:
            raise web.notfound()

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
