// frontend/utils/saveLog.ts

import fs from 'fs'
import path from 'path'
import yaml from 'yaml'

export function saveLogToYAML(log: string[], persona: string) {
  const timestamp = new Date().toISOString()
  const filename = `${persona || 'autonomous'}-${timestamp}.yaml`
  const filepath = path.join(process.cwd(), 'storage/yuri', filename)

  const data = {
    timestamp,
    persona: persona || '自律照応',
    log,
  }

  const yamlString = yaml.stringify(data)
  fs.writeFileSync(filepath, yamlString, 'utf8')
}
