# import requests
# import onetimepass as otp
# import urllib.parse as urlparse
# from kiteconnect import KiteConnect
# import json

# def do_login_kite(username,password, totp,apikey,secretkey):
#     login_url = "https://kite.trade/connect/login?api_key=" + str(apikey)
#     print(f"Login Url : {login_url}")
#     request_token = ""
#     session = requests.Session()
#     session.headers.update(
#         {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3'})
#     session.get(login_url)
#     res0 = session.get(login_url)
#     res1 = session.post("https://kite.zerodha.com/api/login",
#                         data={'user_id': username,
#                               'password': password})

#     data = json.loads(res1.text)
#     print("Data", data)
#     res2 = session.post("https://kite.zerodha.com/api/twofa",
#                         data={'user_id': username,
#                               'request_id': data['data']["request_id"],
#                               'twofa_value': str(otp.get_totp(totp))})
#     print(res2.json(),"res2")
#     print(res0.url + "&skip_session=true")
#     try:
#         res = session.get(res0.url + "&skip_session=true")
#         print(res.url)
#         parsed = urlparse.urlparse(res.history[1].headers['location'])
#         request_token = urlparse.parse_qs(parsed.query)['request_token'][0]
#     except Exception as e:
#         print(e,"exeception")

#     session.close()
#     kite = KiteConnect(api_key=apikey)
#     print('request_token',request_token)
#     data = kite.generate_session(request_token, api_secret=secretkey)
#     print('data',data)
#     app = KiteConnect(apikey)
#     app.set_access_token(data['access_token'])
#     print(data['access_token'],"access_token")
#     return app,data

# username="BAX203"
# password="Test@#123"
# totp="TCZSUZMBG3W6W4CKPVXO3ZUSZTMDQ6H7"
# apikey="wi71gjy0lde2n48t"
# secretkey="2utx4v7uviccrbssvn1qtrrml5s7a07f"

import requests
import onetimepass as otp
import urllib.parse as urlparse
from kiteconnect import KiteConnect
import time

def do_login_kite(username, password, totp_secret, api_key, api_secret):
    login_url = f"https://kite.trade/connect/login?api_key={api_key}"
    print(f"Login URL: {login_url}")
    request_token = ""
    session = requests.Session()
    session.headers.update({'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3'})

 
    session.get(login_url)
    
  
    res1 = session.post("https://kite.zerodha.com/api/login", data={'user_id': username, 'password': password})
    data = res1.json()
    print("Login Response:", data)

    if res1.status_code != 200 or 'data' not in data:
        print("Login failed.")
        return None, "Login failed"

 
    totp_value = otp.get_totp(totp_secret)
    res2 = session.post("https://kite.zerodha.com/api/twofa", data={
        'user_id': username,
        'request_id': data['data']["request_id"],
        'twofa_value': str(totp_value)
    })
    print("TOTP Response:", res2.json())

    if res2.status_code != 200 or res2.json().get('status') != 'success':
        print("Invalid TOTP.")
        return None, "Invalid TOTP"


    try:
        res = session.get(login_url + "&skip_session=true")
        for hist in res.history:
            if 'location' in hist.headers:
                parsed = urlparse.urlparse(hist.headers['location'])
                if 'request_token' in urlparse.parse_qs(parsed.query):
                    request_token = urlparse.parse_qs(parsed.query)['request_token'][0]
                    break
    except Exception as e:
        print("Exception while fetching request token:", e)
        return None, str(e)

    if not request_token:
        print("Failed to retrieve request token.")
        return None, "Failed to retrieve request token"

    print('Request Token:', request_token)
    print('Request Token Time:', time.time())

   
    kite = KiteConnect(api_key=api_key)
    access_token = None
    try:
        data = kite.generate_session(request_token, api_secret=api_secret)
        print('Session Data:', data)
        access_token = data['access_token']
        kite.set_access_token(access_token)
        print('Access Token:', access_token)
    except Exception as e:
        print("Exception during session generation:", e)
        return None, str(e)


    if access_token:
        try:
            profile = kite.profile()
            print("Access token is valid.")
            print("Profile:", profile)
        except Exception as e:
            print("Access token is invalid or has expired:", e)
            return None, "Access token is invalid or has expired"
    else:
        print("Failed to generate access token.")
        return None, "Failed to generate access token"

    return kite, data

username = "BAX203"
password = "Test@#123"
totp_secret = "TCZSUZMBG3W6W4CKPVXO3ZUSZTMDQ6H7"
api_key = "wi71gjy0lde2n48t"
api_secret = "2utx4v7uviccrbssvn1qtrrml5s7a07f"

kite, data = do_login_kite(username, password, totp_secret, api_key, api_secret)
if kite:
    print("Login successful:", data)
else:
    print("Login failed:", data)
