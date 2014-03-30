import urllib2
import json
import RPi.GPIO as GPIO
import time
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)


def GetWeather(state, city):
    GPIO.output(7,True)
    f = urllib2.urlopen('http://api.wunderground.com/api/9b80ce40807665f1/geolookup/conditions/q/' + state + '/' + city + '.json')
    json_string = f.read()
    parsed_json = json.loads(json_string)
    location = parsed_json['location']['city']
    temp_f = parsed_json['current_observation']['temp_f']
    print "Current temperature in %s is: %s" % (location, temp_f)
    f.close()
    GPIO.output(7,False)
    Semaphor(float(temp_f))


def Semaphor(temp_f):
    if (temp_f > 55.0):
        for i in range (0,99):
            GPIO.output(4,True)
            time.sleep(0.3)
            GPIO.output(4,False)
            time.sleep(0.3)

    elif (temp_f <= 55.0 or temp_f >= 30.0):
         for i in range (0,99):
            GPIO.output(17,True)
            time.sleep(0.3)
            GPIO.output(17,False)
            time.sleep(0.3)

    elif (temp_f < 30.0):
         for i in range (0,99):
            GPIO.output(27,True)
            time.sleep(0.3)
            GPIO.output(27,False)
            time.sleep(0.3)
    GPIO.cleanup()

GetWeather(str('MA'),str('quincy'))
