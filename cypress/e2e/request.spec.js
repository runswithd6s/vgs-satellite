describe('Localhoste request actions flow', function() {
  beforeEach(() => {
    cy.intercept('GET', 'flows.json').as('getFlows');
    cy.intercept('DELETE', 'flows/**').as('deleteFlow');
    cy.intercept('POST', 'flows/**').as('postFlow');
    cy.intercept('PUT', 'flows/**').as('putFlow');
    cy.cleanupFlows();
    cy.fixCypressSpec(__filename);
  });

  it('Send, duplicate, replay, edit, delete request', function() {
    cy.visit('/');
    cy.get('.menu-item').contains('Logs').click();
    cy.wait(['@getFlows']);
    cy.get('[data-role="no-logs"]').toMatchSnapshot();

    cy.task('viaProxy', {
      method: 'POST',
      url: 'http://httpbin.org/post',
      data: { foo: 'bar' },
    });

    cy.get('[data-role="logs-row"]').should('have.length', 1);
    cy.get('[data-role="logs-row"] .badge-success').contains('200');
    cy.get('[data-role="logs-row"]').contains('/post').click();

    cy.get('button').contains('Duplicate').click({ force: true });
    cy.wait(['@postFlow', '@getFlows']);
    cy.get('[data-role="logs-row"]').should('have.length', 2);

    cy.get('[data-role="logs-row"]').contains('/post').click();
    cy.get('[data-role="log-details-trace-id"]').should('have.length', 1);
    cy.get('button').contains('Delete').click({ force: true });
    cy.wait(['@deleteFlow', '@getFlows']);
    cy.get('[data-role="logs-row"]').should('have.length', 1);

    cy.get('[data-role="logs-row"]').contains('/post').click();
    cy.get('button').contains('Replay').click({ force: true });
    cy.wait(['@postFlow', '@getFlows']);
    cy.get('[data-role="logs-row"]').should('have.length', 1);
    cy.get('[data-role="logs-row"] [data-icon="reload"]');

    cy.get('[data-role="logs-row"]').contains('/post').click();
    cy.get('button').contains('Edit').click({ force: true });
    cy.get('[data-role="edit-path-input"] input').clear().type('/edited');
    cy.get('button').contains('Save').click({ force: true });

    cy.wait(['@putFlow', '@getFlows']);
    cy.get('[data-role="logs-row"]').contains('/edited').click();
    cy.get('button').contains('Delete').click({ force: true });

    cy.wait(['@deleteFlow', '@getFlows']);
    cy.get('[data-role="no-logs"]');
  });
});
