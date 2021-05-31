# Backend Tests

## Steps to setup the test bed
* Create a virtual envrionment, command for reference - ```virtualenv -p python3 ~/Desktop/venvs/ub-bknd```
* Activate the virtual environment - ```source ~/Desktop/venvs/ub-bknd/bin/activate```
* Install the dependencies - ```pip install -r requirements.txt```
* All the tests available currently can be executed with the following command - ```python -m pytest tests```

NOTE: Make sure all the 3 services - server/search-service/author-service are up and running

## Assumptions / Known Issues
* The idea is to basically enable layout for writing both independent tests + integration tests
* The tests developed so far are not exhaustive and just positive ones
* I see the services work only for postive use cases and are hung in case of negative test cases like malformed paylaods and etc - So, didn't dig deeper to cover other tests / scenarios
* I have compromised in test data generation / comments / etc @ some instances due to time constraints intentionally. It was definitely not realistic to cover all the scenarios in the specified time
* The test data generation is critical and if taken care smartly - The tests can be parametrized for various input attributes to validate the robustness of API/s
