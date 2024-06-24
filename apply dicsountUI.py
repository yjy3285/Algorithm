import tkinter as tk
from tkinter import ttk

def create_ui():
    root = tk.Tk()
    root.title("Payment 결제하기")

    
    step1_label = ttk.Label(root, text="Step 1 포인트 적립/사용 ,할인을 먼저 선택해주세요.")
    step1_label.grid(row=0, column=0, columnspan=3, padx=10, pady=5, sticky="w")

    point_accumulate_button = ttk.Button(root, text="포인트 적립")
    point_use_button = ttk.Button(root, text="포인트 사용")
    employee_discount_button = ttk.Button(root, text="임직원 할인")

    point_accumulate_button.grid(row=1, column=0, padx=5, pady=5)
    point_use_button.grid(row=1, column=1, padx=5, pady=5)
    employee_discount_button.grid(row=1, column=2, padx=5, pady=5)

    
    step2_label = ttk.Label(root, text="Step 2 결제수단을 선택해주세요.")
    step2_label.grid(row=2, column=0, columnspan=3, padx=10, pady=5, sticky="w")

    card_payment_button = ttk.Button(root, text="카드/삼성페이")
    applepay_button = ttk.Button(root, text="애플페이")

    card_payment_button.grid(row=3, column=0, padx=5, pady=5)
    applepay_button.grid(row=3, column=1, padx=5, pady=5)

   
    final_amount_frame = ttk.Frame(root)
    final_amount_frame.grid(row=4, column=0, columnspan=3, padx=10, pady=10, sticky="ew")

    final_amount_label = ttk.Label(final_amount_frame, text="최종 결제금액", foreground="pink", font=("Arial", 14))
    final_amount_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

    final_amount_value = ttk.Label(final_amount_frame, text="24850원", foreground="pink", font=("Arial", 14))
    final_amount_value.grid(row=0, column=1, padx=5, pady=5, sticky="e")

    order_total_label = ttk.Label(final_amount_frame, text="총 주문 금액", font=("Arial", 12))
    order_total_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

    order_total_value = ttk.Label(final_amount_frame, text="35,500", font=("Arial", 12))
    order_total_value.grid(row=1, column=1, padx=5, pady=5, sticky="e")

    discount_total_label = ttk.Label(final_amount_frame, text="총 할인 금액", font=("Arial", 12))
    discount_total_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")

    discount_total_value = ttk.Label(final_amount_frame, text="10,650", font=("Arial", 12))
    discount_total_value.grid(row=2, column=1, padx=5, pady=5, sticky="e")

    
    cancel_payment_button = ttk.Button(root, text="결제 취소", foreground="pink", font=("Arial", 12))
    cancel_payment_button.grid(row=5, column=0, columnspan=3, pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_ui()
