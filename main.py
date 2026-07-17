from app.generators.prompt_builder import PromptBuilder
from app.models.interview import (
    InterviewExample,
    Difficulty,
    Category,
)
from app.generators.llm_client import LLMClient
from app.generators.interview_generator import InterviewGenerator
from rich import print

from app.storage.jsonl_writer import JSONLWriter

response = InterviewGenerator()
writer = JSONLWriter("datasets/raw/interview.jsonl")

example = InterviewExample(
    id=1,
    question="What is a binary tree?",
    answer="A binary tree is something",
    difficulty=Difficulty.EASY,
    category=Category.TREES,
    company="Google",
    tags=["Binary trees", "design thinking"],
)

generator = InterviewGenerator()
writer = JSONLWriter("datasets/raw/interviews.jsonl")


result = generator.generate(
    Category.TREES,
    Difficulty.MEDIUM,
)

writer.write(result)

print("saved")


