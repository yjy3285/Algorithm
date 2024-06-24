import tkinter as tk
from tkinter import ttk

class CafeOrderApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Take-out 가져가기")
        self.geometry("800x600")
        self.create_widgets()

    def create_widgets(self):
        # 주문 내역 타이틀
        title_label = tk.Label(self, text="Take-out 가져가기", font=("Arial", 18, "bold"))
        title_label.pack(pady=20)

        # 아이템 개수
        items_label = tk.Label(self, text="3 items", font=("Arial", 12))
        items_label.pack(pady=10)

        # 주문 내역 프레임
        order_frame = tk.Frame(self)
        order_frame.pack(pady=20)

        # 메뉴 항목들
        menu_items = [
            ("Americano 아메리카노", 5.0, 2),
            ("Cafe Latte 카페라떼", 6.0, 1),
            ("Sunny Latte 써니라떼", 6.5, 3)
        ]

        # 주문 내역 표시
        for i, (menu_name, price, quantity) in enumerate(menu_items):
            item_frame = tk.Frame(order_frame, borderwidth=1, relief="solid", pady=5)
            item_frame.pack(fill="x", padx=20, pady=5)

            menu_label = tk.Label(item_frame, text=f"{menu_name}", font=("Arial", 14, "bold"))
            menu_label.pack(side="left", padx=10)

            price_label = tk.Label(item_frame, text=f"{price:.1f} / ea", font=("Arial", 12), fg="green")
            price_label.pack(side="left", padx=10)

            quantity_label = tk.Label(item_frame, text=f"{quantity}ea", font=("Arial", 12))
            quantity_label.pack(side="right", padx=10)

            total_label = tk.Label(item_frame, text=f"{price * quantity:.1f}", font=("Arial", 14, "bold"))
            total_label.pack(side="right", padx=10)

        # 주문 요약
        summary_frame = tk.Frame(self, borderwidth=1, relief="solid", pady=10)
        summary_frame.pack(pady=20, fill="x", padx=20)

        summary_title = tk.Label(summary_frame, text="주문내역", font=("Arial", 14, "bold"))
        summary_title.pack(anchor="w", padx=10)

        total_price = sum(price * quantity for _, price, quantity in menu_items)
        for menu_name, price, quantity in menu_items:
            summary_label = tk.Label(summary_frame, text=f"{menu_name} {quantity}ea {price * quantity:.1f}", font=("Arial", 12))
            summary_label.pack(anchor="w", padx=10)
        
        total_label = tk.Label(summary_frame, text=f"Total {total_price:.1f}", font=("Arial", 14, "bold"))
        total_label.pack(anchor="e", padx=10)

        # 결제 버튼
        payment_button = tk.Button(self, text="Continue to payment", font=("Arial", 14, "bold"), bg="green", fg="white")
        payment_button.pack(pady=20, padx=20, anchor="e")

if __name__ == "__main__":
    app = CafeOrderApp()
    app.mainloop()
