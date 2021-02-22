# mqtt_thread
This project is created to accept data received from a sensor after every 30 seconds of delay, and each data point will be followed by a success or failure response.If the server is stopped, the data point will be stored in a buffer.

<ul>
  <li>Porgram is made multi-threaded</li>
  <li>Used the real sensors, and retrieved data from the censor</li>
</ul>

To run the project, use the commands <br>
<code>Python edgeprogram.py is edge program</code> <br>
<code>Python serverprogram.py is server program</code> <br>

Results will be stored in a .csv file
