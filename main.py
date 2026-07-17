from app.models.interview import (
    InterviewExample,
    Difficulty,
    Category,
)
from app.generators.interview_generator import InterviewGenerator
from rich import print
from app.storage.jsonl_writer import JSONLWriter
from app.config import TARGET_DATASET_SIZE

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

for _ in range(10):
    result = generator.generate_random()
    writer.write(result)

print("saved")


