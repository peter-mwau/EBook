/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ["./src/**/*.{html,js}"],
    dark: ['class', '[data-mode="dark"]'],
    theme: {
      extend: {},
      screens: {
        'sm': '500px',
        'md': '768px',
        'lg': '1100px',
        'xl': '1400px',
      },
    plugins: [],
  }
}