import paho.mqtt.client as mqttClient
import time
import random

x = 0

def on_connect(client, userdata, flags, rc):
 
    if rc == 0:
 
        print("Connected to broker")
 
        global Connected                 
        Connected = True                 
 
    else:
 
        print("Connection failed")
 
def on_message(client, userdata, message):
    print "Message received: "  + message.payload
 
Connected = False    
 
#broker_address = "test.mosquitto.org"
#broker_address = "iot.eclipse.org"

broker_address = "broker.hivemq.com" 
  
client = mqttClient.Client("html")               
 
client.on_connect= on_connect                      
client.on_message= on_message                      
client.connect(broker_address)                     
client.loop_start()                                
 
while Connected != True:                           
    time.sleep(1)
 
client.subscribe("RANDOM")
 
try:
    while True:
        x+=1
        client.publish("RANDOM", str('{:2.0f}'.format(random.uniform(0, 100)))) 
        time.sleep(1)
 
except KeyboardInterrupt:
    print "exiting"
    client.disconnect()
    client.loop_stop()


