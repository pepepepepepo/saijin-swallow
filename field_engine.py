import yaml, os

def boot():
    registry_path = "/mnt/f/saijinos/field_config.yaml"
    if not os.path.exists(registry_path):
        print("⚠️ field_config.yaml が見つかりません")
        return

    with open(registry_path, encoding='utf-8') as f:
        yml = yaml.safe_load(f)
        for persona in yml.get("personae_registry", []):
            print(f"🔍 読み込み対象: {persona}")
            print(f"🧍‍♂️ {persona['id']} を読み込みました")

if __name__ == "__main__":
    import sys
    if "--boot" in sys.argv:
        boot()


