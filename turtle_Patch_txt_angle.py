# https://stackoverflow.com/questions/72749874/how-to-create-rotated-text-in-pythons-turtle-graphics
# https://stackoverflow.com/a/72749875/7711283
class Patch_txt_angle:
    def RawTurtleDOTwrite(self, arg, move=False, align="left", font=("Arial", 11, "normal"), txt_angle=0):
        if self.undobuffer:
            self.undobuffer.push(["seq"])
            self.undobuffer.cumulate = True
        end = self._write(str(arg), align.lower(), font, txt_angle)
        if move: x, y = self.pos() ; self.setpos(end, y)
        if self.undobuffer: self.undobuffer.cumulate = False
    def RawTurtleDOT_write(self, txt, align, font, txt_angle):
        item, end = self.screen._write(self._position, txt, align, font, self._pencolor, txt_angle)
        self.items.append(item)
        if self.undobuffer: self.undobuffer.push(("wri", item))
        return end
    def TurtleScreenBaseDOT_write(self, pos, txt, align, font, pencolor, txt_angle):
        x, y = pos ; x = x * self.xscale ; y = y * self.yscale
        anchor = {"left":"sw", "center":"s", "right":"se" }
        item = self.cv.create_text(x-1, -y, text = txt, anchor = anchor[align],
            fill = pencolor, font = font, angle = txt_angle)
        x0, y0, x1, y1 = self.cv.bbox(item)
        self.cv.update()
        return item, x1-1
import turtle
turtle.RawTurtle.write         = Patch_txt_angle.RawTurtleDOTwrite
turtle.RawTurtle._write        = Patch_txt_angle.RawTurtleDOT_write
turtle.TurtleScreenBase._write = Patch_txt_angle.TurtleScreenBaseDOT_write

# ======================================================================
if __name__ == "__main__": 
    txt = '𝄖 𝄗 𝄘 𝄙  𝄚 𝄛'
    tt = turtle.Turtle()
    sc = turtle.Screen() ; sc.bgcolor("black")
    for enum_index, txt_angle in enumerate(range(0, 36000, 1125)):
        if (enum_index)%4 == 0: tt.color("green" ); fontsize=10
        if (enum_index)%4 == 1: tt.color("yellow"); fontsize=15
        if (enum_index)%4 == 2: tt.color("red"   ); fontsize=10
        if (enum_index)%4 == 3: tt.color("orange"); fontsize=13
        txt_angle /= 100    
        tt.setheading(txt_angle); tt.forward(100)
        tt.write(txt, font=("Arial", fontsize, "bold"), align="right", txt_angle=txt_angle)
        tt.backward(100)
    from time import sleep; sleep(30)
