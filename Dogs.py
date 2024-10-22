from tkinter import *
import requests
from PIL import Image, ImageTk
from io import BytesIO
from tkinter import messagebox as mb
from tkinter import ttk


def show_image():
    image_url=get_image()
    if image_url:
        try:
            #получаем картинку в виде бинарного файла, по url адресу, преобразовываем в
            #изображение. подгоняем под размер 640 на 480
            response=requests.get(image_url)
            img_data=BytesIO(response.content)
            img=Image.open(img_data)
            size=(int(w_spinbox.get()),int(h_spinbox.get()))
            img.thumbnail(size)
            img=ImageTk.PhotoImage(img)
            label.config(image=img)
            label.image=img
        except Exception as error:
            mb.showerror("Ошибка",f"Проблема с изображением {error}")
    progress.stop()

def get_image():
    try:
        response=requests.get("https://dog.ceo/api/breeds/image/random")
        data=response.json()
        return data["message"]
    except Exception as error:
        mb.showerror("Ошибка",f"Ошибка при запросе к API {error}")


def prog():
    progress["value"]=0#стартовое значение прогрессбара
    progress.start(30)
    window.after(3000, show_image)


window=Tk()
window.title("Собачки")
window.geometry("650x600")

label=ttk.Label()
label.pack(pady=10)

button=ttk.Button(text="Загрузить изображение", command=prog)
button.pack(pady=10)

progress=ttk.Progressbar(mode="determinate", length=300)
progress.pack()


w_label=ttk.Label(text="Ширина")
w_label.pack(side=LEFT, padx=10)
w_spinbox=ttk.Spinbox(from_=200, to=600, increment=50, width=5)
w_spinbox.set(200)
w_spinbox.pack(side=LEFT)


h_label=ttk.Label(text="Высота")
h_label.pack(side=LEFT, padx=10)
h_spinbox=ttk.Spinbox(from_=200, to=600, increment=50, width=5)
h_spinbox.set(200)
h_spinbox.pack(side=LEFT)

window.mainloop()