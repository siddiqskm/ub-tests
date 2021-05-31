describe('Minimal E2E tests for UB Events website', () => {
    before(() => {
        // Executes @ suite level
        console.log('Yup, am inside before');
        cy.visit('');
    });

    beforeEach(() => {
        // To execute before each and every test
    });

    it('Check the availability of elements on home page', () => {
      cy.get('#layout-stack-wrapper').should('be.visible');
    });
  });