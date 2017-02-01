import unittest
import xmlrunner
from test_segment_size_post import SegmentSizePostTests


if __name__ == "__main__":

    test_classes_to_run = [SegmentSizePostTests]

    loader = unittest.TestLoader()

    suite_list = []
    for test_class in test_classes_to_run:
        suite = loader.loadTestsFromTestCase(test_class)
        suite_list.append(suite)

    big_suite = unittest.TestSuite(suite_list)
    runner=xmlrunner.XMLTestRunner(output='test-reports')
    runner.run(big_suite)

