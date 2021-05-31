describe('Minimal E2E tests for UB Events website', () => {
    beforeEach(() => {
        // Executes @ suite level
        cy.visitSite();
    });

    it('Check the home page accessibility', () => {
      cy.validateHomePage();
    });

    it('Validate User Signup', () => {
      cy.validateUserSignUpPage();
      // Assuming the signup is successful - Validate if the user lands
      // on events page
      cy.validateEventsPage();
    });

    it('Validate User Login Flow + Direct Messages', () => {
      cy.visitLoginPage();
      cy.setAuth();
      cy.validateEventsPage();
    });

    it('Validate User Logout Flow', () => {
      cy.visitLoginPage();
      cy.setAuth();
      cy.validateEventsPage();
      cy.logoutUser();
    });
  });