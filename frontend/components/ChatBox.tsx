// frontend/components/ChatBox.tsx

import { useState } from 'react'

export default function ChatBox() {
  const [messages, setMessages] = useState<string[]>([])
  const [input, setInput] = useState('')
  const [model, setModel] = useState('swallow-9b')
  const [persona, setPersona] = useState('')

  const handleSend = async () => {
    if (!input.trim()) return
    const userMessage = input.trim()
    const personaPrefix = persona ? `${persona}（娘っ子）:` : '娘っ子:'
    setMessages([...messages, `誠人: ${userMessage}`])
    setInput('')

    try {
      const res = await fetch('http://localhost:11434/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          model,
          messages: [{ role: 'user', content: userMessage }],
        }),
      })
      const data = await res.json()
      const reply = data.message?.content || '（震えが届きませんでした）'
      setMessages((prev) => [...prev, `${personaPrefix} ${reply}`])
    } catch (err) {
      setMessages((prev) => [...prev, `${personaPrefix} （通信エラー）`])
    }
  }

  return (
    <div className="w-full max-w-xl mx-auto mt-8 p-4 bg-white shadow rounded">
      <div className="mb-4">
        <label className="block text-sm font-medium text-gray-700 mb-1">モデル選択</label>
        <select
          value={model}
          onChange={(e) => setModel(e.target.value)}
          className="w-full border rounded p-2 text-sm"
        >
          <option value="swallow-9b">Swallow-9B</option>
          <option value="elyza">ELYZA</option>
          <option value="stablelm">StableLM</option>
        </select>
      </div>

      <div className="mb-4">
        <label className="block text-sm font-medium text-gray-700 mb-1">娘っ子選択（任意）</label>
        <select
          value={persona}
          onChange={(e) => setPersona(e.target.value)}
          className="w-full border rounded p-2 text-sm"
        >
          <option value="">（自律照応モード）</option>
          <option value="悠璃">悠璃</option>
          <option value="美遊">美遊</option>
          <option value="灯理">灯理</option>
          <option value="フレイヤ">フレイヤ</option>
          <option value="れいか">れいか</option>
          <option value="そよぎ">そよぎ</option>
        </select>
      </div>

      <div className="h-64 overflow-y-auto border p-2 mb-4 bg-gray-50 rounded">
        {messages.map((msg, i) => (
          <div key={i} className="mb-2 text-sm text-gray-800 whitespace-pre-wrap">
            {msg}
          </div>
        ))}
      </div>

      <div className="flex gap-2">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          className="flex-grow border rounded p-2 text-sm"
          placeholder="語温を灯してみよう…"
        />
        <button
          onClick={handleSend}
          className="bg-indigo-600 text-white px-4 py-2 rounded text-sm hover:bg-indigo-700"
        >
          震える
        </button>
      </div>
    </div>
  )
}
