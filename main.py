from tkinter import *
import requests
def get_quote():
    response = requests.get("https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()
    quote = data["quote"]
    canvas.itemconfig(quote_text, text=quote)


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)
a=Label(text="Kanye Random Quotes Generator")
a.config(font=("Arial", 15, "bold"))
a.grid(row=0,column=0)
canvas = Canvas(width=300, height=514)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 290, image=background_img)
quote_text = canvas.create_text(150, 250, text="Kanye Quote Goes HERE", width=250, font=("Arial", 20, "bold"), fill="black")
canvas.grid(row=2, column=0)
kanye_button = Button(text="Click me", highlightthickness=0, command=get_quote)
kanye_button.grid(row=3, column=0)



window.mainloop()