from django.shortcuts import render



class BackendBase(object):
    """
    A helper class to return data that the test asserts on
    """
    PEOPLE_LIST = (
        {'name': 'Tom', 'age': 50},
    )
    def get_people(self):
        return self.PEOPLE_LIST


class MySQLDbBackend(BackendBase):
    def get_people(self):
        print('MYSQL SPECIFIC NETWORK CALL - WOULD BE MOCKED')
        return super(MySQLDbBackend, self).get_people()


class MongoDbBackend(BackendBase):
    PEOPLE_LIST = (
        {'name': 'Mongo', 'age': 1},
    )
    def get_people(self):
        print('MONGO SPECIFIC NETWORK CALL - WOULD BE MOCKED')
        return super(MongoDbBackend, self).get_people()


class PeopleRetriever(object):

    def __init__(self):
        self.connection = MySQLDbBackend()

    def get_people(self):
        return self.connection.get_people()
