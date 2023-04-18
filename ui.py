import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfiles
from PIL import Image, ImageTk, ImageFont, ImageDraw


class App:

    def __init__(self):
        self.images_links = []
        self.entry = ""
        self.watermark_button = ""
        self.save_image = ""
        self.text = ""
        self.text_for_image = ""
        self.entry_label = ""
        self.size_label = ""
        self.color_label = ""
        self.position_label = ""
        self.options_size = ""
        self.options_color = ""
        self.options_position = ""
        self.variable_size = ""
        self.variable_color = ""
        self.variable_position = ""
        self.images_label = ""
        self.window = tk.Tk()
        self.window.resizable(0, 0)
        self.f1 = tk.Frame(self.window, bg="#645cbb")
        self.f2 = tk.Frame(self.window, bg="#645cbb")
        self.f3 = tk.Frame(self.window, bg="#645cbb")
        self.f4 = tk.Frame(self.window, bg="#645cbb")
        self.window.title("Watermark")
        # self.window.rowconfigure(0, weight=1)
        # self.window.columnconfigure(0, weight=1)
        self.window.config(bg="#BFACE2", pady=50, padx=50)
        self.canvas = ""
        self.save_button_image = tk.PhotoImage(file="./app_imgs/button_save-image.png")
        self.put_button_image = tk.PhotoImage(file="./app_imgs/button_put-watermark.png")

        self.upload_button_image = tk.PhotoImage(file="./app_imgs/button_upload-image.png")
        self.upload_button = tk.Button(command=self.open_file,
                                       image=self.upload_button_image,
                                       bg="#BFACE2",
                                       highlightthickness=0,
                                       border=0,
                                       activebackground="#BFACE2")
        self.upload_button.grid(column=0,
                                row=0,
                                columnspan=3)

        self.window.mainloop()

    def open_file(self):

        self.images_links = None
        self.images_links = askopenfiles(mode="r", filetypes=[("Image Files", "*jpg"), ("Image Files", "*png")])
        if self.images_links:
            if self.images_label:
                self.images_label.grid_forget()

            # Canvas create
            self.canvas = tk.Canvas(self.window,
                                    width=0,
                                    height=0,
                                    borderwidth=0,
                                    background="#BFACE2",
                                    highlightbackground="#BFACE2",
                                    highlightthickness=0)

            self.canvas.grid(column=0,
                             row=1,
                             columnspan=1,
                             rowspan=3,
                             padx=25,
                             pady=25)

            # destroy frame's widgets
            for widgets in self.f1.winfo_children():
                widgets.destroy()
            for widgets in self.f2.winfo_children():
                widgets.destroy()
            for widgets in self.f3.winfo_children():
                widgets.destroy()
            for widgets in self.f4.winfo_children():
                widgets.destroy()
            self.text = ""

            print(self.images_links)
            print(self.images_links[0].name)
            img = Image.open(self.images_links[0].name)
            print(img.size)
            resize_rate = int(img.size[0] / 350)
            # self.canvas.config(width=img.size[0] / resize_rate,
            #                    height=img.size[1] / resize_rate)
            resized_img = img.resize((int(img.size[0] / resize_rate), int(img.size[1] / resize_rate)), Image.LANCZOS)
            self.canvas.config(width=resized_img.size[0],
                               height=resized_img.size[1])
            print(resized_img.size)
            print(self.canvas.winfo_height())
            show_img = ImageTk.PhotoImage(resized_img)
            self.window.img = show_img
            # image_ = tk.PhotoImage(file=image.name)
            self.canvas.create_image(int((img.size[0] / resize_rate) / 2), int((img.size[1] / resize_rate) / 2),
                                     image=self.window.img,
                                     anchor="center")
            if len(self.images_links) > 1:
                self.images_label = tk.Label(self.window,
                                             text=f"{len(self.images_links) - 1} "
                                                  f"more images will be watermarked",
                                             fg="black")
                self.images_label.grid(column=0,
                                       row=3)

            # Text
            self.f1.grid(column=1,
                         row=1,
                         padx=5,
                         )
            self.entry_label = tk.Label(self.f1, text="Text: ",
                                        fg="#ebc7e6",
                                        borderwidth=8,
                                        bg="#645cbb",
                                        font=("MS Sans Serif", 10, "bold"))

            self.entry_label.pack()
            self.entry = tk.Entry(self.f1, width=17)

            self.entry.pack()

            # Size
            options_size = [
                1,
                2,
                3
            ]
            self.f2.grid(column=2,
                         row=1)
            self.size_label = tk.Label(self.f2, text="Size: ",
                                       bg="#645cbb",
                                       fg="#ebc7e6",
                                       font=("MS Sans Serif", 10, "bold")
                                       )
            self.size_label.pack()
            self.variable_size = tk.StringVar(self.f2)
            self.variable_size.set(options_size[0])
            self.options_size = tk.OptionMenu(self.f2, self.variable_size, *options_size)
            self.options_size.config(width=10)
            self.options_size.pack()

            # Color
            options_color = [
                "white",
                "red",
                "black"
            ]
            self.f3.grid(column=1,
                         row=2)
            self.color_label = tk.Label(self.f3, text="Color: ",
                                        bg="#645cbb",
                                        fg="#ebc7e6",
                                        font=("MS Sans Serif", 10, "bold")
                                        )
            self.color_label.pack()
            self.variable_color = tk.StringVar(self.f3)
            self.variable_color.set(options_color[0])
            self.options_color = tk.OptionMenu(self.f3, self.variable_color, *options_color)
            self.options_color.config(width=10)
            self.options_color.pack()

            # Position
            options_position = [
                "center",
                "left-up",
                "right-up"
            ]
            self.f4.grid(column=2,
                         row=2)
            self.position_label = tk.Label(self.f4, text="Position: ",
                                           bg="#645cbb",
                                           fg="#ebc7e6",
                                           font=("MS Sans Serif", 10, "bold"))
            self.position_label.pack()
            self.variable_position = tk.StringVar(self.f4)
            self.variable_position.set(options_position[0])
            self.options_position = tk.OptionMenu(self.f4, self.variable_position, *options_position)
            self.options_position.config(width=10)
            self.options_position.pack()

            self.watermark_button = tk.Button(image=self.put_button_image,
                                              command=self.watermark,
                                              bg="#BFACE2",
                                              highlightthickness=0,
                                              border=0,
                                              activebackground="#BFACE2"
                                              )
            self.watermark_button.grid(column=1,
                                       row=3,
                                       columnspan=2)
            self.save_image = tk.Button(image=self.save_button_image,
                                        command=self.save_image_f,
                                        bg="#BFACE2",
                                        highlightthickness=0,
                                        border=0,
                                        activebackground="#BFACE2")
            self.save_image.grid(column=0,
                                 row=4,
                                 columnspan=3,
                                 pady=25
                                 )

    def watermark(self):
        print(self.entry.get())
        if not self.text:
            # position of the text
            if self.variable_position.get() == "center":
                self.text = self.canvas.create_text(int(self.canvas.winfo_width() / 2),
                                                    int(self.canvas.winfo_height() / 2),
                                                    fill=self.variable_color.get(),
                                                    text=self.entry.get(),
                                                    anchor="center",
                                                    font=("Arial", 12 * int(self.variable_size.get()))
                                                    )
            elif self.variable_position.get() == "left-up":
                self.text = self.canvas.create_text(10,
                                                    10,
                                                    fill=self.variable_color.get(),
                                                    text=self.entry.get(),
                                                    anchor="nw",
                                                    font=("Arial", 12 * int(self.variable_size.get()))
                                                    )
            elif self.variable_position.get() == "right-up":
                self.text = self.canvas.create_text(self.canvas.winfo_width() - 10,
                                                    10,
                                                    fill=self.variable_color.get(),
                                                    text=self.entry.get(),
                                                    anchor="ne",
                                                    font=("Arial", 12 * int(self.variable_size.get()))
                                                    )
            print(f"Size is: {self.variable_size.get()}")
        else:
            if self.variable_position.get() == "center":
                self.canvas.itemconfig(self.text,
                                       text=self.entry.get(),
                                       fill=self.variable_color.get(),
                                       anchor="center",
                                       font=("Arial", 12 * int(self.variable_size.get())))
                self.canvas.coords(self.text, int(self.canvas.winfo_width() / 2),
                                   int(self.canvas.winfo_height() / 2))
            elif self.variable_position.get() == "left-up":
                self.canvas.itemconfig(self.text,
                                       text=self.entry.get(),
                                       fill=self.variable_color.get(),
                                       anchor="nw",
                                       font=("Arial", 12 * int(self.variable_size.get())))
                self.canvas.coords(self.text, 10, 10)
            elif self.variable_position.get() == "right-up":
                self.canvas.itemconfig(self.text,
                                       text=self.entry.get(),
                                       fill=self.variable_color.get(),
                                       anchor="ne",
                                       font=("Arial", 12 * int(self.variable_size.get())))
                self.canvas.coords(self.text, self.canvas.winfo_width() - 10, 10)
            print(f"Size is: {self.variable_size.get()}")
        self.text_for_image = self.entry.get()

    def save_image_f(self):
        if self.text:
            for num in range(len(self.images_links)):
                image = Image.open(self.images_links[num].name)
                name = self.images_links[num].name.split("/")[-1]
                print(f"Image name: {name}")

                draw = ImageDraw.Draw(image)
                coef = image.size[0] / 300
                font = ImageFont.truetype("arial.ttf", size=int((coef * 10) * int(self.variable_size.get())))
                w, h = font.getsize(self.text_for_image)
                print(f"Size of the text: {w} - wide and {h} - height")
                if self.variable_position.get() == "center":
                    x = int((image.size[0] - w) / 2)
                    y = int((image.size[1] - h) / 2)
                elif self.variable_position.get() == "left-up":
                    x = int(10 * coef)
                    y = int(10 * coef)
                elif self.variable_position.get() == "right-up":
                    x = int(image.size[0] - w - (10 * coef))
                    y = int(10 * coef)

                # Color
                if self.variable_color.get() == "white":
                    color = (255, 255, 255)
                elif self.variable_color.get() == "black":
                    color = (0, 0, 0)
                elif self.variable_color.get() == "red":
                    color = (255, 0, 0)

                draw.text((x, y),
                          self.text_for_image,
                          fill=color,
                          font=font,)
                image.save(f'./images/wm_{name}')
        else:
            messagebox.showerror(title="Error", message="Put watermark first.")