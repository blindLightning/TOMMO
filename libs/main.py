from libs.globals import *

async def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((settings['host'],settings['port']))
        s.listen()
        
        while True:
            conn, addr = s.accept()
            print(f'{conn} just connected')
            conns[addr]=conn
            for i in conns.values():
                data = i.recv(1024)
                data=str(data)
                print(data)
                #if data==b'chat\r\n':
                
                for c in conns.values():
                    c.sendall(bytes(data,encoding='utf-8'))
                    print(data)
                    


