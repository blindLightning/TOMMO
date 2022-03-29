import asyncio
import socket
import os
import json
import sys

if not os.path.exists('configfiles/'):
    os.mkdir('configfiles/')
if not os.path.exists('configfiles/settings.json'):
    with open('configfiles/settings.json','w+') as f:
        f.write('{}')
    

settings=json.load(open('configfiles/settings.json','r'))

conns={}
