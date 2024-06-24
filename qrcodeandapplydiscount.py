import cv2
from pyzbar.pyzbar import decode
import pandas as pd

# 예시 포스기 메뉴 데이터 (CSV 파일로부터 불러온다고 가정)
# 실제 포스기 시스템과 연동할 때는 해당 시스템의 API를 사용
menu_data = {
    'menu_id': [1, 2, 3],
    'menu_name': ['Americano', 'Orange juice', 'Cafe Latte'],
    'price': [5.00, 7.50, 6.00]
}
menu_df = pd.DataFrame(menu_data)

# 사번으로 직원 정보를 확인하는 예시 데이터
employees_data = {
    'emp_id': ['20240001', '20220002', '20200003'],
    'name': ['홍길동', '김나영', '신다혜']
}
employees_df = pd.DataFrame(employees_data)

# QR 코드를 인식하고 사번을 추출
def read_qr_code(frame):
    decoded_objects = decode(frame)
    for obj in decoded_objects:
        emp_id = obj.data.decode('utf-8')
        return emp_id
    return None

# 사번으로 직원 정보를 조회
def get_employee_info(emp_id):
    emp_info = employees_df[employees_df['emp_id'] == emp_id]
    if not emp_info.empty:
        return emp_info.iloc[0]
    return None

# 주문 금액과 할인율을 받아 할인 금액을 계산
def calculate_discounted_price(price, discount_rate=0.3):
    return price * (1 - discount_rate)

# 포스기와 연동하여 메뉴 가격을 가져옴  (여기서는 예시 데이터프레임을 사용)
def get_menu_prices():
    return menu_df


def main():
    # 키오스크 또는 테블릿에서 주문할 메뉴 선택
    print("Menu:")
    for index, row in menu_df.iterrows():
        print(f"{row['menu_id']}: {row['menu_name']} - ${row['price']:.2f}")
    
    selected_menu_ids = input("Enter the menu IDs you want to order, separated by commas: ").split(',')
    selected_menu_ids = [int(id.strip()) for id in selected_menu_ids]

    # 선택된 메뉴의 원래 가격 합계 계산
    selected_menus = menu_df[menu_df['menu_id'].isin(selected_menu_ids)]
    original_price = selected_menus['price'].sum()

    # QR 코드 인식
    cap = cv2.VideoCapture(0)
    print("Please show your employee QR code to the camera.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        emp_id = read_qr_code(frame)
        if emp_id:
            emp_info = get_employee_info(emp_id)
            if emp_info is not None:
                name = emp_info['name']
                discounted_price = calculate_discounted_price(original_price)
                print(f"Employee: {name}")
                print(f"Original Price: ${original_price:.2f}")
                print(f"Discounted Price: ${discounted_price:.2f}")
            else:
                print("Employee not found.")

            break

        cv2.imshow('QR Code Scanner', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
