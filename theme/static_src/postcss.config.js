module.exports = {
  content: [
    '../templates/**/*.html',
    '../../templates/**/*.html', // Путь к вашим основным шаблонам
    '../../**/templates/**/*.html', // Поиск шаблонов во всех приложениях
  ],
  plugins: {
    "@tailwindcss/postcss": {},
    "postcss-simple-vars": {},
    "postcss-nested": {}
  },
}
