# 피자 주문 함수
def pizza_select():
    pizza_menu = {'페페로니 피자': 3000, 
                '치즈피자': 3200, 
                '콤비네이션 피자': 3500, 
                '불고기 피자': 3600, 
                '해산물 피자': 3800}
    order_pizza = {}
    for name, price in pizza_menu.items():
        print(f'{name} ({price}) 원')

    while True:
        p_name = input('메뉴 이름 입력하세요(종료: 0)')
        if p_name == '0':
            pass
        elif p_name in pizza_menu:
            count = int(input('수량을 입력하세요: '))
            order[p_name] = count           # 딕셔너리에 데이터 삽입
            print('주문 완료')
        elif p_name == 'exit':
            break

    return order_pizza

    print(order_pizza)




# 음료 주문 함수
def drink_select():
    drink_menu = {'콜라': 1500, 
                '사이다': 1500, 
                '생수': 1000}
    order_drink = {}
    for name, price in drink_menu.items():
        print(f'{name} ({price}) 원')

    while True:
        d_name = input('메뉴 이름 입력하시오 (종료: 0)')
        if d_name == '0':
            pass
        elif d_name in drink_menu:
            count = int(input('수량을 입력하세요: '))
            order[d_name] = count
            print('주문 완료')
        elif d_name == 'exit':
            break

    return order_drink




if __name__ == '__main__':
    pizza_select(pizza_select())
    drink_select(drink_select())