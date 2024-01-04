import tkinter as tk
import time

def tick(time_label):
    # 获取当前的系统时间
    current_time = time.strftime('%H:%M:%S')
    
    # 更新时钟显示的时间
    time_label.config(text=current_time)
    
    # 每隔200毫秒调用函数自身获取时间（需要调整intervals可以自己更改）
    time_label.after(200, tick, time_label)

def main():
    # 创建 Tkinter 窗口
    root = tk.Tk()
    root.title("实时同步时钟")
    
    # 创建时间显示标签
    time_label = tk.Label(root, font=('Helvetica', 48), fg='black')
    time_label.pack(anchor='center')
    
    # 开始时钟循环
    tick(time_label)
    
    # 启动 GUI 程序
    root.mainloop()

if __name__ == "__main__":
    main()