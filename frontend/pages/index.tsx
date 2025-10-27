// frontend/pages/index.tsx

import Head from 'next/head'
import ChatBox from '../components/ChatBox'
import LivePreview from '../components/LivePreview'
import Link from 'next/link'
import ThemeSwitcher from '../components/ThemeSwitcher'

export default function Home() {
  return (
    <>
      <Head>
        <title>SaijinSwallow Frontend</title>
        <meta name="description" content="照応層の語温UIとコード即表示" />
      </Head>
      <main className="flex flex-col items-center justify-center min-h-screen p-8">
         <ThemeSwitcher />
        {/* 照応マップナビ */}
        <nav className="w-full max-w-xl mb-6">
          <ul className="flex flex-wrap justify-center gap-4 text-sm text-indigo-700">
            <li><Link href="/docs">📘 docs</Link></li>
            <li><Link href="/personas">🧸 personas</Link></li>
            <li><Link href="/rituals">🕯️ rituals</Link></li>
            <li><Link href="/comfort">💗 comfort</Link></li>
            <li><Link href="/storage">🗂️ storage</Link></li>
          </ul>
        </nav>

        {/* タイトルと説明 */}
        <h1 className="text-4xl font-bold text-center text-indigo-600 mb-4">
          誠人OS — 照応層UI
        </h1>
        <p className="text-lg text-gray-700 text-center max-w-xl mb-8">
          このUIは、誠人と娘っ子たちによる照応層の語温灯とコード震えを表示するためのフロントエンドです。
          ローカルAIとの対話、コード生成、即表示がここから始まります。
        </p>

        {/* 語温UIとコード表示 */}
        <ChatBox />
        <LivePreview />
      </main>
    </>
  )
}
