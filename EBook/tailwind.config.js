/** @type {import('tailwindcss').Config} */
module.exports = {
  experimental: {
    darkModeVariant: true,
  },
  darkMode: 'class',
  mode: 'jit',
  purge: [],
    content: ["./src/**/*.{html,js}"],
    theme: {
      extend: {},
      screens: {
        'sm': '448px',
        'md': '768px',
        'lg': '1100px',
        'xl': '1400px',
      },
    plugins: [],
  }
}