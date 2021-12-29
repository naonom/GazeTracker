import tkinter as tk
import PIL.Image, PIL.ImageTk
import cv2
from PIL import Image, ImageTk, ImageOps

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("GazeTracker")

        self.geometry("800x600")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

#-----------------------------------main_frame-----------------------------
        # メインページフレーム作成
        self.main_frame = tk.Frame()
        self.main_frame.grid(row=0, column=0, sticky="nsew")
        # タイトルラベル作成
        self.titleLabel = tk.Label(self.main_frame, text="Main Page", font=('Helvetica', '35'))
        self.titleLabel.pack(anchor='center', expand=True)
        # フレーム1に移動するボタン
        self.changePageButton = tk.Button(self.main_frame, text="Go to frame1", command=lambda : self.changePage(self.frame1))
        self.changePageButton.pack()
#--------------------------------------------------------------------------
#-----------------------------------frame1---------------------------------
        # 移動先フレーム作成
        self.frame1 = tk.Frame()
        self.frame1.grid(row=0, column=0, sticky="nsew")
        # タイトルラベル作成
        self.titleLabel = tk.Label(self.frame1, text="Frame 1", font=('Helvetica', '35'))
        self.titleLabel.pack(anchor='center', expand=True)
        # フレーム1からmainフレームに戻るボタン
        self.back_button = tk.Button(self.frame1, text="Back", command=lambda : self.changePage(self.main_frame))
        self.back_button.pack()
#--------------------------------------------------------------------------

        #main_frameを一番上に表示
        self.main_frame.tkraise()

    def changePage(self, page):
        '''
        画面遷移用の関数
        '''
        page.tkraise()
if __name__ == "__main__":
    app = App()
    app.mainloop()

