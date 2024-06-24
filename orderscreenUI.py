import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class CafeMenuApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cafe Menu")
        self.geometry("800x600")
        
        self.create_widgets()

    def create_widgets(self):
        # 메뉴 카테고리 라벨
        cafe_label = tk.Label(self, text="CAFE", font=("Arial", 18, "bold"))
        cafe_label.grid(row=0, column=0, padx=10, pady=10)
        
        bread_label = tk.Label(self, text="BREAD", font=("Arial", 18, "bold"))
        bread_label.grid(row=0, column=1, padx=10, pady=10)
        
        brunch_label = tk.Label(self, text="BRUNCH", font=("Arial", 18, "bold"))
        brunch_label.grid(row=0, column=2, padx=10, pady=10)
        
        wine_beer_label = tk.Label(self, text="WINE/BEER", font=("Arial", 18, "bold"))
        wine_beer_label.grid(row=0, column=3, padx=10, pady=10)
        
        # 메뉴 항목들
        menu_items = [
            ("Sunny Latte 써니라떼", 6.5),
            ("Tropical Ade 트로피칼 에이드", 7.0),
            ("Orange Cream Sherbet 오렌지 크림샤베트", 5.0),
            ("Americano 아메리카노", 5.0),
            ("Cafe Latte 카페라떼", 6.0),
            ("Vanilla Latte 바닐라 라떼", 6.5),
            ("Cappuccino 카푸치노", 6.0),
            ("Einspanner 아인슈페너", 6.0),
            ("Fruit Tea 과일티", 4.0),
            ("Herb Tea 허브티", 6.5),
            ("Orange squeezed juice 오렌지 착즙주스", 7.0),
            ("Ade 에이드", 5.5),
            ("Soda 탄산음료", 4.0)
        ]
        
        # Signature 메뉴
        signature_label = tk.Label(self, text="SIGNATURE", font=("Arial", 14, "bold"))
        signature_label.grid(row=1, column=0, sticky="W", padx=10, pady=5)
        
        for i, (menu_name, price) in enumerate(menu_items[:3]):
            menu_label = tk.Label(self, text=f"{menu_name}", font=("Arial", 12))
            menu_label.grid(row=i+2, column=0, sticky="W", padx=20)
            price_label = tk.Label(self, text=f"${price:.1f}", font=("Arial", 12, "italic"), fg="red")
            price_label.grid(row=i+2, column=1, sticky="W")

        # Coffee 메뉴
        coffee_label = tk.Label(self, text="COFFEE", font=("Arial", 14, "bold"))
        coffee_label.grid(row=5, column=0, sticky="W", padx=10, pady=5)
        
        for i, (menu_name, price) in enumerate(menu_items[3:8]):
            menu_label = tk.Label(self, text=f"{menu_name}", font=("Arial", 12))
            menu_label.grid(row=i+6, column=0, sticky="W", padx=20)
            price_label = tk.Label(self, text=f"${price:.1f}", font=("Arial", 12, "italic"), fg="red")
            price_label.grid(row=i+6, column=1, sticky="W")

        # Beverage 메뉴
        beverage_label = tk.Label(self, text="BEVERAGE", font=("Arial", 14, "bold"))
        beverage_label.grid(row=11, column=0, sticky="W", padx=10, pady=5)
        
        for i, (menu_name, price) in enumerate(menu_items[8:]):
            menu_label = tk.Label(self, text=f"{menu_name}", font=("Arial", 
