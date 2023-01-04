import requests
import threading
import json

class Osint:
    def __init__(self):
        self.steamID = ""
        self.token = ""
        self.myFriends = []
        self.allFriends = []
        self.closeFriend = []
        self.threads = []

    def scanProfile(self, steamID, token):
        self.token = token
        self._allMyFriends(steamID)
        self._threads()
        self.closeFriends()

    def get_friends(self, steamID):
        scanProfile = f'http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key={self.token}&steamid={steamID}'
        request = requests.get(scanProfile)
        friends = json.loads(request.content)
        if(friends):
            return friends["friendslist"]["friends"]

    def _allMyFriends(self, steamID):
        for friend in self.get_friends(steamID):
            if(len(friend)):
                self.myFriends.append(friend["steamid"])

    def _threads(self):
        for url in self.myFriends:
            threadURL = f'http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key={self.token}&steamid={url}'
            thread = threading.Thread(target=self._friendsByFriends, args=(threadURL,))
            self.threads.append(thread)
        for thread in self.threads:
            thread.start()    
        for thread in self.threads:
            thread.join()
    def _friendsByFriends(self, steamURL):
        requestThreads = requests.get(steamURL)
        friends = json.loads(requestThreads.content)
        if(friends):
            for friendOFfriend in friends["friendslist"]["friends"]:
                self.allFriends.append(friendOFfriend['steamid'])
    def closeFriends(self):
        for myFriend in self.myFriends:
            if(myFriend in set(self.allFriends)):
                self.closeFriend.append({
                "profile":f"https://steamcommunity.com/profiles/{myFriend}/", 
                "accuracy": self.allFriends.count(myFriend)})
        return self.closeFriend

    def clearList(self):
        self.steamID = ""
        self.myFriends = []
        self.allFriends = []
        self.closeFriend = []
        self.threads = []
        return