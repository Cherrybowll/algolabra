from pathlib import Path

class FileHelper:
    def __init__(self):
        self._root = Path(".")
        self._create_directories()

    def create_key(self, name: str, key, overwrite: bool):
        print("avain", len(key))
        new_key_path = self._keys / name
        new_key_path.touch(exist_ok=overwrite)
        with new_key_path.open(mode="w") as new_key:
            for part in key:
                new_key.write(str(part) + ";")

    def get_key(self, name: str):
        key_path = self._keys / name
        with key_path.open("r") as got_key:
            key = got_key.read()
            key_parts = key.split(";")[:-1]
            key_parts = [int(part) for part in key_parts]
            print(len(key_parts))
            return key_parts

    def create_message(self, name, message):
        pass

    def check_key_exist(self, name: str):
        key_path = self._keys / name
        return key_path.exists()

    def _create_directories(self):
        self._keys = self._root / "data" / "keys"
        self._messages = self._root / "data" / "messages"

        self._keys.mkdir(parents=True, exist_ok=True)
        self._messages.mkdir(parents=True, exist_ok=True)


if __name__ == "__main__":
    helper =  FileHelper()
    print(helper.root)
    print(helper.root.exists())
    print(helper.fake.exists())
