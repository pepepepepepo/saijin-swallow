// frontend/context/ThemeContext.tsx

import { createContext, useContext, useState } from 'react'

const ThemeContext = createContext<any>(null)

export const ThemeProvider = ({ children }: { children: React.ReactNode }) => {
  const [theme, setTheme] = useState<'masato' | 'daughter'>('masato')
  return (
    <ThemeContext.Provider value={{ theme, setTheme }}>
      <div className={theme === 'masato' ? 'bg-gray-50 text-gray-800' : 'bg-pink-50 text-pink-900'}>
        {children}
      </div>
    </ThemeContext.Provider>
  )
}

export const useTheme = () => useContext(ThemeContext)
