import json
import requests

API_BASE_URL = "https://fantasy.premierleague.com/drf/"

class User(object):
    """
    A class representing a user of the Fantasy Premier League.
    """

    def __init__(self, user_id):
        self.id = user_id

        self.cup = self._cup()
        self.entry = self._entry()
        self.history = self._history()
        self.leagues = self._leagues()
        self.leagues_entered = self._leagues_entered()
        self.picks = self._picks()
        self.transfers = self._transfers()

    def _cup(self):
        """
        Returns a dictionary with information about the cup progression of the
        user.
        """
        return requests.get("{}entry/{}/cup".format(API_BASE_URL,
            self.id)).json()

    def _entry(self):
        """
        Returns a dictionary containing information about the user.
        """
        return requests.get("{}entry/{}".format(API_BASE_URL, self.id)).json()

    def _history(self):
        """
        Returns a dictionary containing the history of the user.
        """
        return requests.get("{}entry/{}/history".format(API_BASE_URL,
            self.id)).json()

    def _leagues(self):
        """
        Returns a dictionary with information about all leagues that the user is
        participating in.
        """
        return requests.get("{}entry/{}".format(API_BASE_URL, self.id)).json()

    def _leagues_entered(self):
        """
        Returns a dictionary with information about all leagues that the user is
        participating in.
        """
        return requests.get("{}leagues-entered/{}".format(API_BASE_URL,
            self.id)).json()

    def _picks(self):
        """
        Returns a dictionary containing all the picks of the user.
        """
        picks = {}
        for gameweek in range(1, 39):
            pick = requests.get("{}entry/{}/event/{}/picks".format(
                API_BASE_URL, self.id, gameweek))

            if pick.status_code == 404:
                return picks

            picks[gameweek] = pick.json()

        return picks

    def _transfers(self):
        """
        Returns a dictionary with all the transfers made by the user.
        """
        return requests.get("{}entry/{}/transfers".format(API_BASE_URL,
            self.id)).json()

if __name__ == '__main__':
    amos = User(3523615)