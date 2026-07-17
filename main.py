from app.generators.prompt_builder import PromptBuilder
from app.models.interview import (
    InterviewExample,
    Difficulty,
    Category,
)
from app.generators.llm_client import LLMClient
from app.generators.interview_generator import InterviewGenerator
from rich import print

example = InterviewExample(
    id=1,
    question="What is a binary tree?",
    answer="A binary tree is something",
    difficulty=Difficulty.EASY,
    category=Category.TREES,
    company="Google",
    tags=["Binary trees", "design thinking"],
)

response = InterviewGenerator()

for i in range(100):
    print(response.generate(Category.BEHAVIORAL, Difficulty.MEDIUM))
    print("="*100)
