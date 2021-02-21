# mqtt_thread
This project is created to accept data received from a censor after every 60 seconds of delay, and each data point will be followed by a success or failure response.If the server is stopped, the data point will be stored in a buffer.

<ul>
  <li>Porgram is made multi-threaded</li>
  <li>Used the real censors, and retrieved data from the censor</li>
</ul>

To run the project, use the commands <br>
<code>Python clienta.py</code> <br>
<code>Python clientb.py</code>
The results are stored in csv file
