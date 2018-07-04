# randQR
1.when receving a string,first get its sha256string as qr image name,if exist,return the img,else generate
it and return

http://localhost:8000/qr/?qrstring=dfadfa/fads
slash is required


when request accepted,return msg like this:
{"code": 200, "data": {"content": "u4e8e15%(\u5305\u542b15%)", "hash": "a1ef024ce5a2a57dd0d2b7823a5ba775f5d8a54c7c64e0ff358ed433d1e05a86", "qr_url": "/static/a1ef024ce5a2a57dd0d2b7823a5ba775f5d8a54c7c64e0ff358ed433d1e05a86.png"}, "msg": "OK!"}

content is recorded in the qr image.
hostname+url to get the file. http://localhost:8000/static/a1ef024ce5a2a57dd0d2b7823a5ba775f5d8a54c7c64e0ff358ed433d1e05a86.png,for example
