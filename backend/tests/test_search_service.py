#
# System Imports
#


#
# Local Imports
#
from lib.service_client import ServiceClient
from lib import utils as utils
from config import Config


class TestSearchService:
    """
    Class to validate APIs related to Author Service
    """
    session_obj = None
    test_data = utils.get_search_test_data()

    @classmethod
    def setup_class(cls):
        """
        Functionality that needs to be executed before triggering
        all the tests
        """
        cls.session_obj = ServiceClient(Config.search_service_url)

    def test_validate_search_service_functionality(cls):
        """
        Given an input argument validate if search service returns right
        response
        """
        search_query_item = cls.test_data[0]
        test_k_value = utils.get_search_k_value_for_input(
            search_query_item.get('associated_max_k_value'))
        srch_payload = utils.get_search_service_payload(
            search_query_item.get('query_string'), test_k_value
        )
        print("Payload constructed is - %s" % srch_payload)
        resp = cls.session_obj.post(
            payload=srch_payload)
        print("Response is: %s" % resp.json())
        assert resp.status_code == 200
        assert len(resp.json()) == test_k_value
        rels_retrieved = [each_ele.get('relvance') for each_ele in resp.json()]
        assert rels_retrieved == sorted(rels_retrieved, reverse=True)
        # Other Validations follow