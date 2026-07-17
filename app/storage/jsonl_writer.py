import json
from pathlib import Path

from app.models.interview import InterviewExample


class JSONLWriter:
    def __init__(self, output_path: str) -> None:
        self.output_path = Path(output_path)
        #if directory dont exist, create it, if it does dont throw error
        self.output_path.parent.mkdir(parents=True, exist_ok=True)
        
    def write(self, interview: InterviewExample) -> None:
        with self.output_path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(interview.model_dump(mode="json"))) #dumps: json string, model_dump: dict, mode: json friendly
            f.write("\n")