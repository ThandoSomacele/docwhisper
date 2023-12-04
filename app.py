# from openai import OpenAI

from openai import OpenAI

client = OpenAI()

# # Set your OpenAI API key
# openai.api_key = 'your-api-key'

def chat_with_docwhisper(user_input):
    """
    Function to interact with DocWhisper and get AI-powered responses.

    Args:
    - user_input (str): User's input/query.

    Returns:
    - str: AI-generated response.
    """
    # Call OpenAI's ChatGPT for generating response
    response = client.chat.completions.create(
      model="gpt-3.5-turbo",  # Choose the appropriate model
      messages=[
          {"role":"system", "content": "You are a chat interaction called DocWhisper, designed to make document search and interaction as intuitive as seeking advice from a seasoned colleague"},
          {"role":"user", "content": user_input}
          ],
      # temperature=0.7,  # Adjust temperature for response randomness
      # max_tokens=150,  # Control response length
      # stop=None
      )

    # Extract and return AI-generated response
    # ai_response = response['choices'][0]['text'].strip()
    ai_response = response.choices[0].message.content
    return ai_response

# Example conversation loop
print("DocWhisper: Hi there! I'm DocWhisper, your documentation expert. How can I assist you today?")

while True:
    user_input = input("You: ")

    # Exit loop if the user wants to end the conversation
    if user_input.lower() == 'exit':
        print("DocWhisper: Goodbye! If you have more questions, feel free to ask.")
        break

    # Get AI-generated response
    docwhisper_response = chat_with_docwhisper(user_input)

    # Display DocWhisper's response
    print(f"DocWhisper: {docwhisper_response}")
