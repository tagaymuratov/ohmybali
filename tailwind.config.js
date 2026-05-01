/** @type {import('tailwindcss').Config} */
export default {
  content: [
    './templates/**/*.html',
    './theme/templates/**/*.html',
    './home/templates/**/*.html',
    './users/templates/**/*.html',
    './search/templates/**/*.html',
    './**/templates/**/*.html',
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
      },
    },
  },
  plugins: [],
}
