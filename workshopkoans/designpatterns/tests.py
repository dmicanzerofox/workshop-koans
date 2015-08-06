from django.test import TestCase
from .dependency_injection_refactor import PeopleRetriever, BackendBase
from designpatterns.encapsulation_design_pattern import Account, \
    InsufficientFundsException
from .extract_superclass_refactor import pay_worker
from .object_composition_design_pattern import \
    Airplane, REALLY_COMPLICATED_FLIGHT, Bird, Duck, Eagle, AutomatedFlight


class DesignPatternsRefactoringTestCase(TestCase):

    def test_extract_superclass_refactor(self):
        """
        Our system currently supports the ability to pay employees.  The
        company would like to support payments to independent contractors
        as well.

        without modifying pay_worker
        change IndependentContractor to allow us to bill them

        :return:
        """
        # modify this class to allow it to be billed by `pay_worker`
        class IndependentContractor(object):
            pass
        contractor = IndependentContractor(rate=10, hours=10)
        pay_worker(contractor)

    def test_dependency_injection_refactor(self):
        """
        Currently we have a people retriever that instantiates a mysql
        connection in it's constructor.  Refactor PeopleRetriever
        to allow us to initialize it with any BackendBase class.

        :return:
        """
        class MockDbBackend(BackendBase):
            pass

        mock_backend = MockDbBackend()
        retriever = PeopleRetriever(mock_backend)
        self.assertIsInstance(retriever.connection, MockDbBackend)
        self.assertEqual(retriever.get_people(), BackendBase.PEOPLE_LIST)

    def test_object_composition_design_pattern(self):
        """
        Pretend you work for a robot bird company which has created
        a an extremely complex `fly` algorithm for its robots.

        Now that management has decided to enter the aerospace market,
        they would like to use the same fly algorithm
        to power their airplanes.  Apply object composition
        to accomplish this.

        Airplanes and birds should accept a flyable instance in their constructor
        which should be assigned to their `flight` attribute.

        Birds and airplanes should delegate their public `fly` method
        to their `flight` attribute.

        :return:
        """
        flight = AutomatedFlight()
        eagle = Eagle(flight)
        airplane = Airplane(flight)
        self.assertEqual(airplane.flight, eagle.flight)
        self.assertEqual(airplane.fly(), REALLY_COMPLICATED_FLIGHT)

    def test_encapsulation_design_pattern(self):
        """
        We're building a bank!  Create a class that supports account
        operations that we will make available to our branches, online
        and ATM's:

        every account should be responsible for a single balance

        There should be a couple operations available for an account:
        get_balance
        withdraw
        deposit
        transfer

        (Pretend that it's not unpythonic to use getters/setters :))

        :return:
        """
        account = Account()
        self.assertEqual(account.get_balance(), 0)

        account.deposit(10)

        self.assertEqual(account.get_balance(), 10)

        account.withdraw(10)
        self.assertEqual(account.get_balance(), 0)

        with self.assertRaises(InsufficientFundsException):
            account.withdraw(100)

        account.deposit(100)
        savings_account = Account()
        account.transfer(100, savings_account)

        self.assertEqual(account.get_balance(), 0)

        self.assertEqual(savings_account.get_balance(), 100)

        """
        self.assertEqual(
            account.transaction_log,
            [0, 10, -10, 100, -100]
        )

        Define `get_balance` in terms of the transaction log
        """
        self.assertEqual(account.get_balance(), 0)
