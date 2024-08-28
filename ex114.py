import urllib.error
import urllib.request

try:
    site = urllib.request.urlopen('https://pt.khanacademy.org/')
except urllib.error.URLError:
    print('Deu erro')
else:
    print('Tudo ok')
