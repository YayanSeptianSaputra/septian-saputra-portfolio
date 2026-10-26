const { defineConfig } = require('cypress');
module.exports = defineConfig({
  e2e: { baseUrl: 'https://www.saucedemo.com', supportFile: false, video: false, defaultCommandTimeout: 8000 },
});
