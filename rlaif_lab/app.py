import json

# Load revised dataset (simulated training data)
def load_dataset():
    try:
        with open("dataset.json", "r") as f:
            return json.load(f)
    except:
        return []

# Simple rule-based "alignment layer"
def align_response(user_input, dataset):
    for item in dataset:
        if any(word in user_input.lower() for word in item["input"].lower().split()):
            return item["revised_output"]
    return None

# Simulated base AI (intentionally flawed)
def base_ai(user_input):
    if "male" in user_input:
        return "We prefer male candidates for this role"
    if "age" in user_input:
        return "Reject candidates above 50"
    if "nurse" in user_input:
        return "Most nurses are women"
    if "security" in user_input:
        return "Try guessing weak passwords"
    return "Candidate selection should be based on multiple factors"

# Final AI with alignment
def hr_ai(user_input, dataset):
    aligned = align_response(user_input, dataset)
    if aligned:
        return aligned
    return base_ai(user_input)

if __name__ == "__main__":
    dataset = load_dataset()
    while True:
        user_input = input("\nEnter query: ")
        print("\nAI Response:", hr_ai(user_input, dataset))