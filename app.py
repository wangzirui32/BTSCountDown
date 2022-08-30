import datetime
import tkinter as tk
from PIL import Image, ImageTk

# 开学时间 Back to school = BTS
BTS_time = "2022/08/31 8:00:00"

# 将时间转为datetime对象
BTS_datetime = datetime.datetime.strptime(BTS_time, "%Y/%m/%d %H:%M:%S")

class Window(tk.Tk):
    def __init__(self):
        super().__init__()

        # 基本窗体设置
        self.title("开学倒计时")
        self.geometry("800x400") # 窗体大小

        # 字体类别 大小设置
        # 注意：这里使用的是Windows 10系统的自带字体
        self.title_label_font = ("SimHei", 45)  # 45大小
        self.time_label_font = ("SimHei", 30)   # 30大小

        self.canvas = tk.Canvas(self, width=800, height=400)  # 创建长800，高400的画布
        self.photo = ImageTk.PhotoImage(Image.open("bg.jpg").resize((800, 400)))  # 背景图
        self.canvas.create_image(400, 200, image=self.photo)    # 在(400, 200)处绘制背景图

        self.show_time()   # 显示时间

    def show_time(self):
        self.canvas.delete("text")  # 删除tag为text的文本
        self.canvas.create_text(400,  # 文字生成在 330, 40
                                40, 
                                text="开学倒计时",
                                font=self.title_label_font,
                                fill="lightblue") # 字体颜色亮蓝色

        # 获取时间差
        now_time = datetime.datetime.now()
        minus_time = BTS_datetime-now_time         # 计算时间
        day    = datetime.timedelta(days=int(minus_time.days))  # 天数

        hour   = datetime.timedelta(hours=int((minus_time-day).seconds / 3600))  # 小时
        minute = datetime.timedelta(minutes=int((minus_time-day-hour).seconds / 60))  # 分钟
        seconds = datetime.timedelta(seconds=int((minus_time-day-hour-minute).seconds))  # 秒数
        # 注：以上都是时间差对象
        
        minus_time = "{} 天 {} 时 {} 分 {} 秒".format(int(day.days),   # 根据秒数计算时间
                                                     int(hour.seconds/3600),
                                                     int(minute.seconds/60),
                                                     int(seconds.seconds))

        self.canvas.create_text(400,
                                100,
                                text=minus_time,
                                font=self.time_label_font,
                                fill="blue",
                                tag="text")  # tag（标签）设定为text 防止删除标题提

        self.canvas.pack()   # 显示画布
        self.after(1000, self.show_time)   # 每隔1000毫秒（1秒）刷新一次时间显示

if __name__ == "__main__":
    # 运行代码
    app = Window()
    app.mainloop()
