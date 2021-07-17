#!/usr/bin/env python3

# Example of using the MQTT client class to publish feed values.

# Import standard python modules.
import random
import sys
import time

import paho.mqtt.client as mqtt

# Set to your Adafruit IO key.
# Remember, your key is a secret,
# so make sure not to publish it when you publish this code!
ADAFRUIT_IO_KEY = '.............'

# Set to your Adafruit IO username.
# (go to https://accounts.adafruit.com to find your username)
ADAFRUIT_IO_USERNAME = '....'

# Set to the ID of the feed to subscribe to for updates.
FEED_ID = 'test-feed-guage'


# Define callback functions which will be called when certain events happen.
def connected(client, userdata, flags_dict, result):
    # Connected function will be called when the client is connected to Adafruit IO.
    # This is a good place to subscribe to feed changes.  The client parameter
    # passed to this function is the Adafruit IO MQTT client so you can make
    # calls against it easily.
    print('Connected to Adafruit IO!')


def disconnected(client, userdata, rc):
    # Disconnected function will be called when the client disconnects.
    print('Disconnected from Adafruit IO!')
    sys.exit(1)


# Create an MQTT client instance.
client = mqtt.Client()
# Enable TLS and use port 8883
# Disable TLS and use port 1883
client.tls_set_context()
# Enter Adafruit IO credentials
client.username_pw_set(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

# Setup the callback functions defined above.
client.on_connect    = connected
client.on_disconnect = disconnected

# Connect to the Adafruit IO server.
client.connect('io.adafruit.com', 8883, 60)

# Now the program needs to use a client loop function to ensure messages are
# sent and received.  There are a few options for driving the message loop,
# depending on what your program needs to do.

# The first option is to run a thread in the background so you can continue
# doing things in your program.
client.loop_start()
# Now send new values every 10 seconds.
print('Publishing a new message every 10 seconds (press Ctrl-C to quit)...')
while True:
    value = random.randint(0, 100)
    print('Publishing {0} to DemoFeed.'.format(value))
    client.publish('{0}/feeds/{1}'.format(ADAFRUIT_IO_USERNAME, FEED_ID), value)
    time.sleep(10)
