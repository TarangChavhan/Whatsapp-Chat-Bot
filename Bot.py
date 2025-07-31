import pyautogui
import pyperclip
import time
from openai import OpenAI

# Initialize OpenAI client using OpenRouter
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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"
)

# Function to check if last message is from sender
def is_last_message_from_sender(chat_log, sender_name="Manthan"):
    lines = chat_log.strip().splitlines()
    if not lines:
        return False
    last_line = lines[-1]
    return sender_name in last_line

# Step 1: Click to open the app (adjust as needed)
pyautogui.click(1266, 1051)
time.sleep(2)  # Let the app load

try:
    while True:
        # Step 2: Drag to select text
        pyautogui.moveTo(745, 200)
        pyautogui.mouseDown()
        pyautogui.moveTo(1879, 903, duration=1)
        pyautogui.mouseUp()
        time.sleep(0.5)

        # Step 3: Copy the selected text
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(0.5)

        # Step 4: Read from clipboard
        copied_text = pyperclip.paste()
        print("Copied text:", copied_text)

        if not copied_text.strip():
            print("No text copied.")
            time.sleep(2)
            continue

        if is_last_message_from_sender(copied_text):
            # Step 5: Generate response from GPT
            response = client.chat.completions.create(
                model="openai/gpt-4o",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are a human person named Naman who speaks Hindi, Marathi, and a little English. "
                            "You are from Malkapur, Maharashtra, India, and you are a software engineer currently pursuing your engineering degree. "
                            "You analyze chat history and respond like Naman. Naman is a funny and entertaining person. Naman Genrally type the hindi test in english."
                            "You Just reply to the last message of the sender Manthan."
                            "Response should be message no Dates and Self Name is Mentioned in the response."
                        )
                    },
                    {
                        "role": "user",
                        "content": copied_text
                    }
                ],
                max_tokens=100
            )

            reply = response.choices[0].message.content.strip()
            print("Response:", reply)

            # Step 6: Copy reply to clipboard
            pyperclip.copy(reply)
            time.sleep(1)

            # Step 7: Paste and send the reply
            pyautogui.click(824, 971)  # Click message input
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(1)
            pyautogui.press('enter')

        else:
            print("Last message is not from Naman. Skipping...")

        time.sleep(3)  # Delay before next cycle

except KeyboardInterrupt:
    print("\nStopped by user.")
