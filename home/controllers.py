import requests

def fetch_json_from_api(url):
    try:
        resp_data = requests.get(url)
        if resp_data.status_code == 200:
            return resp_data.json()
        else:
            return None
    except Exception as e:
        print(e)
        return None