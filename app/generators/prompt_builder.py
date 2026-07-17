from app.models.interview import (
    Category,
    Difficulty,
)


class PromptBuilder:
    @staticmethod
    def build(
        category: Category,
        difficulty: Difficulty,
    ) -> str:
        return f""" 
    You are a Senior Software Engineer creating training data for an AI Interview Coach.

Generate exactly ONE interview example.

Requirements:
- Category: {category.value}
- Difficulty: {difficulty.value}
- The question should be realistic.
- The answer should be concise, technically correct, and interview-quality.
- Return ONLY valid JSON.

JSON Schema:
{{
    "question": "...",
    "answer": "...",
    "difficulty": "{difficulty.value}",
    "category": "{category.value}",
    "company": null,
    "tags": ["tag1", "tag2"]
}}
    
    """
