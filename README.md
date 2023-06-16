# sqlmap_tcp_proxy

## Overview
sqlmap_tcp_proxy is a tcp proxy for sqlmap. Since sqlmap only supports http requests, this proxy is used to convert the parameters of sqlmap into tcp messages to be sent.

## How to use?
```python
python3 sqlproxy.py ip port Start_position End_position Initial_hexadecimal_message
```
sqlmap_tcp_proxy takes a total of five parameters:
```ip```: The IP of the server to receive the tcp request
```port```: The server port that will accept the tcp request
```Start_position```: Start position of the replacement message
```End_position```: End position of the replacement message
```Initial_hexadecimal_message```: Initial_hexadecimal_message

Testing ``` http://your_ip:28888/?a=```with sqlmap
The value of 'a' will be spliced into the tcp message

## Example
```python
python3 sqlproxy.py 127.0.0.1 29999 1 3 '11 22 33 44 55'
```
After running this command, the value of a will replace the first 11 and end with the third 33, for example, if the value of 'a' is 1, it will produce ```31 44 55 ```(The hexadecimal value of``` '1'``` is``` '31'```,if you want to replace ```one bit```, you can make the ```Start_position``` and ```End_position``` as the same)```.


## Demo

![demo](./demo.gif)
