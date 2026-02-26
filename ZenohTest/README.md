Connecting to the ESP32 with zenoh 

download zenohd for you here
https://download.eclipse.org/zenoh/zenoh/latest/

download uv if you don't have it already (see uv astral)

then run: 
uv venv 
then 
uv sync 
then run 
the subscriber (the esp will be the publisher that you will ahve to make, there is an example in z_pub.py)

in the background you will have to run .\zenohd.exe 
for example i can run .\zenohd.exe -l tcp/10.0.0.247:7447
where 10.0.0.247 is my ipv4 ip address 
then on the esp32 you will have to configure for it to send to this ip

then in your publisher that will run on the esp32 you can publish a serialized array, and then deserialize it with the pub in python ( we will move this to c++ later.)