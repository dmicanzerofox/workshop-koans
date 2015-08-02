from django.shortcuts import render



class BackendBase(object):
    """
    A helper class to return data that the test asserts on
    """
    PEOPLE_LIST = (
        {'name': 'Tom', 'age': 50},
        {'name': 'Jane', 'age': 50}
    )
    def get_people(self):
        return self.PEOPLE_LIST


class MySQLDbBackend(BackendBase):
    def get_people(self):
        print('NETWORK CALL WOULD BE MOCKED')
        return super(MySQLDbBackend, self).get_people()


class MongoDbBackend(BackendBase):
    pass


class PeopleRetriever(object):

    def __init__(self):
        self.connection = MySQLDbBackend()

    def get_people(self):
        return self.connection.get_people()
