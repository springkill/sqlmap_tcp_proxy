import sys
import socket
from flask import Flask, request
from binascii import hexlify, unhexlify
import chardet

app = Flask(__name__)

# args
host = sys.argv[1]
port = int(sys.argv[2])
start = int(sys.argv[3])
end = int(sys.argv[4])
hex_text = sys.argv[5].split(' ')  # Splitting strings into lists by spaces

@app.route('/')
def home():
    global hex_text

    a = request.args.get('a')

    if a:
        print(f"'a' is : {a}")  

        # Detection code
        encoding = chardet.detect(a.encode())['encoding']

        # Encode string to hexadecimal
        hex_str = [hexlify(c.encode(encoding)).decode() for c in a]

        # replace
        new_hex_text = hex_text[:start] + hex_str + hex_text[end:]
        hex_text = new_hex_text

        # send
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            tcp_message = ''.join(new_hex_text)
            #print(tcp_message)
            s.sendall(unhexlify(tcp_message))
            data = s.recv(1024)
            print('response is :', data.decode())
        return "success,response is "+data.decode()
    else:
        return "null 'a'"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=28888)
