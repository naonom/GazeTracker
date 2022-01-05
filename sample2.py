import tkinter as tk
import cv2
import PIL.Image, PIL.ImageTk
from PIL import Image, ImageTk, ImageOps

import gazetracker as gt

class Application(tk.Frame):
        def __init__(self, master=None):
                super().__init__(master)
                self.master.geometry("700x400+50+50")
                self.master.title("OpenCV 動画表示")
        
                #動画ファイルの読み込み
                self.cap = cv2.VideoCapture(1)
                #プロパティ
                self.width = self.cap.get( cv2.CAP_PROP_FRAME_WIDTH)
                self.height = self.cap.get( cv2.CAP_PROP_FRAME_HEIGHT)
                self.fps = self.cap.get(cv2.CAP_PROP_FPS)
                self.frame_num = self.cap.get(cv2.CAP_PROP_FRAME_COUNT)
                self.time = self.frame_num / self.fps
        
                self.create_frame()
                self.create_widget()
                self.delay = 10
                self.play_video()
        
        def create_frame(self):
                #フレームの作成
                self.frame1 = tk.Frame(self.master, width=600, height=350, bg="#E6E6E6")
                self.frame1.place(x=0, y=0)
                self.frame2 = tk.Frame(self.master, width=600, height=50, bg="#E6E6E6")
                self.frame2.place(x=0, y=350)
                self.frame3 = tk.Frame(self.master, width=600, height=400, bg="#E6E6E6")
                self.frame3.place(x=600, y=0)
                # Canvasの作成
                self.canvas = tk.Canvas(self.frame1, width=600, height=350,)
                # Canvasを配置
                self.canvas.pack()

        def create_widget(self):
                #Labelの生成
                l_property = tk.Label(self.frame3,text="プロパティ", relief="flat")
                l_property.grid(row=0, column=0, sticky = tk.W)
                l_width = tk.Label(self.frame3,text="width: "+str(int(self.width)), relief="flat")
                l_width.grid(row=1, column=0, sticky = tk.W)
                l_height = tk.Label(self.frame3,text="height: "+str(int(self.height)), relief="flat")
                l_height.grid(row=2, column=0, sticky = tk.W)
                l_fps = tk.Label(self.frame3,text="fps: "+str(int(self.fps)), relief="flat")
                l_fps.grid(row=3, column=0, sticky = tk.W)
                l_time = tk.Label(self.frame3,text="time: "+str(int(self.time))+"sec", relief="flat")
                l_time.grid(row=4, column=0, sticky = tk.W)
        
        def play_video(self):
                #動画をリサイズしてキャンバスに表示
                ret, frame = self.cap.read()
                self.current_frame = self.cap.get(cv2.CAP_PROP_POS_FRAMES)
                l_time = tk.Label(self.frame3,text="frame: "+str(int(self.current_frame)), relief="flat")
                l_time.grid(row=5, column=0, sticky = tk.W)

                frame = cv2.resize(frame, dsize=(600, int(600*int(self.height)/int(self.width))))
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)        
                self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
                self.canvas.create_image(0,0, image= self.photo, anchor = tk.NW)
                #alter関数 10ms後に関数を実行
                self.master.after(self.delay, self.play_video)
        

def main():
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop() 

if __name__ == "__main__":
    main()