import requests
res = requests.get('http://www.gutebug.org/eksd.txt')
res.raise_for_status()
playFile = open('romeoandjuliet.txt','wb')
for chunk in res.iter_content(1001010):
    playFile.write(chunk)

playFile.close()