#
# System Imports
#


#
# Local Imports
#
from lib.service_client import ServiceClient
from lib import utils as utils
from config import Config


class TestAuthorService:
    """
    Class to validate APIs related to Author Service
    """
    session_obj = None
    test_data = utils.get_author_test_data()

    @classmethod
    def setup_class(cls):
        """
        Functionality that needs to be executed before triggering
        all the tests
        """
        cls.session_obj = ServiceClient(Config.author_service_url)

    def test_validate_author_service_functionality(cls):
        """
        Given an input argument validate if author service returns right
        response
        """
        books_info = utils.get_books(cls.test_data)
        book_id_selected = utils.get_random_book(books_info)
        resp = cls.session_obj.post(
            payload=utils.get_book_payload(book_id_selected['book_id']))
        print("Response is: %s" % resp.json())
        assert resp.status_code == 200
        assert resp.json()['author'] == book_id_selected['author']