from tkinter import *
from ui import UI
from PIL import Image, ImageTk

count = 5
after_id = None


# ----------------------------- Key pressed -----------------------------------
def key_pressed(key):
    global count, after_id
    if after_id is not None:
        window.after_cancel(after_id)
    count = 5
    update_timer()


# --------------------------------- Update timer --------------------------------
def update_timer():
    global after_id, count
    ui.time_label.config(text=count)
    if count > 0:
        count -= 1
        after_id = window.after(1000, update_timer)
    else:
        reset()


# --------------------------------- reset ---------------------------------------
def reset():
    global count, after_id
    window.after_cancel(after_id)
    count = 5
    ui.time_label.config(text=count)
    ui.text_entry.delete("1.0", END)


window = Tk()
window.title("Disappearing Text Writing")
window.config(padx=100, pady=50)

background_image = Image.open("bg.png")
background_photo = ImageTk.PhotoImage(background_image)

background_label = Label(window, image=background_photo)
background_label.place(x=-110, y=-70)

ui = UI()
ui.place_title_label(background_photo)
ui.place_time_label_info(background_photo)
ui.place_time_label(background_photo)
ui.place_text_entry()
ui.text_entry.focus()

ui.text_entry.bind("<Key>", key_pressed)

window.mainloop()
