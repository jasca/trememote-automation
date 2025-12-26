/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          DEFAULT: '#147d7f', // Teal base
          light: '#2dd4bf',   // Lighter teal for glows
          dark: '#0f5c5e',    // Darker teal for depth
        },
        secondary: '#a1a1aa', // Light gray for secondary text in dark mode
        background: '#030712', // Rich black/navy background
        surface: '#111827',    // Card background
        accent: '#8b5cf6',     // Violet accent for gradients
      },
      fontFamily: {
        sans: ['Poppins', 'sans-serif'],
      },
      backgroundImage: {
        'gradient-radial': 'radial-gradient(var(--tw-gradient-stops))',
        'hero-glow': 'conic-gradient(from 180deg at 50% 50%, #147d7f55 0deg, #8b5cf655 180deg, #147d7f55 360deg)',
      }
    },
  },
  plugins: [],
}

