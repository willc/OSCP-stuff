# Template for HTTP requests.
# Includes sample for image data extraction.

# Library for requests
import requests
# PIL adds image processing capabilities
from PIL import Image
# StringIO allows to read and write strings as files
from StringIO import StringIO

# URL to send stuff to - modify accordingly
target = 'http://somewebsite.com'

# Cookies - modify accordingly
cookieName1 = 'PHPSESSID'
cookieValue1 = 'somevaluehere'
cookies = {cookieName1: cookieValue1}

# Referer - modify accordingly
referer = 'http://somereferer.php'

# Headers - modify accordingly
headers = {'Referer': referer}

# Verifying we can connect
req = requests.post(target, cookies=cookies)
if req.status_code != requests.codes.ok:
        raise ValueError('Poof! Unable to connect to target t(X_X)t')
else:
        print('+++ Connected to target. Starting operation...\n')

# Sample image data extraction - gets image and RGB
theImage = Image.open(StringIO(req.content))
rColor, gColor, bColor = theImage.getpixel((1, 1))
answerColor = str(rColor) + ';' + str(gColor) + ';' + str(bColor)
data = {'color': answerColor, 'submit': '1'}

# Send cookies, data, and headers - modify accordingly
req = requests.post(target, cookies=cookies, data=data, headers=headers)

print('+++ Successfully sent information.\n') 
print(req.content)

