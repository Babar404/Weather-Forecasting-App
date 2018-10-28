TIME_LAP= 3600 # In Seconds
ERROR_TIME_LAP = 10 # Seconds
RETRY=15
from scraper import site,handel
# Site For Scraping >> This Url Is For Karachi Temperaturee
#site="https://darksky.net/forecast/24.9294,67.1021/ca12/en"


# Importing Module
import time
import GUI
import sys
time.sleep(0.1)
# Creating Loop
while True:
	retry=0	 	# Retry Counting
	data=handel(site)	# Here Retriving Data Handler
	try:
		while True:
			k=data.start() # Connecting To Website
			if k:
				# Showing Our GUI
				GUI.GUI(k)
				time.sleep(TIME_LAP)
			else:
				print("RETRY")
				time.sleep(ERROR_TIME_LAP)
				retry=retry+1	# Counting Every Retry
				if retry==RETRY:	# Checking Retry Times
					print("Break")
					sys.exit(0)

	except Exception as e:
		print(e)
