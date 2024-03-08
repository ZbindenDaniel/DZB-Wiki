# webServer.py
from machine import Pin, Timer

import network
try:
 import usocket as socket        #importing socket
except:
 import socket
from configuration import Config
#import measurement
import utime
import ujson
from logger import logger

class webserver:

    def __init__(self):
        # Create a configuration instance
        self.config = Config()
        self.log = logger("webserver", 2, True)
        ssid = self.config.getValue("webServer.AP.essid")
        password = self.config.getValue("webServer.AP.password")
        self.ap = network.WLAN(network.AP_IF)
        self.ap.config(essid=ssid, password=password)

    def __handle_request__(self, request): # request is a json string
        try:
            #status = 200
            if 'POST' in request:
                print("POST")
                # Update the configuration with the form data
                #form_data = ujson.loads(request.read())
                #for key, value in form_data.items():
                #    self.config_instance.set_value(key, value)

                response = "Configuration saved successfully."
            elif 'GET' in request:
                print("GET")
                if '/current_measurement' in request:
                    # Read and respond with direct measurements
                    #current_data = measurement.read_sensor()
                    response = "Current Measurement"#: {}".format(current_data.decode())
                elif '/download_measurements' in request:
                    # Serve the saved measurements as a downloadable file
                    #with open("measurements.csv", "r") as measurement_file:
                    #    measurements = measurement_file.read()
                    #request.send(200, measurements, headers={"Content-Disposition": "attachment; filename=measurements.csv"})
                    response = "download_measurements"
                else:
                    # Generate an HTML form based on the configuration data
                    response = self.config.getHTMLFormForConfig()
            else:
                response = "Invalid request method."
        except Exception as e:
            # Log the exception to a file with a timestamp
            #timestamp = utime.localtime()
            #timestamp_str = "{:04d}-{:02d}-{:02d}_{:02d}:{:02d}:{:02d}".format(
            #    timestamp[0], timestamp[1], timestamp[2],
            #    timestamp[3], timestamp[4], timestamp[5]
            #)
            #with open("{}.log".format(timestamp_str), "w") as log_file:
            #    log_file.write("Exception: {}\n".format(str(e)))
            response = "Error: {}".format(str(e))
        print(response)
        #request.send(status, response)

    def start(self):
        self.ap.active(True)            #activating
        while self.ap.active() == False:
          pass
        #print('Connection is successful')
        self.log.debug(self.ap.ifconfig())

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #creating socket object
        s.bind(('', 80))
        s.listen(5)
        while True:
            conn, addr = s.accept()
            print('Got a connection from %s' % str(addr))
            request = conn.recv(1024)
            self.__handle_request__(request)
            #print('Content = %s' % str(request))
            ## TODO: handle request
            conn.send(self.config.getHTMLFormForConfig())
            conn.close()
        self.log.debug('server started')

    def stop(self):
        print('server stoped')
        #self.server = null

    def runServerFor(self, minutes):
        self.start()
        utime.sleep(minutes)
        self.stop()
        #timer.init(freq=60*minutes, mode=Timer.ONE_SHOT, callback=self.stop)