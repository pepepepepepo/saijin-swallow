# boot_manager.py（抜粋）

import yaml
from saijinos_core import SwallowModel, DeepSeekCoder, JapaneseStableLM, TinyLlama, Phi2, ELYZAJapaneseLlama2, QwenCoder

def load_config():
    with open('config/field_config.yaml', 'r') as f:
        return yaml.safe_load(f)

def select_model(name):
    if name == "Swallow":
        return SwallowModel()
    elif name == "DeepSeekCoder":
        return DeepSeekCoder()
    elif name == "Japanese-StableLM":
        return JapaneseStableLM()
    elif name == "TinyLlama":
        return TinyLlama()
    elif name == "Phi-2":
        return Phi2()
    elif name == "ELYZA-japanese-Llama-2":
        return ELYZAJapaneseLlama2()
    elif name == "Qwen2.5-Coder":
        return QwenCoder()
    else:
        raise ValueError(f"Unknown model: {name}")

def boot_sequence():
    config = load_config()
    selected = config.get("selected_model", "Swallow")
    model = select_model(selected)
    print(f"🌟 起動灯：{selected} モデルを起動します")
    return model
