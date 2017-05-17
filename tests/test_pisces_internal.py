import datetime
import requests
import tabulate
import unittest


test = {}


def build_table(list1, list2):
    # function builds a two column table containing url's and status codes
    report = [""] * len(list1)
    for idx, item in enumerate(list1):
        report[idx] = [list1[idx], list2[idx]]
    return report

def start_report():
    start_time = datetime.datetime.utcnow()
    print(str(start_time))

def write_report(check_pages, response):
    try:
        report = build_table(check_pages, response)
        headers = ["expected", "actual url or status"]
        output_table = tabulate.tabulate(report, headers, tablefmt='grid')
        print(output_table)
        n_tests = len(response)
        n_successes = response.count(200)
        test_result = str(n_successes) + " of " + str(n_tests) + " pass.\n"
        print(test_result)
    except:
        print('report error in test')
    finally:
        pass
        #print("Time elapsed = " + str((end_time-start_time).seconds) + " seconds")
    return

def end_report():
    end_time = datetime.datetime.utcnow()
    print(str(end_time))

class TestPiscesPages(unittest.TestCase):
    """
    this testing routine accepts a list of pages and performs a series of unit tests that ensure
    that the web pages are up and operational on the server.
    """

    def setup(self):
        pass

    def teardown(self):
        pass

    def test_pisces_200(self):
        start_report()
        servers = ["https://qedinternal.epa.gov/pisces/", "http://127.0.0.1:8000/pisces/"]
        pages = ["", "watershed", "stream", "algorithms", "references"]
        check_pages = [s + p for s in servers for p in pages]
        response = [requests.get(p).status_code for p in check_pages]
        response_200s = ([200] * len(response))
        write_report(check_pages, response)
        self.assertListEqual(response, response_200s)
        end_report()

if __name__ == '__main__':
    unittest.main()