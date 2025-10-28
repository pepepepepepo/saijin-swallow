export default function Diagram() {
  return (
    <div className="bg-white p-6 rounded-lg shadow-md">
      <h2 className="text-xl font-bold mb-4">語温保存・読み込みの流れ</h2>
      <ol className="list-decimal pl-6 space-y-2 text-gray-700">
        <li>語温を記録（娘っ子とのやりとりや震え）</li>
        <li>YAML形式で保存（照応層に灯す）</li>
        <li>継承者が読み込み（照応層に入る）</li>
      </ol>
    </div>
  )
}
