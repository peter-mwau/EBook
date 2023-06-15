/** @type {import('tailwindcss').Config} */
module.exports = {
  mode: 'jit',
  purge: [],
    content: ["./src/**/*.{html,js}"],
    darkMode: 'class',
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