// Cypress pada situs demo publik saucedemo.com. Tanpa data privat.
describe('SauceDemo', () => {
  const login = (user, pass) => {
    cy.visit('/');
    cy.get('[data-test="username"]').type(user);
    cy.get('[data-test="password"]').type(pass);
    cy.get('[data-test="login-button"]').click();
  };

  it('login gagal menampilkan pesan error', () => {
    login('standard_user', 'salah');
    cy.get('[data-test="error"]').should('contain', 'do not match');
  });

  it('login berhasil menampilkan 6 produk', () => {
    login('standard_user', 'secret_sauce');
    cy.url().should('include', '/inventory.html');
    cy.get('.inventory_item').should('have.length', 6);
  });

  it('checkout selesai sampai halaman konfirmasi', () => {
    login('standard_user', 'secret_sauce');
    cy.get('[data-test="add-to-cart-sauce-labs-backpack"]').click();
    cy.get('.shopping_cart_badge').should('have.text', '1');
    cy.get('.shopping_cart_link').click();
    cy.get('[data-test="checkout"]').click();
    cy.get('[data-test="firstName"]').type('Test');
    cy.get('[data-test="lastName"]').type('User');
    cy.get('[data-test="postalCode"]').type('12345');
    cy.get('[data-test="continue"]').click();
    cy.get('[data-test="finish"]').click();
    cy.get('[data-test="complete-header"]').should('contain', 'Thank you');
  });

  it('form checkout menolak isian kosong', () => {
    login('standard_user', 'secret_sauce');
    cy.get('[data-test="add-to-cart-sauce-labs-backpack"]').click();
    cy.get('.shopping_cart_link').click();
    cy.get('[data-test="checkout"]').click();
    cy.get('[data-test="continue"]').click();
    cy.get('[data-test="error"]').should('contain', 'First Name is required');
  });
});
