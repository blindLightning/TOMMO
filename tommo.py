from libs import globals as g
from libs import main

def initialise():
    if g.settings['host']=='':
        g.settings['host']=input('Enter the ip or address that this TOMMO MUD server is running from.          ')
        try:
            g.settings['port']=int(input('Enter the port that this TOMMO MUD server is running through.          '))
        except ValueError:
            print('Integer not entered, try again.')
            g.sys.exit(1)
        g.json.dump(g.settings,open('configfiles/settings.json','w'))
    g.asyncio.run(main.main())
    

initialise()
