import driver
import sys
import urllib2
import json
import threading
import time

d = driver.LEDMessageBoard()

clock_on = True

note = {
	1 : [1, 0, 0, 0, 0, 1, 1],
	2 : [1, 0, 0, 0, 0, 1, 1],
	3 : [1, 0, 1, 1, 0, 1, 1],
	4 : [1, 0, 1, 1, 0, 1, 1],
	5 : [1, 0, 1, 0, 0, 1, 1],
	6 : [0, 0, 1, 0, 0, 1, 1],
	7 : [0, 0, 1, 1, 1, 1, 1],
}

def clock():
	global clock_on

	proxy_config = {'http': 'http://proxy.bauer-uk.bauermedia.group:3128'}

	proxy = urllib2.ProxyHandler(proxy_config)
	opener = urllib2.build_opener(proxy)
	urllib2.install_opener(opener)

	i = 0
	
	
	while(True):
		try:
			if clock_on == True:
				format_string = "%H:%M"
				if i > 8:
					format_string = "%H %M"
				if i == 10:
					i = 0


				localtime = time.localtime()
				time_string = time.strftime(format_string, localtime)
				if time_string == '17:05':
					d.clear_screen()
					d.scroll_message('abcabc')
				else:
					d.write_string(time_string, 0)
					d.push_screen()

				time.sleep(0.2)
				i += 2
			else:
				time.sleep(1)

					
		except KeyboardInterrupt:
			sys.exit(1)

def lastfm():
	global clock_on
	api_counter = 0
	now_playing_mbid = None

	while(True):
		try:
			if api_counter % 150 == 0:
				api_url = "http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user=jackrabbitslim&api_key=5805551071db81a56b74eecbced7318c&format=json"
				lastfm = urllib2.urlopen( api_url )
				resp = lastfm.read()
				lastfm.close()

				try:
					tracks = json.loads(resp)

					now_playing = tracks['recenttracks']['track'][0]

					song_changed = (now_playing_mbid != now_playing['mbid'])

					if song_changed:
						clock_on = False
						now_playing_mbid = now_playing['mbid']
						song = now_playing['artist']['#text'] + ' - ' + now_playing['name']
						song = song.lower()
						print song_changed
						print now_playing_mbid

						api_url = "http://ws.audioscrobbler.com/2.0/?method=track.getInfo&api_key=5805551071db81a56b74eecbced7318c&username=jackrabbitslim&format=json&mbid=" + now_playing_mbid
						lastfm = urllib2.urlopen( api_url )
						resp = lastfm.read()
						track_info = json.loads(resp)
						plays = track_info['track']['userplaycount']
						lastfm.close()

						song += ' [plays: ' + plays + ']'

						d.clear_screen()
						d.write_char(None, 0, f=note)
						d.write_char(None, 7, f=note)
						d.write_char(None, 14, f=note)
						d.push_screen()
						d.scroll_message(song, 28)
						clock_on = True
				except:
					clock_on = True
					pass
		
			time.sleep(0.2)
			api_counter += 2

		except KeyboardInterrupt:
			sys.exit(1)


print "Running clock code now..."
t_clock = threading.Thread(target=clock)
t_clock.daemon = True
t_clock.start()

t_lastfm = threading.Thread(target=lastfm)
t_lastfm.daemon = True
t_lastfm.start()

while True:
	try:
		time.sleep(1)
	except KeyboardInterrupt:
		sys.exit(1)

# from Pubnub import Pubnub

# pubnub = Pubnub.Pubnub(
# 	'',
#     "sub-eff4f180-d0c2-11e1-bee3-1b5222fb6268",  ## SUBSCRIBE_KEY
#     None,    ## SECRET_KEY
#     False    ## SSL_ON?
# )

# pubnub.set_proxy('http://proxy.bauer-uk.bauermedia.group', '3128')

# def receive(message):
# 	global clock_on

# 	print message
# 	if message['artist'] != '' and message['title'] != '':
# 		clock_on = False
# 		song = message['artist'] + ' - ' + message['title']
# 		print song
# 		song = song.lower()
# 		d.clear_screen()
# 		d.write_char(None, 0, f=note)
# 		d.write_char(None, 7, f=note)
# 		d.write_char(None, 14, f=note)
# 		d.push_screen()
# 		time.sleep(1)
# 		d.push_screen()
# 		time.sleep(1)
# 		d.scroll_message(song)
# 		clock_on = True
# 	return True


# print "Waiting for songs..."

# pubnub.subscribe({
#     'channel'  : 'np_99',
#     'callback' : receive 
# })
		
# d.scroll_message('abcdefghijklmnopqrstuvwxyz?!-. ')


	






