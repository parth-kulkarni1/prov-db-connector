from provdbconnector.tests.db_adapters.test_baseadapter import AdapterTestTemplate
from provdbconnector.tests.test_provapi import ProvApiTestTemplate
import unittest


def additional_tests():
    from examples.tests.test_examples import ExamplesTest
    return unittest.defaultTestLoader.loadTestsFromTestCase(ExamplesTest)
