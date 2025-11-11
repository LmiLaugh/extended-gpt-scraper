thonimport openai
import logging

def process_with_gpt(content, instructions):
    try:
        openai.api_key = instructions['api_key']

        # Call GPT API
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"{instructions['prompt_prefix']} {content}",
            max_tokens=150
        )

        return response.choices[0].text.strip()

    except Exception as e:
        logging.error(f"Error processing with GPT: {e}")
        raise