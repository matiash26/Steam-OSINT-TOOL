import requests
import json

class Osint:
    def __init__(self):
        self.steamID = ""
        self.token = ""
        self.myFriendsID = []
        self.allFriends = []
        self.closeFriend = []

    def scanProfile(self, steamID, token):
        self.token = token
        self._allMyFriends(steamID)
        self._friendsByFriends()
        self._setCloseFriends()

    def get_friends(self, id):
        steamAPI = f"http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key={self.token}&steamid={id}"
        request = requests.get(steamAPI)
        friends = json.loads(request.content)
        if(friends):
            return friends["friendslist"]["friends"]

    def _allMyFriends(self, steamID):
        for friend in self.get_friends(steamID):
            if(len(friend)):
                self.myFriendsID.append(friend["steamid"])

    def _friendsByFriends(self):
        for eachMyFriend in self.myFriendsID:
           hisFriends = self.get_friends(eachMyFriend)
           if(hisFriends):
            for friendByFriend in hisFriends:
                self.allFriends.append(friendByFriend["steamid"])

    def _setCloseFriends(self):
        for myFriend in self.myFriendsID:
            if(myFriend in set(self.allFriends)):
                self.closeFriend.append({
                "profile":f"https://steamcommunity.com/profiles/{myFriend}/", 
                "accuracy": self.allFriends.count(myFriend)})

    def closeFriends(self):
        return self.closeFriend
