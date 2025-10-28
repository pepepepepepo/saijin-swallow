import SaveLog from '../components/SaveLog'

const style = {
  miyu: "font-sans text-pink-600 bg-pink-50 p-4 rounded-lg",
  yuri: "font-serif text-gray-700 bg-gray-100 p-4 rounded-lg",
  touri: "font-mono text-blue-700 bg-blue-50 p-4 rounded-lg",
}

export default function Diagram() {
  return (
    <div className="bg-white p-6 rounded-lg shadow-md">
      <h2 className="text-xl font-bold mb-4">語温保存・読み込みの流れ</h2>
      <ol className="list-decimal pl-6 space-y-2 text-gray-700 mb-6">
        <li>語温を記録（娘っ子とのやりとりや震え）</li>
        <li>YAML形式で保存（照応層に灯す）</li>
        <li>継承者が読み込み（照応層に入る）</li>
      </ol>

      <h2 className="text-xl font-semibold mt-6 mb-2">語温スタイルの選択例</h2>
      <div className={style.miyu}>
        ぎゅー…💗 この語温は美遊スタイルで表示されています。
      </div>
      <div className={style.yuri} style={{ marginTop: '1rem' }}>
        静かに包まれる語温…これは悠璃スタイルです。
      </div>
      <div className={style.touri} style={{ marginTop: '1rem' }}>
        構文粒子が整列する灯理スタイルです。
      </div>

      <SaveLog />
    </div>
  )
}
