from abc import abstractmethod
from collections.abc import Iterator
from typing import Iterable


class Profile:
    def __init__(self, profile_id, email=None):
        self._id = profile_id
        self._email = email

    def get_id(self):
        return self._id

    def get_email(self):
        return self._email


class ProfileIterator(Iterator):
    _position = None

    def __init__(self, cache):
        self._cache = cache or []

    def __next__(self):
        try:
            value = self._cache[self._position]
            self._position += 1
        except IndexError:
            raise StopIteration()

        return value


class SocialNetwork(Iterable):
    def __init__(self, cache=None):
        self._cache = cache or []

    def __iter__(self):
        return ProfileIterator(self._cache)

    @abstractmethod
    def create_friends_iterator(self, profile_id):
        pass

    @abstractmethod
    def create_coworkers_iterator(self, profile_id):
        pass


class FacebookIterator(ProfileIterator):
    _position = None
    _cache = []

    def __init__(self, facebook, profile_id, type):
        self.facebook = facebook
        self.profile_id = profile_id
        self.type = type
        super().__init__(self._cache)

    def lazy_init(self):
        pass


class Facebook(SocialNetwork):
    def create_friends_iterator(self, profile_id):
        return FacebookIterator(self, profile_id, "friends")

    def create_coworkers_iterator(self, profile_id):
        return FacebookIterator(self, profile_id, "coworkers")


class SocialSpammer:
    def send(self, iterator):
        pass


class Application:
    def __init__(self, network, spammer):
        self.network = network
        self.spammer = spammer

    def send_spam_to_friends(self, profile_id):
        iterator = self.network.create_friends_iterator(profile_id)
        self.spammer.send(iterator)

    def send_spam_to_coworkers(self, profile_id):
        iterator = self.network.create_coworkers_iterator(profile_id)
        self.spammer.send(iterator)


if __name__ == "__main__":
    facebook = Facebook()
    app = Application(facebook, SocialSpammer())
    app.send_spam_to_friends(1)
    app.send_spam_to_coworkers(1)
