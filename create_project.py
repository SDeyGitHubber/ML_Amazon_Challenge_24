import os
import subprocess

def create_project_structure(base_dir):
    # Define folder structure
    folders = [
        "dataset", "src", "models", "images", "notebooks", "scripts", "outputs"
    ]
    
    # Create base project directory
    if not os.path.exists(base_dir):
        os.mkdir(base_dir)
    
    # Create all necessary subfolders
    for folder in folders:
        os.makedirs(os.path.join(base_dir, folder), exist_ok=True)
    
    # Create files in the project structure
    files = {
        "README.md": "",
        ".gitignore": "__pycache__/\n*.pyc\nvenv/\n.env\n*.ipynb_checkpoints/\ndataset/\noutputs/",
        "requirements.txt": "opencv-python\npillow\ntesseract\npytesseract\npandas\nnumpy\nscikit-learn\ntorch\ntensorflow\nmatplotlib",
        "src/utils.py": "# Utility functions",
        "src/sanity.py": "# Sanity check script",
        "src/constants.py": "# Constants and configurations",
        "src/test.ipynb": "# Jupyter notebook for testing",
        "scripts/ocr_text_extraction.py": "# OCR-based text extraction",
        "scripts/cnn_extraction.py": "# CNN-based extraction",
        "scripts/evaluate_model.py": "# Model evaluation script",
        "outputs/test_out.csv": "",
    }
    
    # Create each file with predefined content
    for file_path, content in files.items():
        with open(os.path.join(base_dir, file_path), "w") as f:
            f.write(content)
    
    print(f"Project structure created in {base_dir}")

def initialize_git_repo(base_dir):
    # Navigate to the project directory
    os.chdir(base_dir)
    
    # Initialize git repository
    subprocess.run(["git", "init"], check=True)
    print("Git repository initialized.")
    
    # Add all files to git
    subprocess.run(["git", "add", "."], check=True)
    
    # Commit initial files
    subprocess.run(["git", "commit", "-m", "Initial commit with folder structure"], check=True)
    print("Initial commit done.")

if __name__ == "__main__":
    # Define your project directory here
    project_dir = "amazon-ml-challenge-2024"
    
    # Create the folder structure and initialize Git
    create_project_structure(project_dir)
    initialize_git_repo(project_dir)