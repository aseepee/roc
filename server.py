import tkinter as tk
from tkinter import messagebox

# إنشاء نافذة
window = tk.Tk()
window.title("واجهة تجريبية")
window.geometry("600x400")
window.configure(bg="red")

# نص التعليمات
label = tk.Label(window, text="أدخل المفتاح الذي حصلت عليه من المهاجم", bg="red", fg="white", font=("Arial", 16))
label.pack(pady=20)

# إدخال النص
entry = tk.Entry(window, font=("Arial", 14), justify="center")
entry.pack(pady=10)

# زر الدخول
def on_submit():
    key = entry.get()
    if key == "12345":
        messagebox.showinfo("نجاح", "تم الدخول إلى النظام!")
    else:
        messagebox.showwarning("خطأ", "المفتاح غير صحيح!")

button = tk.Button(window, text="دخول إلى النظام", command=on_submit, bg="white", fg="black", font=("Arial", 14))
button.pack(pady=20)

# صورة الجمجمة
skull_image = tk.PhotoImage(file="skull.png")  # ضع صورة الجمجمة هنا
skull_label = tk.Label(window, image=skull_image, bg="red")
skull_label.pack(pady=20)

# تشغيل التطبيق
window.mainloop()