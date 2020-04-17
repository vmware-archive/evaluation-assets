import requests


def send_a_request(url):
    try:
        r = requests.get(url)
        print("Sending request to {}, Status Code: {}".format(url, r.status_code))
    except requests.exceptions.ConnectionError as e:
        print("Error connecting to server {}".format(e))
        pass
