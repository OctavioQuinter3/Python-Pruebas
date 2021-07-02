import requests
if __name__ == '__main__':
    url = 'https://httpbin.org/get'
    args = {'name':'Octavio', 'curso':'python'}
    response = requests.get(url,params=args)
    print(response.url)

    if response.status_code == 200:
        print(response.content)

