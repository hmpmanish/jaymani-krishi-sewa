/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        primary: "#166534", // Green 800
        secondary: "#4ade80", // Green 400
      }
    },
  },
  plugins: [],
}
