
                           README - Zootopia Playlist 

0) Introduction
Zootopia is a RadioLogik based automation system that supplies the on air
program feed when there is no human DJ and on the KZSU-3 streaming channel.
Zootopia Playlist is a Python/web.py based application that displays the
most recently played Zootopia tracks. Its input is provided by the RadioLogik
DJ app using its publish feature to send the track info to the app server
via HTTP GET requests. The app stores the most recent N tracks in memory 
(no presistance yet) and uses it to build a web page that displays them
to users.


