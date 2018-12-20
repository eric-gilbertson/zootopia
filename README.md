
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

1) Configuring RadioLogik to publish to web app
Radiologik must be configured to push each song to the web app. This is done
as follows:

    * open Preferences dialog
    * enter 'http://127.0.0.1:8080/logsong?artist=<a>&title=<t>' into the GET URL 1' field
    * Click OK

Once configured RadiologiK will publish each song it plays via and HTTP GET 
command to the web server.


Required Python libraries:
    * web.py 0.38
`


