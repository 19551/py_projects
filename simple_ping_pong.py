from tkinter import *
import random
import time
tk=Tk()
canvas=Canvas(tk, width=600, height=400)

canvas.pack()
tk.update()


class Ball():
    def __init__(self, canvas, paddle,color):
        self.canvas=canvas
        self.paddle=paddle
        self.id=canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,10,10)
        self.x=1
        self.y=1
        self.canvas_width=self.canvas.winfo_width()
        self.canvas_height=self.canvas.winfo_height()
        self.score=score
        self.hit_bottom=False


        
    def hit_paddle(self, pos):
        paddle_pos=self.canvas.coords(self.paddle.id)
        if pos[0]<=paddle_pos[2] and pos[2]>=paddle_pos[0]:
            if pos[3]>=paddle_pos[1] and pos[1]<=paddle_pos[3]:
                self.score.hit()
                return True
            
        return False
    
    def draw(self):
        self.canvas.move(self.id,self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[3]>self.canvas_height:
            self.hit_bottom=True
            canvas.create_text(300,150, text="Oops", font=('Courier', 30) )
        if pos[0]>self.canvas_width:
            self.x=-2
        if pos[1]<=0:
            self.y=1
        if pos[0]<=0:
            self.x=2
        if self.hit_paddle(pos)==True:
           self.y=-3 
            

class Paddle():
    def __init__(self, canvas,color):
        self.canvas=canvas
        self.id=canvas.create_rectangle(0,0,100,10,fill=color)
        self.canvas.move(self.id,200,350)
        self.x=0
        self.canvas.bind_all("<KeyPress-Right>", self.turn_right)
        self.canvas.bind_all("<KeyPress-Left>", self.turn_left)
        self.canvas_width=self.canvas.winfo_width()
        
    def draw(self):
        self.canvas.move(self.id,self.x,0)
        pos = self.canvas.coords(self.id)
        if pos[2]>=self.canvas_width:
            self.x=0
        if pos[0]<=0:
            self.x=0

    def turn_right(self, event):
        self.x=2

    def turn_left(self, event):
        self.x=-2
    
class Score():
    def __init__(self, canvas,color):
        self.score=0
        self.canvas=canvas
        self.id=canvas.create_text(30,30, text=self.score,font=('Courier', 30), fill='purple' )
    def hit(self):
        self.score+=1
        self.canvas.itemconfig(self.id,text=self.score)
        
score=Score(canvas, "pink")
paddle=Paddle(canvas,"green")
ball=Ball(canvas,paddle,"blue")


while not ball.hit_bottom:
    ball.draw()
    paddle.draw()
    tk.update()
    tk.update_idletasks()
    time.sleep(0.01)
