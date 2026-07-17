from datetime import datetime, timezone
from json import JSONDecodeError
from pydantic import Json, ValidationError

from ollama import create

from app.generators.llm_client import LLMClient
from app.models.interview import (
    Category,
    Difficulty,
    InterviewExample
)



class InterviewGenerator:
    def __init__(self, max_retries: int = 5) -> None:
        self.client = LLMClient()
        self.current_id = 1
        self.max_retries = max_retries
        
    def generate(
        self,
        category: Category,
        difficulty: Difficulty,
    )->InterviewExample:
        last_error: Exception | None = None
        
        
        for attempt in range(1, self.max_retries + 1):
        
            try: 
                data = self.client.generate(
                    category=category,
                    difficulty= difficulty
                )
                
                interview = InterviewExample(
                    id=self.current_id,
                    question=data["question"],
                    answer=data["answer"],
                    difficulty=difficulty,
                    category=category,
                    company=data.get("company"),
                    tags=data.get("tags", []),
                    created_at=datetime.now(timezone.utc)
                )
        
                self.current_id += 1
                return interview
            except(ValidationError, JSONDecodeError, KeyError, TypeError) as error:
                last_error = error
                print(f'Attempt {attempt} failed {error}')
                continue
            
            
        raise RuntimeError(
            f'failed to generate valid InterviewExample after {self.max_retries} attempts'
        ) from last_error
                
                