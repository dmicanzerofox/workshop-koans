class Billable(object):
    pass


class Employee(Billable):
    def __init__(self, rate, hours):
        self.rate = rate
        self.hours = hours

    # getters are unpythonic!
    def get_rate(self):
        return self.rate

    def get_hours(self):
        return self.hours


def pay(amount):
    pass

def pay_worker(employee):
    assert isinstance(employee, Billable)
    total = employee.get_rate() * employee.get_billable_hours()
    pay(total)
