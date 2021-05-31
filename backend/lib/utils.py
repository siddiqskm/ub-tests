#
# System Imports
#
import os
import json
import random


#
# Local Imports
#
from lib import global_base_dir
from config import Config


def get_author_test_data():
    """
    Returns test data from the data file
    """
    content = None
    with open(os.path.join(global_base_dir, Config.test_data_file)) as fd:
        content = json.load(fd)
    return content

def get_books(test_data):
    """
    Returns a list of authors available from the test data
    """
    return test_data['authors']

def get_random_book(books):
    """
    Returns a random book
    """
    return random.choice(books)

def get_book_payload(input_book_id):
    """
    Returns the book payload for an appropriate input id
    """
    return "{\"book_id\": %s}" % input_book_id

def get_search_test_data():
    """
    Returns test data from the data file
    """
    """
    A dynamic solution to generate test data for search service need
    to be developed. This is time taking and hence moving ahead with
    static query for these prototype tests.
    """
    return [{"query_string": 'is', "associated_max_k_value": 10}]

def get_search_k_value_for_input(maximum_k_val):
    """
    For a specified query string - returns the appropriate k value
    """
    return random.choice(range(1, maximum_k_val))

def get_search_service_payload(input_query_string, k_value):
    """
    Returns the book payload for an appropriate input id
    """
    return ("{\"query\": \"%s\", \"results_length\": %s}"
        % (input_query_string, k_value))

def get_proxy_service_test_data():
    """
    Returns the test data for proxy service
    """
    return ["{\"queries\": [\"is\"], \"associated_max_k_value\": 10}"]

def get_proxy_service_paylaod(input_k_val):
    """
    Returns the paylaod for proxy service
    """
    return ("{\"queries\": [\"is\"], \"results_length\": %s}" % input_k_val)