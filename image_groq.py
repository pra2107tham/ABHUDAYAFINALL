import base64
from groq import Groq
import os
# Load environment variables


# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# Path to your image
image_path = "image/image.jpg"

# Getting the base64 string
base64_image = encode_image(image_path)

client = Groq(api_key="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")


chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "What's in this image?"},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image}",
                    },
                },
            ],
        }
    ],
    model="llama-3.2-11b-vision-preview",
)

print(chat_completion.choices[0].message.content)
def get_text():
    return chat_completion.choices[0].message.content