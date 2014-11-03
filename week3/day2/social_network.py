from graph import DirectedGraph
import json
import requests


class SocialNetwork:
    MAX_DEPTH = 4

    def __init__(self, user, data_file_name='data.txt'):
        self.user = user
        self.graph = DirectedGraph()
        self.token = ('b5e76a8058b4977727fa4f9703da9601b7b2acc8', '')

#    def __get_tolken(self, filename):
#        with open(filename, 'r') as infile:
#            content = infile.read()
#            baba = json.loads(content)
#        return baba['token']

    def following(self):
        r = requests.get('https://api.github.com/users/{}/following'.format(self.user),  auth=self.token)
        return [user['login'] for user in r.json()]

    def is_followed(self, user):
        return user in self.following()

    def steps_to():
        


network = SocialNetwork('alexnad')
print(network.following())
