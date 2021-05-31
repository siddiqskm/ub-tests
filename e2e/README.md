# ub-tests E2E UI Tests

## Steps to setup testbed
* Navigate to the base DIR i.e. - e2e
* Make sure latest version of NodeJS / Cypress is installed - Reference: https://docs.cypress.io/guides/getting-started/installing-cypress
* Run the following command - ```npm install``` from base directory to take care of the dependencies
* Execute - ```npx cypress open``` command from terminal to cypress pane which shows the suite already developed by name e2e
*  Click on e2e suite and the test execution will follow

## Assumptions / Known Issues
* The tests developed so far are just to cover the user flows asked for - exhaustive validations can be further added
* Test Libraries need to be developed - some commands in 'support' are developed to provide a glimpse on the plan
* POMS / static configurations need be managed better