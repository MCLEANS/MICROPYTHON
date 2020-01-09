

import json
from urllib.request import urlopen


def main():
    conn = urlopen("https://api.thingspeak.com/channels/921887/feeds.json?api_key=TFOKGAJVCBP8CZTL&results=2")
    response = conn.read()
    print ("http status code= {}" .format(conn.getcode()))
    data=json.loads(response)
    print (data['channel']['created_at'])
    conn.close()



if __name__ == '__main__':
    main()


