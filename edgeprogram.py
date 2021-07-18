import paho.mqtt.client as mqtt
import time,logging
import Adafruit_DHT as d
from threading import Timer
broker="broker.hivemq.com"
count = 0;
port=1883;
QOS=0;
starttime = 0
q = [];
flag = True
CLEAN_SESSION=True
logging.basicConfig(level=logging.INFO) #error logging
#use DEBUG,INFO,WARNING

class BufferThread(Timer):
  def run(self):
    while not self.finished.wait(self.interval):
      self.function(*self.args, **self.kwargs)


def on_subscribe(client, userdata, mid, granted_qos):   #create function for callback
   #print("subscribed with qos",granted_qos, "\n")
   logging.info("sub acknowledge message id="+str(mid))

def on_disconnect(client, userdata,flags,rc=0):
    logging.info("DisConnected result code "+str(rc))


def on_connect(client, userdata, flags, rc):
    logging.info("Connected flags"+str(flags)+"result code "+str(rc))


def on_message(client, userdata, message):
    msg=str(message.payload.decode("utf-8"))
    myfunction()
    print("message received  "  +msg)

def on_publish(client, userdata, mid):
    logging.info("message published "  +str(mid))

#mqtt.Client.connected_flag=False #create flag
topic1 ="interview/IoT1"
client= mqtt.Client("IoT1",False)       #create client object

client.on_subscribe = on_subscribe   #assign function to callback
#client.on_disconnect = on_disconnect #assign function to callback
client.on_connect = on_connect #assign function to callback
client.on_disconnect = on_disconnect
client.on_message=on_message

client.connect(broker,port)           #establish connection
#client.loop_start()


client.subscribe("interview/IoT2")
def sensor_reading():
 k=d.read_retry(d.DHT11,21)
 t=k[1]
 return t
def myfunction(): #runs forever break with CTRL+C
      #client.on_message=on_message
      print("publishing on topic ",topic1)
      msg=sensor_reading()
      client.publish(topic1,msg)
      time.sleep(30)
      global count
      count = count+1
      global starttime
      starttime = time.time()
      global flag
      flag = True
      print(msg)
      #time.sleep(5)
def buffer():
    #print('in buffer')
    a=sensor_reading()
    print('im in buffer')
    print(a)
    q.append(a)
    print(q)
def get_buffer():
     print('im in get buffer')
     try:
       if flag and len(q)>0:
        client.publish(topic1,q.pop())
        print('buffer published')

     except:
      print('q not yet initiated')

getbufferthread = BufferThread(5, get_buffer)
getbufferthread.start()
#my = BufferThread(60,buffer)

#client.on_message=buffer
while True:
   global flag
   global starttime
   client.loop()
   print(count)
   if (time.time() - starttime) > 30 and flag:
       buffer()
       flag=False
#client1.disconnect()

#client1.loop_stop()
