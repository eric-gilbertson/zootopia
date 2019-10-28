
                           README - Zootopia Playlist 

0) Introduction
Zootopia is a RadioLogik based automation system that supplies the on air
program feed when there is no human DJ and on the KZSU-3 streaming channel.
Zootopia Playlist is a Python/web.py based application that displays the
most recently played Zootopia tracks. Its input is provided by the RadioLogik
DJ app using its publish feature to send the track info to the app server
via HTTP GET requests. The app stores the most recent N tracks in memory 
(no presistance yet) and uses it to build a web page that displays them
to users. The production version of this application can be found at 
http://kzsu.rocks. It is deployed on a Mac in the Neil Diamond center.

1) Configuring RadioLogik to publish to web app
Radiologik must be configured to push each song to the web app. This is done
as follows:

    * open Preferences dialog
    * enter 'http://127.0.0.1/logsong?artist=<a>&title=<t>' into the GET URL 1' field
    * Click OK

Once configured RadiologiK will publish each song it plays via and HTTP GET 
command to the web server.

In order for the web server to access the RL generated playlist artwork a
symbolic link must be made from ./images/albumart to the albumart directory
under the RL installation. Typically this is done as follows:

   * cd ./images
   * ln -s $HOME/Music/Radiologik/Web/albumart .


Required Python libraries:
    * web.py 0.38
`


