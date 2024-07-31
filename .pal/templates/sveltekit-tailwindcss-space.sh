# Create sveltekit project and install packages

yarn create svelte $1
cd $1
yarn install

# Add tailwindcss

yarn add -D tailwindcss postcss autoprefixer
npx tailwindcss init -p

echo "import adapter from '@sveltejs/adapter-auto';
import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';
/** @type {import('@sveltejs/kit').Config} */
const config = {
  kit: {
    adapter: adapter()
  },
  preprocess: vitePreprocess()
};
export default config;" > svelte.config.js
echo "/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{html,js,svelte,ts}'],
  theme: {
    extend: {}
  },
  plugins: []
};" > tailwind.config.js

touch ./src/app.css
echo "@tailwind base;
@tailwind components;
@tailwind utilities;" > ./src/app.css

touch ./src/routes/+layout.svelte
echo "<script>
  import '../app.css';
</script>

<slot />" > ./src/routes/+layout.svelte

# Add deta space

touch Spacefile
echo "v: 0
micros:
- name: $1
  src: .
  engine: svelte-kit
  primary: true
  dev: yarn dev" > Spacefile
