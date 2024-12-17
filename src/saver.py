import json
from pathlib import Path


class JSONSaver:
    """Класс для сохранения информации в файл."""

    def save_to(self, data: list, filename: str) -> None:
        """Метод сохранения информации в файл."""
        BASE_DIR = Path(__file__).resolve().parent.parent
        filename = str(BASE_DIR / "data" / filename)
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False)
