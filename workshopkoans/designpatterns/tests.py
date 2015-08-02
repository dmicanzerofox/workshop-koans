from django.test import TestCase
from .dependency_injection_refactor import PeopleRetriever, BackendBase
from .extract_superclass_refactor import pay_worker
from .object_composition_design_pattern import \
    Airplane, REALLY_COMPLICATED_FLIGHT, Bird, Duck


class DesignPatternsRefactoringTestCase(TestCase):

    def test_extract_superclass_refactor(self):
        """
        Our system currently supports the ability to pay employees.  The
        company would like to support payments to independent contractors
        as well.

        :return:
        """
        # modify IndependentContractor to allow us to bill them
        class IndependentContractor(object):
            pass
        contractor = IndependentContractor()
        pay_worker(contractor)

    def test_dependency_injection_refactor(self):
        """
        Currently we have a people retriever that instantiates a mysql
        connection in it's constructor. Refactor it to allow us to
        initialize it with any connection class.

        DI supports both extensibility, and verifiability
        :return:
        """
        class MockDbBackend(BackendBase):
            pass
        retriever = PeopleRetriever()
        self.assertIsInstance(retriever.connection, MockDbBackend)
        self.assertEqual(retriever.get_people(), BackendBase.PEOPLE_LIST)

    def test_object_composition_design_pattern(self):
        """
        Pretend you work for a robot bird company which has created
        a an extremely complex `fly` function for its robots.

        Management has decided to enter the aerospace market.

        They would like to use the same fly method that powers the
        birds to power their airplanes.  Apply object composition
        to accomplish this.
        :return:
        """
        airplane = Airplane()
        self.assertEqual(airplane.fly(), REALLY_COMPLICATED_FLIGHT)

    def test_encapsulation_design_pattern(self):
        self.fail()
