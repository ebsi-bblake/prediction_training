import { defineConfig } from 'vite';

export default defineConfig({
  server: {
    proxy: {
      '/api': 'http://backend:50051'  // Ensure this proxy is correct
    },
    port: 3000,  // Ensure Vite is configured to run on port 3000
  }
});
