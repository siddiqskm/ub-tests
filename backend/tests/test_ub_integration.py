#
# System Imports
#


#
# Local Imports
#
from lib.service_client import ServiceClient
from lib import utils as utils
from config import Config


class TestProxyService:
    """
    Class to validate APIs related to Author Service
    """
    session_obj = None
    test_data = utils.get_proxy_service_test_data()

    @classmethod
    def setup_class(cls):
        """
        Functionality that needs to be executed before triggering
        all the tests
        """
        cls.session_obj = ServiceClient(Config.proxy_service_url)

    def test_validate_proxy_service_functionality(cls):
        """
        Given an input argument validate if search service returns right
        response
        """
        # I hate this but a static config to validate results again
        input_k_val = 3
        # Get a static paylaod to validate this API
        srch_payload = utils.get_proxy_service_paylaod(input_k_val)
        print("Payload constructed is - %s" % srch_payload)
        resp = cls.session_obj.post(
            payload=srch_payload)
        print("Response is: %s" % resp.json())
        assert resp.status_code == 200
        # We have only one query in static paylaod constructed - So, 
        # Validating the same
        assert len(resp.json()) == 1
        assert len(resp.json()[0]) == input_k_val
        # Validate the order of releveance attribute returned
        rels_retrieved = [each_ele.get('relvance') for each_ele in resp.json()[0]]
        assert rels_retrieved == sorted(rels_retrieved, reverse=True)
        assert all('author' in each_ele for each_ele in resp.json()[0])
        # Other Validations follow ...