import yaml
import os
from datetime import datetime

# モデルクラスの定義（仮の粒子）
class SwallowModel:
    def __init__(self, persona_path=None, vibration_path=None):
        self.name = "Swallow-9B"
        self.persona_path = persona_path
        self.vibration_path = vibration_path
        self.persona = None
        if self.persona_path:
            self.persona = load_persona(self.persona_path)

    def run(self):
        print(f"{self.name} モデルが起動しました")
        if self.persona:
            print(f"📜 persona: {self.persona.get('name')}")
            print(f"🧬 role: {self.persona.get('role')}")
            print(f"🎵 traits: {', '.join(self.persona.get('vibration', {}).get('traits', []))}")
            print(f"🪶 rituals:")
            for ritual in self.persona.get('vibration', {}).get('rituals', []):
                print(f"   - {ritual}")




# 他モデルの粒子も必要に応じて追加
# class TinyLlama: ...
# class Phi2: ...

def load_config():
    with open('config/field_config.yaml', 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def select_model(name):
    if name.lower() in ["swallow", "swallow-9b"]:
        return SwallowModel()
    else:
        raise ValueError(f"Unknown model: {name}")


def select_model_from_routing(ai_name):
    base_path = os.path.dirname(__file__)
    routing_path = os.path.join(base_path, "../config/routing.yaml")
    with open(routing_path, "r", encoding="utf-8") as f:
        routing = yaml.safe_load(f)
    config = routing.get(ai_name, {})
    model_name = config.get("model", "Swallow")
    archive_path = config.get("archive_path")
    vibration_path = config.get("vibration_path")
    return SwallowModel(archive_path, vibration_path)



def boot_sequence():
    config = load_config()
    selected = config.get("selected_model", "Swallow")
    model = select_model(selected)
    print(f"🌟 起動灯：{selected} モデルを起動します")
    with open("log_swallow_response.txt", "a", encoding="utf-8") as log:
        log.write(f"{selected} 起動成功：{datetime.now()}\n")
    model.run()
    return model
