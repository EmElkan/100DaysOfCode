/// <reference types="cypress" />

describe("Our first suite", () => {

    it('First test', () => {

        cy.visit("/")
        cy.contains("Forms").click()
        cy.contains("Form Layouts").click()

        // by Tag Name
        cy.get("input")

        // by ID
        cy.get("#inputEmail1")

        // by Class name
        cy.get(".input-full-width")

        // by Attribute name
        cy.get("[placeholder]")

        // by Attribute name and value
        cy.get("[placeholder='Email']")

        // by Class value
        cy.get("[class='input-full-width size-medium shape-rectangle']")

        // by Tag name and Attribute with value
        cy.get("input[placeholder='Email']")

        // by two different attributes
        cy.get("[placeholder='Email'][type='email']")

        // by Tag name, Attribute with value, ID and Class name
        cy.get("input[placeholder='Email']#inputEmail1, input-full-width")

        // recommended way
        cy.get("[data-cy='imputEmail1']")

    })

    it.only('Second test', () => {

      cy.visit("/")
      cy.contains("Forms").click()
      cy.contains("Form Layouts").click()

      cy.get("[data-cy='signInButton']")

      cy.contains("Sign in")
      cy.contains("[status='warning']", "Sign in")

      cy.get('#inputEmail3')
        .parents('form')
        .find('button')
        .should('contain', 'Sign in')
        .parents('form')
        .find('nb-checkbox')
        .click()

      cy.contains('nb-card', 'Horizontal form').find('[type="email"]')


    })

it.only('list and dropdown', () => {
  cy.visit('/')

  cy.get('nav nb-select').then( dropdown => {
  cy.wrap(dropdown).click()
  cy.get('.options-list nb-option').each( (listItem, index) => {
    const itemText = listItem.text().trim()

    const colors = {
      "Light": "rgb(255, 255, 255)",
      "Dark": "rgb(34, 43, 69)",
      "Cosmic": "rgb(50, 50, 89)",
      "Corporate": "rgb(255, 255, 255)"
    }

    cy.wrap(listItem).click()
    cy.wrap(dropdown).should('contain', itemText)
    cy.get('nb-layout-header nav').should('have.css', 'background-color', colors[itemText])
    if( index < 3){
      cy.wrap(dropdown).click()

    }

  })
})
})
})
