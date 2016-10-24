import requests

def send_notification(host, text, api_key):
    enc_api = base64.b64encode(api_key.encode('ascii'))
    not_url = 'http://' + host + ':8080/api/v2/device/notifications'
    headers = {
    'Content-type': 'application/json',
    'Accept': 'application/json',
    'Authorization': b'Basic ' + enc_api,
    'Cache-Control': 'no-cache',
     }
    data = '{"priority": "warning", "icon_type": "none", "model": {"frames": [{"icon": "i3579", "text":' + text + '}], "sound": {"category": "notifications", "id": "positive4"}}}'
    requests.post(noturl, headers=headers, data=data)
