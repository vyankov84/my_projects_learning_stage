from tkinter import *
from tkinter import scrolledtext
import groq

# Initialize Groq API client
client = groq.Client(api_key="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")  # Replace with your actual API key

# Function to get AI response from Groq API
def get_ai_response(user_input):
    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": user_input}]
        )
        return response.choices[0].message.content  # Corrected access
    except Exception as e:
        return f"Error: {e}"


def search():
    query = text_input.get("1.0", "end-1c").strip()  # Get input text

    if query:
        output_text.delete("1.0", END)  # Clear previous output
        output_text.insert(END, f"You searched for: {query}")  # Display search term
        window.update() # Force UI update before calling API

        response = get_ai_response(query)

        output_text.delete("1.0", END)
        output_text.insert(END, f"AI: {response}")

window = Tk()
window.title("AI groq search")
window.geometry('800x700')
window.config(background='black')

# Insert widget dialog box = search box
text_input = Text(window, height=3, width=60, background='white', font=('Calibri', 14))
text_input.place(relx = 0.5, rely = 0.8, anchor = 'center')
text_input.insert("1.0", "Question: ")


# Insert widget search button
btn = Button(window, text = 'Search!', command = search)
btn.place(relx=0.5, rely=0.9, anchor='center')

# Insert widget output search dialog box
output_text = scrolledtext.ScrolledText(window, wrap=WORD, height=20, width=70, background='white', font=('Calibri', 14))
output_text.place(relx = 0.5, rely = 0.7, anchor = 's')

window.mainloop()