// ***********************************************
// This example commands.js shows you how to
// create various custom commands and overwrite
// existing commands.
//
// For more comprehensive examples of custom
// commands please read more here:
// https://on.cypress.io/custom-commands
// ***********************************************
//
//
// -- This is a parent command --
// Cypress.Commands.add('login', (email, password) => { ... })
//
//
// -- This is a child command --
// Cypress.Commands.add('drag', { prevSubject: 'element'}, (subject, options) => { ... })
//
//
// -- This is a dual command --
// Cypress.Commands.add('dismiss', { prevSubject: 'optional'}, (subject, options) => { ... })
//
//
// -- This will overwrite an existing command --
// Cypress.Commands.overwrite('visit', (originalFn, url, options) => { ... })

Cypress.Commands.add('visitSite', () => {
    cy.clearCookies();
    console.log('Visiting home page !!!', Cypress.config().baseUrl);
    cy.visit('');
 });

Cypress.Commands.add('validateHomePage', () => {
    cy.get('[data-test-id="layout-stack-wrapper"]').should('be.visible');
    // More checks to be added
 });

 Cypress.Commands.add('validateUserSignUpPage', () => {
    // A better way to deal with user information in signup flow is required
    // i.e. Options to start on a clean slate everytime so that signup flow
    // doesn't fail with Email Already Exists error
    // POMS here should come from library - In a hurry to get stuff working now !!!
    cy.visitSite('./your-university/my-first-event/auth/logout');
    cy.get('a[href="/your-university/my-first-event/auth/register"]').should('be.visible');
    cy.get('a[href="/your-university/my-first-event/auth/register"]').click();
    cy.get('#register1-container').should('be.visible');
    // All these static values should come from a configuration, but not now !!!
    cy.get('#first-name').type('siddiq');
    cy.get('#last-name').type('hussain');
    cy.get('#email').type('siddiqhussainskm@gmail.com');
    cy.get('#password').type('Password@123');
    cy.get('#confirm-password').type('Password@123');
    cy.get('#privacy').check();
    cy.get('#continue').click();
    // Second Web Page which takes more preferences from user shows up
    // Lets validate if the redirection is as expected
    cy.url({ timeout: 20000 }).should('match', new RegExp('.*(your-university/my-first-event/auth/register2).*', 'g'));
    // Key-In other preferences - Apologies am out of email ids now !!!
 });

 Cypress.Commands.add('visitLoginPage', () => {
    cy.visitSite();
    cy.visitSite('./your-university/my-first-event/auth/logout');
    cy.get('a[href="/your-university/my-first-event/auth/login"]').click();
 });

 Cypress.Commands.add('setAuth', () => {
    // Static configurations need to go away and this information
    // (test users etc) should be picked from configs
    cy.get('#email').type('siddiqhussainskm@gmail.com');
    cy.get('#password').type('Password@123');
    cy.get('#login').click();
 });

 Cypress.Commands.add('validateEventsPage', () => {
    cy.url({ timeout: 20000 }).should('match', new RegExp('.*(your-university/my-first-event/chat).*', 'g'));
    // More checks to be added
 });

 Cypress.Commands.add('logoutUser', () => {
    // A harness to make sure logout happens everytime
    cy.visitSite('./your-university/my-first-event/auth/logout');
 });