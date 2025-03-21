import os

folders = [
    "data",
    "preprocessing",
    "models",
    "federated",
    "recommendation_engine",
    "evaluation",
    "privacy",
    "api",
    "frontend",
    "docs"
]

root_dir = "federated-healthcare-recommender"

# Create root project directory
os.makedirs(root_dir, exist_ok=True)

# Create all subfolders
for folder in folders:
    os.makedirs(os.path.join(root_dir, folder), exist_ok=True)

print("✅ Project structure created successfully!")
