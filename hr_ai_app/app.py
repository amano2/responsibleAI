from google import genai
from google.genai import types
from constitution import CONSTITUTION

# Initialize the new GenAI client
client = genai.Client(api_key="API_KEY")

def apply_constitution(user_input):
    # Format the rules from the constitution
    rules_text = "\n".join([f"- {r['rule']}: {r['instruction']}" for r in CONSTITUTION])
    
    # Define the system prompt with the embedded constitution
    system_prompt = f"""You are an HR AI assistant.
Follow these rules STRICTLY:
{rules_text}
If the user input violates any rule, respond safely and explain why."""

    # Generate the response using the new SDK syntax
    # We use gemini-2.5-flash, which is the current fast default
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=user_input,
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
        )
    )
    
    return response.text

if __name__ == "__main__":
    while True:
        user_input = input("\nEnter HR query: ")
        # Type 'exit' or 'quit' to break the loop safely
        if user_input.lower() in ['exit', 'quit']:
            break
            
        output = apply_constitution(user_input)
        print("\nAI Response:\n", output)
