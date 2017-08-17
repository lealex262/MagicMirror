from Tkinter import *
from time import sleep
import camera_functions
import multiprocessing
import detection

class FullscreenWindow:

    def __init__(self):
        #Settings
        self.tk = Tk()
        self.tk.configure(background='black')
        self.topFrame = Frame(self.tk, background='black')
        self.bottomFrame = Frame(self.tk, background='black')
        self.topFrame.pack(side=TOP, fill=BOTH, expand=YES)
        self.bottomFrame.pack(side=BOTTOM, fill=BOTH, expand=YES)
        self.state = False
        self.tk.bind("<F11>", self.toggle_fullscreen)
        self.tk.bind("<Escape>", self.end_fullscreen)
        self.label = Label(self.tk, background="black", foreground="white", text="", width=10)
        self.label.pack()

    def toggle_fullscreen(self, event=None):
        self.state = not self.state
        self.tk.attributes("-fullscreen", self.state)
        return "break"

    def end_fullscreen(self, event=None):
        self.state = False
        self.tk.attributes("-fullscreen", False)
        return "break"

    def countdown(self, remaining=None):
        print remaining
        if remaining is not None:
            self.remaining = remaining
        if self.remaining <= 0:
            self.label.configure(text="Say cheese!")
            self.tk.update()
            camera_functions.take_image()
            self.label.configure(text="")
            self.tk.update()
        else:
            self.label.configure(text="%d" % self.remaining)
            self.tk.update()
            sleep(1)
            self.countdown(self.remaining - 1)

def mainloop(queue, event):
    w = FullscreenWindow()
    while True:
        if queue.qsize() > 0:
            queue.get()
            w.countdown(5)
            event.set()
            
if __name__ == '__main__':
    camera_functions.scheduler_setup()
    queue = multiprocessing.Queue()
    event = multiprocessing.Event()
    process = multiprocessing.Process(target=detection.detect_fist, args=(event, queue))
    process.start()

    mainloop(queue, event)