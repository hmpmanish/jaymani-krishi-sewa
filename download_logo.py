import urllib.request, re
url = 'https://html.duckduckgo.com/html/?q=Sharda+University+logo+png'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
html = urllib.request.urlopen(req).read().decode('utf-8')
matches = re.findall(r'src="([^"]+)"', html)
for m in matches:
    if 'duckduckgo' in m or 'proxy' in m or 'external' in m:
        if m.startswith('//'): m = 'https:' + m
        print('Downloading', m)
        try:
            urllib.request.urlretrieve(m, 'sharda_logo.png')
            print('Downloaded logo')
            break
        except Exception as e:
            print(e)
