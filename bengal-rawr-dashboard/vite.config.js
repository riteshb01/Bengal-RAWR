import { defineConfig, loadEnv } from 'vite';
import react from '@vitejs/plugin-react';
import { resolve } from 'path';

// https://vitejs.dev/config/
export default defineConfig(({ mode }) => {
  const env = loadEnv(mode, process.cwd(), '');

  return {
    plugins: [react()],
    resolve: {
      alias: {
        '@': resolve(__dirname, 'src'),
      },
    },
    server: {
      port: 3000,
      open: true,
      proxy: {
        // Dev proxy: forwards /api/* to Django backend, avoids CORS in dev
        '/api': {
          target: env.VITE_API_BASE_URL?.replace('/api/v1', '') || 'http://localhost:8000',
          changeOrigin: true,
        },
      },
    },
    build: {
      outDir: 'dist',
      // Disable sourcemaps in production to avoid leaking source
      sourcemap: mode !== 'production',
    },
  };
});
