import requests

# 키오스크 주문 데이터 생성
order_data = {
    "order_id": 123,
    "items": [
        {"name": "Americano", "quantity": 1},
        {"name": "Latte", "quantity": 2}
    ],
    "total_price": 11.00
}

# 키오스크에서 POS 시스템으로 주문 전송
pos_endpoint = "http://pos-system.local/api/orders"
response = requests.post(pos_endpoint, json=order_data)
if response.status_code == 200:
    print("Order sent to POS system successfully")

# POS 시스템에서 OMS로 주문 전송
oms_endpoint = "http://order-management-system.local/api/orders"
response = requests.post(oms_endpoint, json=order_data)
if response.status_code == 200:
    print("Order sent to OMS successfully")

# OMS에서 주방 디스플레이 시스템(KDS)으로 주문 전송
kds_endpoint = "http://kitchen-display-system.local/api/orders"
response = requests.post(kds_endpoint, json=order_data)
if response.status_code == 200:
    print("Order sent to KDS successfully")
