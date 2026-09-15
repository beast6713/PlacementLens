/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  darkMode: "class",
  theme: {
    extend: {
      colors: {
        background: "#090D16",
        foreground: "#F8FAFC",
        card: "#0F172A",
        "card-hover": "#1E293B",
        border: "#1E293B",
        primary: {
          DEFAULT: "#00F0FF",
          foreground: "#090D16",
          glow: "rgba(0, 240, 255, 0.4)"
        },
        secondary: {
          DEFAULT: "#6366F1",
          foreground: "#FFFFFF",
          glow: "rgba(99, 102, 241, 0.4)"
        },
        accent: {
          DEFAULT: "#3B82F6",
          emerald: "#10B981",
          amber: "#F59E0B",
          rose: "#F43F5E"
        }
      },
      animation: {
        "border-beam": "border-beam calc(var(--duration)*1s) infinite linear",
        marquee: "marquee var(--duration) linear infinite",
        "marquee-vertical": "marquee-vertical var(--duration) linear infinite",
        pulse: "pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite",
        shimmer: "shimmer 2s linear infinite",
      },
      keyframes: {
        "border-beam": {
          "100%": {
            "offset-distance": "100%",
          },
        },
        marquee: {
          from: { transform: "translateX(0%)" },
          to: { transform: "translateX(-50%)" },
        },
        "marquee-vertical": {
          from: { transform: "translateY(0%)" },
          to: { transform: "translateY(-50%)" },
        },
        shimmer: {
          "0%": { backgroundPosition: "0 0" },
          "100%": { backgroundPosition: "-200% 0" }
        }
      },
    },
  },
  plugins: [],
}
