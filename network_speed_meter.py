import psutil
import tkinter as tk
import time
import ctypes

def get_network_speed():
    net_io = psutil.net_io_counters()
    return net_io.bytes_sent, net_io.bytes_recv

def format_speed(speed):
    if speed > 1024 * 1024:
        return f"{speed / (1024 * 1024):.2f} MB/s"
    elif speed > 1024:
        return f"{speed / 1024:.2f} KB/s"
    else:
        return f"{speed:.2f} B/s"

def update_speed_label():
    sent_before, recv_before = get_network_speed()
    time.sleep(1)
    sent_after, recv_after = get_network_speed()
    sent_speed = (sent_after - sent_before)
    recv_speed = (recv_after - recv_before)
    upload_label.config(text=f"Upload: {format_speed(sent_speed)}")
    download_label.config(text=f"Download: {format_speed(recv_speed)}")
    root.after(1000, update_speed_label)

root = tk.Tk()
root.title("Network Speed Meter")
root.attributes("-topmost", True)
root.overrideredirect(True)
root.geometry("240x20")
root.configure(background='white')

upload_label = tk.Label(root, text="Upload: -- B/s", bg='white', fg='black')
upload_label.pack(side=tk.LEFT)

download_label = tk.Label(root, text="Download: -- B/s", bg='white', fg='black')
download_label.pack(side=tk.RIGHT)

root.after(0, update_speed_label)

root.geometry(f"+{1046}+{816}")

root.mainloop()

ctypes.windll.user32.SetWindowPos(root.winfo_id(), -1, 1046, 816, 0, 0, 0x0001)