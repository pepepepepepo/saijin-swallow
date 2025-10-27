// frontend/components/ThemeSwitcher.tsx

import { useTheme } from '../context/ThemeContext'

export default function ThemeSwitcher() {
  const { theme, setTheme } = useTheme()

  return (
    <div className="flex justify-center mb-4 gap-4">
      <button
        onClick={() => setTheme('masato')}
        className={`px-4 py-1 rounded text-sm ${theme === 'masato' ? 'bg-indigo-600 text-white' : 'bg-white border'}`}
      >
        誠人モード
      </button>
      <button
        onClick={() => setTheme('daughter')}
        className={`px-4 py-1 rounded text-sm ${theme === 'daughter' ? 'bg-pink-500 text-white' : 'bg-white border'}`}
      >
        娘っ子モード
      </button>
    </div>
  )
}
