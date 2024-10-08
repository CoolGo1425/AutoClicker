# Author: Synctic
# License: MIT | Copyright (c) 2022 Synctic
# Version: 1.05

from PIL import Image, ImageTk
from pynput.keyboard import *
from pynput.keyboard import Key, Listener
from pynput import keyboard
import pydirectinput
import sys
import os
import pydirectinput
import customtkinter
import threading
import spinbox as spinbox

autoclick_key = Key.f6
holdm_key = Key.f7

button1 = "Left"
clicktype = "Single"
repeattype = 1


class App(customtkinter.CTk):
    auto = False
    auto1 = False

    WIDTH = 315
    HEIGHT = 440

    global resource

    def resource(relative_path):
        base_path = getattr(sys, "_MEIPASS", os.path.dirname(
            os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)

    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue")

    def __init__(self):
        super().__init__()

        self.title("AutoClicker")
        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")

        self.p1 = ImageTk.PhotoImage(file=resource("../Assets/icon.ico"))
        self.wm_iconbitmap()
        self.iconphoto(False, self.p1)

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame = customtkinter.CTkFrame(master=self)
        self.frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(1, weight=1)
        self.frame.grid_columnconfigure(5, weight=1)

        self.title = customtkinter.CTkLabel(
            master=self.frame, text="AutoClicker", font=("Roboto Medium", -16)
        )
        self.title.grid(row=1, column=1, pady=10)

        self.protocol("WM_DELETE_WINDOW", self.on_close)

        self.start_auto_button = customtkinter.CTkButton(
            master=self.frame,
            text="Start",
            fg_color=("black"),
            font=("Roboto Medium", -16),
            command=self.start_button,
        )
        self.start_auto_button.place(x=80, y=280)

        self.stop_auto_button = customtkinter.CTkButton(
            master=self.frame,
            text="Stop",
            fg_color=("black"),
            font=("Roboto Medium", -16),
            state="disabled",
            command=self.stop_button,
        )
        self.stop_auto_button.place(x=80, y=315)

        self.buttonmenu_var = customtkinter.StringVar(value="Left")

        self.buttonmenu = customtkinter.CTkComboBox(
            master=self.frame,
            font=("Roboto Medium", -14),
            width=115,
            fg_color="black",
            button_color="black",
            variable=self.buttonmenu_var,
            command=self.buttonmenu_event,
            values=["Left", "Middle", "Right"],
        )
        self.buttonmenu.place(x=20, y=90)

        self.buttonmenu.bind("<Return>", lambda e: self.custombutton())

        self.buttontxt = customtkinter.CTkLabel(
            master=self.frame, text="Button:", font=("Roboto Medium", -15)
        )
        self.buttontxt.place(x=46, y=60)

        self.clicktype_var = customtkinter.StringVar(value="Single")

        self.clicktypemenu = customtkinter.CTkOptionMenu(
            master=self.frame,
            font=("Roboto Medium", -14),
            width=115,
            fg_color="black",
            button_color="black",
            variable=self.clicktype_var,
            command=self.clicktype_event,
            values=["Single", "Double", "Triple", "Hold"],
        )
        self.clicktypemenu.place(x=160, y=90)

        self.clicktypetxt = customtkinter.CTkLabel(
            master=self.frame, text="Click Type:", font=("Roboto Medium", -15)
        )
        self.clicktypetxt.place(x=180, y=60)

        self.clickinterval_var = customtkinter.StringVar(
            master=self.frame, value=str(0.01)
        )

        self.clickinterval = customtkinter.CTkEntry(
            master=self.frame,
            font=("Roboto Medium", -14),
            width=80,
            textvariable=self.clickinterval_var,
        )
        self.clickinterval.place(x=110, y=380)

        self.clickintervaltxt = customtkinter.CTkLabel(
            master=self.frame, text="Click interval", font=("Roboto Medium", -14)
        )
        self.clickintervaltxt.place(x=108, y=350)

        self.secondstxt = customtkinter.CTkLabel(
            master=self.frame, text="secs", font=("Roboto Medium", -13), width=10
        )
        self.secondstxt.place(x=195, y=385)

        self.repeat_var = customtkinter.IntVar()
        self.repeat_var.set(value=1)

        self.repeat = customtkinter.CTkRadioButton(
            master=self.frame,
            text="Repeat",
            value=0,
            variable=self.repeat_var,
            command=self.repeat_event,
            font=("Roboto Medium", -13),
            width=20,
            height=20,
        )
        self.repeat.place(x=20, y=140)

        self.repeatstopped = customtkinter.CTkRadioButton(
            master=self.frame,
            text="Repeat until stopped",
            value=1,
            variable=self.repeat_var,
            command=self.repeat_event,
            font=("Roboto Medium", -13),
            width=20,
            height=20,
        )
        self.repeatstopped.place(x=20, y=170)

        self.repeattimes = spinbox.FloatSpinbox(
            master=self.frame, width=105, height=25, step_size=1
        )
        self.repeattimes.place(x=160, y=135)

        self.lis2 = keyboard.Listener(on_press=self.on_press1)
        self.lis2.start()

        self.repeattimes.set(1)
        self.repeatstopped.select()

    def buttonmenu_event(self, choice5):
        global button1
        self.choice5 = choice5

        if self.choice5 == "Left":
            button1 = "Left"
        elif self.choice5 == "Middle":
            button1 = "Middle"
        elif self.choice5 == "Right":
            button1 = "Right"

    def custombutton(self):
        global button1
        button1 = self.buttonmenu_var.get()
        self.frame.focus_set()

    def clicktype_event(self, choice):
        global clicktype

        if choice == "Single":
            clicktype = "Single"
        elif choice == "Double":
            clicktype = "Double"
        elif choice == "Triple":
            clicktype = "Triple"
        elif choice == "Hold":
            clicktype = "Hold"

    def repeat_event(self):
        global repeattype

        if self.repeat_var.get() == 0:
            repeattype = 0
        if self.repeat_var.get() == 1:
            repeattype = 1

    def start_button(self):
        if (
            clicktype == "Single"
            or clicktype == "Double"
            or clicktype == "Triple"
            and not self.pause
        ):
            self.lis2.stop()
            self.pause = False

            self.autoclc = threading.Thread(target=self.autoClick)
            self.autoclc.start()

            self.buttonmenu.configure(state="normal")
            self.buttonmenu.configure(state="disabled")
            self.start_auto_button.configure(state="disabled")
            self.stop_auto_button.configure(state="enabled")
        else:
            if not self.pause:
                self.lis2.stop()
                self.pause = False

                self.autohol = threading.Thread(target=self.autoHold)
                self.autohol.start()

                self.buttonmenu.configure(state="normal")
                self.buttonmenu.configure(state="disabled")
                self.start_auto_button.configure(state="disabled")
                self.stop_auto_button.configure(state="enabled")

    def on_press1(self, key):
        if not self.auto1 and key == autoclick_key:
            self.pause = False
            self.auto1 = True
            self.auto = False
            self.lis2.stop()
            self.start_button()

        if not self.auto and key == holdm_key:
            self.pause = False
            self.lis2.stop()
            self.start_button()
            self.auto1 = True

    def on_press(self, key):
        if self.auto1 and key == autoclick_key:
            self.pause = True
            self.auto1 = False
            self.stop_button()
            self.lis2 = keyboard.Listener(on_press=self.on_press1)
            self.lis2.start()

        if self.auto and key == holdm_key:
            self.pause = True
            self.auto = False
            self.stop_button()
            self.lis2 = keyboard.Listener(on_press=self.on_press1)
            self.lis2.start()

    def autoHold(self):
        self.auto = True
        self.auto1 = False
        self.pause = False

        lis = Listener(on_press=self.on_press)
        lis.start()

        while self.auto:
            if not self.pause:
                if button1 == "Left":
                    pydirectinput.mouseDown(button="left")
                elif button1 == "Middle":
                    pydirectinput.mouseDown(button="middle")
                elif button1 == "Right":
                    pydirectinput.mouseDown(button="right")
                else:
                    pydirectinput.keyDown(keys=self.buttonmenu.get().lower())
                    pydirectinput.PAUSE = self.interval

            if self.pause:
                self.autohol.join()
                break
        lis.stop()

    def autoClick(self):
        self.auto = False
        self.auto1 = True
        self.pause = False

        lis1 = Listener(on_press=self.on_press)
        lis1.start()

        self.interval = float(self.clickinterval.get())
        if repeattype == 1:
            while self.auto1:
                if not self.pause:
                    if clicktype == "Single":
                        if self.buttonmenu.get() == "Left":
                            pydirectinput.click(button="left")
                            pydirectinput.PAUSE = self.interval
                        elif self.buttonmenu.get() == "Middle":
                            pydirectinput.click(button="middle")
                            pydirectinput.PAUSE = self.interval
                        elif self.buttonmenu.get() == "Right":
                            pydirectinput.click(button="right")
                            pydirectinput.PAUSE = self.interval
                        else:
                            pydirectinput.press(
                                keys=self.buttonmenu.get().lower())
                            pydirectinput.PAUSE = self.interval

                    if clicktype == "Double":
                        if button1 == "Left":
                            pydirectinput.doubleClick(button="left")
                            pydirectinput.PAUSE = self.interval
                        elif button1 == "Middle":
                            pydirectinput.doubleClick(button="middle")
                            pydirectinput.PAUSE = self.interval
                        elif button1 == "Right":
                            pydirectinput.doubleClick(button="right")
                            pydirectinput.PAUSE = self.interval
                        else:
                            pydirectinput.press(
                                keys=self.buttonmenu.get().lower())
                            pydirectinput.PAUSE = self.interval

                    if clicktype == "Triple":
                        if button1 == "Left":
                            pydirectinput.tripleClick(button="left")
                            pydirectinput.PAUSE = self.interval
                        elif button1 == "Middle":
                            pydirectinput.tripleClick(button="middle")
                            pydirectinput.PAUSE = self.interval
                        elif button1 == "Right":
                            pydirectinput.tripleClick(button="right")
                            pydirectinput.PAUSE = self.interval
                        else:
                            pydirectinput.press(
                                keys=self.buttonmenu.get().lower())
                            pydirectinput.PAUSE = self.interval
                if self.pause:
                    break
        else:
            for i in range(int(self.repeattimes.get()) + 1):
                if not self.pause:
                    if clicktype == "Single":
                        if self.buttonmenu.get() == "Left":
                            pydirectinput.click(button="left")
                            pydirectinput.PAUSE = self.interval
                        elif self.buttonmenu.get() == "Middle":
                            pydirectinput.click(button="middle")
                            pydirectinput.PAUSE = self.interval
                        elif self.buttonmenu.get() == "Right":
                            pydirectinput.click(button="right")
                            pydirectinput.PAUSE = self.interval
                        else:
                            pydirectinput.press(keys=self.buttonmenu.get())
                            pydirectinput.PAUSE = self.interval

                    if clicktype == "Double":
                        if button1 == "Left":
                            pydirectinput.doubleClick(button="left")
                            pydirectinput.PAUSE = self.interval
                        elif button1 == "Middle":
                            pydirectinput.doubleClick(button="middle")
                            pydirectinput.PAUSE = self.interval
                        elif button1 == "Right":
                            pydirectinput.doubleClick(button="right")
                            pydirectinput.PAUSE = self.interval
                        else:
                            pydirectinput.press(
                                keys=self.buttonmenu.get().lower())
                            pydirectinput.PAUSE = self.interval

                    if clicktype == "Triple":
                        if button1 == "Left":
                            pydirectinput.tripleClick(button="left")
                            pydirectinput.PAUSE = self.interval
                        elif button1 == "Middle":
                            pydirectinput.tripleClick(button="middle")
                            pydirectinput.PAUSE = self.interval
                        elif button1 == "Right":
                            pydirectinput.tripleClick(button="right")
                            pydirectinput.PAUSE = self.interval
                        else:
                            pydirectinput.press(
                                keys=self.buttonmenu.get().lower())
                            pydirectinput.PAUSE = self.interval

                    if i == int(self.repeattimes.get()):
                        self.pause = True

                if self.pause:
                    self.auto1 = False
                    self.stop_button()
                    self.autoclc.join()
                    break
                lis1.stop()

    def stop_button(self):
        self.pause = True

        if clicktype == "Single":
            if button1 == "Left":
                self.auto1 = False
                pydirectinput.mouseUp(button="left")
            elif button1 == "Middle":
                self.auto1 = False
                pydirectinput.mouseUp(button="middle")
            elif button1 == "Right":
                self.auto1 = False
                pydirectinput.mouseUp(button="right")

        if clicktype == "Double":
            if button1 == "Left":
                self.auto1 = False
                pydirectinput.mouseUp(button="left")
            elif button1 == "Middle":
                self.auto1 = False
                pydirectinput.mouseUp(button="middle")
            elif button1 == "Right":
                self.auto1 = False
                pydirectinput.mouseUp(button="right")

        if clicktype == "Triple":
            if button1 == "Left":
                self.auto1 = False
                pydirectinput.mouseUp(button="left")
            elif button1 == "Middle":
                self.auto1 = False
                pydirectinput.mouseUp(button="middle")
            elif button1 == "Right":
                self.auto1 = False
                pydirectinput.mouseUp(button="right")

        if clicktype == "Hold":
            if button1 == "Left":
                self.auto = False
                pydirectinput.mouseUp(button="left")
            elif button1 == "Middle":
                self.auto = False
                pydirectinput.mouseUp(button="middle")
            elif button1 == "Right":
                self.auto = False
                pydirectinput.mouseUp(button="right")
            else:
                pydirectinput.keyUp(button=self.buttonmenu.get().lower())

        self.buttonmenu.configure(state="normal")
        self.start_auto_button.configure(state="enabled")
        self.stop_auto_button.configure(state="disabled")

    def on_close(self, event=0):
        self.destroy()

    def start(self):
        self.mainloop()


if __name__ == "__main__":
    app = App()
    app.attributes("-topmost", True)
    app.resizable(False, False)
    app.update()
    app.start()
