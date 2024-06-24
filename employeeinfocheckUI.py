import tkinter as tk
from tkinter import ttk

def create_ui():
    root = tk.Tk()
    root.title("정보 확인")

    
    main_frame = ttk.Frame(root, padding="20")
    main_frame.grid(row=0, column=0, sticky="nsew")

    
    check_info_button = ttk.Button(main_frame, text="정보 확인", style="TButton")
    check_info_button.grid(row=0, column=0, columnspan=2, pady=(0, 20))

    
    labels = ["이름", "부서", "직급", "사번"]
    values = ["XXX", "ooo팀", "yy", "20xx00xx"]
    for i, (label, value) in enumerate(zip(labels, values)):
        ttk.Label(main_frame, text=label, foreground="blue", background="#f0f0f0").grid(row=i+1, column=0, padx=10, pady=5, sticky="e")
        ttk.Label(main_frame, text=value, background="#fffacd").grid(row=i+1, column=1, padx=10, pady=5, sticky="w")

   
    confirmation_label = ttk.Label(main_frame, text="본인의 정보가 맞습니까?", font=("Arial", 12))
    confirmation_label.grid(row=len(labels)+1, column=0, columnspan=2, pady=30)

   
    cancel_button = ttk.Button(main_frame, text="취소", style="TButton")
    confirm_button = ttk.Button(main_frame, text="확인", style="TButton")

    cancel_button.grid(row=len(labels)+2, column=0, padx=5, pady=10)
    confirm_button.grid(row=len(labels)+2, column=1, padx=5, pady=10)

    
    style = ttk.Style()
    style.configure("TButton", font=("Arial", 12), padding=10, foreground="white", background="green")
    style.map("TButton",
              foreground=[('pressed', 'white'), ('active', 'white')],
              background=[('pressed', 'darkgreen'), ('active', 'green')])

    root.mainloop()

if __name__ == "__main__":
    create_ui()
