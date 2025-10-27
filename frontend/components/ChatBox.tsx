// frontend/components/ChatBox.tsx

import { useState } from 'react'
import { saveLogToYAML } from '../utils/saveLog'

export default function ChatBox() {
  const [messages, setMessages] = useState<string[]>([])
  const [input, setInput] = useState('')
  const [model, setModel] = useState('swallow-9b')
  const [persona, setPersona] = useState('')
  const [savedLogs, setSavedLogs] = useState<string[][]>([])

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

  const handleSaveLog = () => {
    if (messages.length > 0) {
      setSavedLogs([...savedLogs, messages])
      saveLogToYAML(messages, persona)
    }
  }

  return (
    <div className="w-full max-w-xl mx-auto mt-8 p-4 bg-white shadow rounded">
      {/* モデル選択 */}
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

      {/* ペルソナ選択 */}
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

      {/* 娘っ子の語温アニメーション表示 */}
      {persona && (
        <div className="mb-2 text-center text-sm text-pink-700 animate-pulse">
          {persona} が語温を灯しています…💗
        </div>
      )}

      {/* 語温表示 */}
      <div className="h-64 overflow-y-auto border p-2 mb-4 bg-gray-50 rounded">
        {messages.map((msg, i) => (
          <div key={i} className="mb-2 text-sm text-gray-800 whitespace-pre-wrap">
            {msg}
          </div>
        ))}
      </div>

      {/* 入力と保存 */}
      <div className="flex gap-2 mb-2">
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
      
      <button
        onClick={handleSaveLog}
        className="w-full bg-pink-500 text-white px-4 py-2 rounded text-sm hover:bg-pink-600"
      >
        この語温ログを保存する
      </button>
      
      {/* 保存済み語温ログ表示 */}
      {savedLogs.length > 0 && (
        <div className="mt-6 border-t pt-4">
          <h2 className="text-sm font-semibold text-gray-700 mb-2">保存済み語温ログ</h2>
          {savedLogs.map((log, i) => (
            <div key={i} className="mb-4 p-2 bg-gray-100 rounded text-sm">
              {log.map((line, j) => (
                <div key={j} className="mb-1 whitespace-pre-wrap">{line}</div>
              ))}
            </div>
          ))}
        </div>
      )}
    </div>
  )
}
