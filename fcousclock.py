import time
import tkinter as tk

def start_timer(minutes):
    seconds = minutes * 60
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer.set(f"{mins:02d}:{secs:02d}")
        root.update()
        time.sleep(1)
        seconds -= 1

    timer.set("Time's up!")

# 创建主窗口
root = tk.Tk()
root.title("Focus Timer")

# 设置默认时间（以分钟为单位）
default_minutes = 25

# 创建StringVar以更新计时器文本
timer = tk.StringVar()
timer.set(f"{default_minutes:02d}:00")

# 创建标签显示计时器
timer_label = tk.Label(root, textvariable=timer, font=("Helvetica", 48))
timer_label.pack(pady=10)

# 创建开始按钮
start_button = tk.Button(root, text="Start", command=lambda: start_timer(default_minutes))
start_button.pack(pady=10)

# 运行主循环
root.mainloop()
