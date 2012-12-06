import dcusb
import sys
import threading
import time

leds = driver.LEDMessageBoard()

clock_on = True

def clock():
	global clock_on

	i = 0
	while(True):
		try:
			format_string = "%H:%M"

			if i > 8:
				format_string = "%H %M"
			if i == 10:
				i = 0

			localtime = time.localtime()
			time_string = time.strftime(format_string, localtime)

			leds.write_string(time_string, 0)
			leds.push_screen()

			time.sleep(0.2)
			i += 2
					
		except KeyboardInterrupt:
			sys.exit(1)


print "Running clock code now..."
t_clock = threading.Thread(target=clock)
t_clock.daemon = True
t_clock.start()

while True:
	try:
		time.sleep(1)
	except KeyboardInterrupt:
		sys.exit(1)


	






