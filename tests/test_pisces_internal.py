import datetime
import requests
import tabulate
import unittest


test = {}

servers = ["https://qedinternal.epa.gov/pisces/","http://127.0.0.1:8000/pisces/"]

pages = ["", "watershed", "stream", "algorithms", "references"]

# api_endpoints = ["https://cyan.epa.gov/cyan/cyano/location/data/28.6138/-81.6227/2017-12-08",
#                  "https://cyan.epa.gov/cyan/cyano/notifications/2015-05-03T20-16-26-000-0400",
#                  #if the next png 500s, you can get an updated image from a specific location e.g.,
#                  #https://cyan.epa.gov/cyan/cyano/location/images/28.6138/-81.6227/
#                  "https://cyan.epa.gov/cyan/cyano/location/images/envisat.2012094.0403.1551C.L3.EF3.v670.CIcyano2.png",
#                  "https://cyan.epa.gov/cyan/cyano/location/images/28.6138/-81.6227/"]

#following are lists of url's to be processed with tests below
check_pages = [s + p for s in servers for p in pages]

def build_table(list1, list2):
    # function builds a two column table containing url's and status codes
    report = [""] * len(list1)
    for idx, item in enumerate(list1):
        report[idx] = [list1[idx], list2[idx]]
    return report


def write_report(test_name, col1, col2, start_time):
    try:
        print(test_name)
        report = build_table(col1, col2)
        headers = ["expected", "actual url or status"]
        output_table = tabulate.tabulate(report, headers, tablefmt='grid')
        print(output_table)
    except:
        print('report error in test')
    finally:
        end_time = datetime.datetime.utcnow()
        print(str(end_time))
        print("Time elapsed = " + str((end_time-start_time).seconds) + " seconds")
    return

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
        start_time = datetime.datetime.utcnow()
        test_name = str(start_time) + "\nPage access for pisces pages \n"
        response = [requests.get(p).status_code for p in check_pages]
        n_tests = len(response)
        response_200s = ([200] * n_tests)
        n_successes = response.count(200)
        test_result = str(n_successes) + " of " + str(n_tests) + " pass.\n"
        test_name = test_name + test_result
        write_report(test_name, check_pages, response, start_time)
        self.assertListEqual(response, response_200s)

if __name__ == '__main__':
    unittest.main()