

REALLY_COMPLICATED_FLIGHT = 'really complicated flight'


class Flyable(object):
    def fly(self):
        raise NotImplementedError()


class AutomatedFlight(Flyable):
    def fly(self):
        return REALLY_COMPLICATED_FLIGHT


class Bird(object):
    def fly(self):
        """
        Pretend this method is an extremely complicated method.
        :return:
        """
        return REALLY_COMPLICATED_FLIGHT


class Duck(Bird):
    pass


class Eagle(Bird):
    pass


class Penguin(Bird):
    def fly(self):
        return 'I dont fly'


class Airplane(object):
    # allow airplane to use
    pass
