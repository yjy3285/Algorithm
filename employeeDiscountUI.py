import tkinter as tk
from tkinter import ttk

class PaymentApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Payment 결제하기")
        self.geometry("600x400")
        self.create_widgets()

    def create_widgets(self):
        # Payment 타이틀
        title_label = tk.Label(self, text="Payment 결제하기", font=("Arial", 18, "bold"), fg="green")
        title_label.pack(pady=20)

        # Step 1: 포인트 적립/사용, 할인을 먼저 선택해주세요.
        step1_label = tk.Label(self, text="Step 1 포인트 적립/사용, 할인을 먼저 선택해주세요.", font=("Arial", 14, "bold"))
        step1_label.pack(anchor="w", padx=20, pady=10)

        # 포인트 적립, 포인트 사용, 임직원 할인 버튼
        buttons_frame1 = tk.Frame(self)
        buttons_frame1.pack(pady=10)

        point_save_button = tk.Button(buttons_frame1, text="포인트 적립", font=("Arial", 12), width=15, height=2, bg="#B2DFDB")
        point_save_button.grid(row=0, column=0, padx=10)

        point_use_button = tk.Button(buttons_frame1, text="포인트 사용", font=("Arial", 12), width=15, height=2, bg="#B2DFDB")
        point_use_button.grid(row=0, column=1, padx=10)

        employee_discount_button = tk.Button(buttons_frame1, text="임직원 할인", font=("Arial", 12), width=15, height=2, bg="#B2DFDB")
        employee_discount_button.grid(row=0, column=2, padx=10)

        # Step 2: 결제수단을 선택해주세요.
        step2_label = tk.Label(self, text="Step 2 결제수단을 선택해주세요.", font=("Arial", 14, "bold"))
        step2_label.pack(anchor="w", padx=20, pady=10)

        # 카드/삼성페이, 애플페이 버튼
        buttons_frame2 = tk.Frame(self)
        buttons_frame2.pack(pady=10)

        card_button = tk.Button(buttons_frame2, text="카드/삼성페이", font=("Arial", 12), width=15, height=2, bg="#B2DFDB")
        card_button.grid(row=0, column=0, padx=10)

        apple_pay_button = tk.Button(buttons_frame2, text="애플페이", font=("Arial", 12), width=15, height=2, bg="#B2DFDB")
        apple_pay_button.grid(row=0, column=1, padx=10)

if __name__ == "__main__":
    app = PaymentApp()
    app.mainloop()
