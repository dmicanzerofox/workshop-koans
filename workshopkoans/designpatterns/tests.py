from django.test import TestCase
from .dependency_injection_refactor import PeopleRetriever, BackendBase
from .extract_superclass_refactor import pay_worker
from .object_composition_design_pattern import \
    Airplane, REALLY_COMPLICATED_FLIGHT, Bird, Duck, Eagle


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
        class IndependentContractor(object):
            pass
        contractor = IndependentContractor()
        pay_worker(contractor)

    def test_dependency_injection_refactor(self):
        """
        Currently we have a people retriever that instantiates a mysql
        connection in it's constructor. Refactor PeopleRetriever
        to allow us to initialize it with any BackendBase class.

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
        a an extremely complex `fly` algorithm for its robots.

        Now that management has decided to enter the aerospace market,
        they would like to use the same fly algorithm
        to power their airplanes.  Apply object composition
        to accomplish this.

        :return:
        """
        eagle = Eagle()
        airplane = Airplane()
        airplane.flyer == eagle.flyer
        self.assertEqual(airplane.fly(), REALLY_COMPLICATED_FLIGHT)

    def test_encapsulation_design_pattern(self):
        self.fail()
