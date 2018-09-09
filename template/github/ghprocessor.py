import requests


def get_github(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    return None


def create_base_url(module):
    f = module.split('.')
    if len(f) < 4:
        return 'http://github.com/FAKE'

    return 'https://raw.githubusercontent.com/{user}/{project}/master/{path}'.format(
        user=f[1], project=f[2], path='/'.join(f[3:])
    )

