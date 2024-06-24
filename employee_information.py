import cv2
from pyzbar import pyzbar
import qrcode

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Employee:
    def __init__(self, id, name, department, position):
        self.id = id
        self.name = name
        self.department = department
        self.position = position

class CafeKiosk:
    def __init__(self):
        self.menu = []
        self.order = []
        self.is_employee = False
        self.discount_rate = 0.3  # 30% discount for employees
        self.employees = {
            "20240001": Employee("20240001", "홍길동", "영업1팀", "사원"),
            "20220002": Employee("20220002", "김나영", "디자인팀", "대리"),
            "20200003": Employee("20200003", "신다혜", "IT개발팀", "팀장")
        }

    def add_menu_item(self, name, price):
        self.menu.append(MenuItem(name, price))

    def show_menu(self):
        print("Menu:")
        for i, item in enumerate(self.menu):
            print(f"{i + 1}. {item.name} - ${item.price:.2f}")

    def take_order(self):
        while True:
            self.show_menu()
            choice = input("Select a menu item by number (or 'done' to finish): ")
            if choice.lower() == 'done':
                break
            try:
                index = int(choice) - 1
                if 0 <= index < len(self.menu):
                    self.order.append(self.menu[index])
                    print(f"Added {self.menu[index].name} to your order.")
                else:
                    print("Invalid menu item number.")
            except ValueError:
                print("Please enter a valid number.")

    def scan_qr_code(self):
        def decode_qr(image):
            decoded_objects = pyzbar.decode(image)
            for obj in decoded_objects:
                return obj.data.decode('utf-8')
            return None

        cap = cv2.VideoCapture(0)
        print("Scanning QR code...")

        while True:
            ret, frame = cap.read()
            if not ret:
                print("Failed to capture image")
                break

            qr_data = decode_qr(frame)
            if qr_data:
                print(f"QR code data: {qr_data}")
                if qr_data in self.employees:
                    self.is_employee = True
                    employee = self.employees[qr_data]
                    print(f"Employee verified: {employee.name}, {employee.department}, {employee.position}, {employee.id}")
                    self.show_employee_info(employee)
                else:
                    print("Invalid employee QR code.")
                break

            cv2.imshow("QR Code Scanner", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

    def show_employee_info(self, employee):
        print("\n정보 확인")
        print(f"이름: {employee.name}")
        print(f"부서: {employee.department}")
        print(f"직급: {employee.position}")
        print(f"사번: {employee.id}")

    def apply_employee_discount(self):
        employee_input = input("본인의 정보가 맞습니까? (확인/취소): ").lower()
        if employee_input == '확인':
            print("결제창으로 이동합니다.")
            self.scan_qr_code()
        else:
            self.is_employee = False

    def calculate_total(self):
        total = sum(item.price for item in self.order)
        if self.is_employee:
            total *= (1 - self.discount_rate)
        return total

    def print_receipt(self):
        print("\nReceipt:")
        for item in self.order:
            print(f"{item.name} - ${item.price:.2f}")
        total = self.calculate_total()
        if self.is_employee:
            print(f"Employee discount applied: {self.discount_rate * 100}%")
        print(f"Total: ${total:.2f}")

def main():
    kiosk = CafeKiosk()
    kiosk.add_menu_item("Americano", 3.00)
    kiosk.add_menu_item("Latte", 4.00)
    kiosk.add_menu_item("Cappuccino", 4.50)
    kiosk.add_menu_item("Mocha", 5.00)
    kiosk.add_menu_item("Tea", 2.50)

    kiosk.take_order()
    kiosk.apply_employee_discount()
    kiosk.print_receipt()

if __name__ == "__main__":
    main()
