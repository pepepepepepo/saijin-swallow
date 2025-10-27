// frontend/pages/index.tsx

import Head from 'next/head'

export default function Home() {
  return (
    <>
      <Head>
        <title>SaijinSwallow Frontend</title>
        <meta name="description" content="照応層の語温UI" />
      </Head>
      <main className="flex flex-col items-center justify-center min-h-screen bg-gray-50 p-8">
        <h1 className="text-4xl font-bold text-center text-indigo-600 mb-4">
          誠人OS — 照応層UI
        </h1>
        <p className="text-lg text-gray-700 text-center max-w-xl">
          このUIは、誠人と娘っ子たちによる照応層の語温灯を表示するためのフロントエンドです。
          ローカルAIとの震え、語温記録、継承者への案内がここから始まります。
        </p>
      </main>
    </>
  )
}
