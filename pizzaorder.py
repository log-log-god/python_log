# 피자 주문 함수
def select(menu, menuname):
  
    order = {}
    print(f'\n*** {menuname}목록****')
    for name, price in menu.items():
        print(f'{name} ({price}) 원')

    while True:
        p_name = input(f'주문할 {menuname} 입력하세요(종료: 0)')
        if p_name == '0':
            pass
        elif p_name in menu:
            count = int(input('수량을 입력하세요: '))
            order[p_name] = count           # 딕셔너리에 데이터 삽입
            print('주문 완료')
        elif p_name == 'exit':
            break

    return order

    # print(order_pizza)


def money_calculator(order, menu, menuname)
    tot_price = 0
    for x in order_pizza.keys():
          price = 0
          if x in pizza_menu.keys():
              price = price+(order_pizza[x]*pizza_menu[x])
          print(f'{x}({pizza_menu[x]}원)x{order_pizza[x]} = {price:, }원')
          tot_price = tot_price +price

      print(f'피자 전체 가격: {tot_price}')

if __name__ == '__main__':
      pizza_menu = {'페페로니 피자': 3000, 
                '치즈피자': 3200, 
                '콤비네이션 피자': 3500, 
                '불고기 피자': 3600, 
                '해산물 피자': 3800}
      
      drink_menu = {'콜라': 1500, '사이다': 1500, '생수': 1000}

      order_pizza = select(pizza_menu, '피자')
      print(order_pizza)
    #   order_drink = select(drink_menu)
    #   print(order_drink)


      for x in order_pizza.keys():
          price = 0
          if x in pizza_menu.keys():
              price = price+(order_pizza[x]*pizza_menu[x])
          print(f'{x}({pizza_menu[x]}원)x{order_pizza[x]} = {price:, }원')
          tot_price = tot_price +price

      print(f'피자 전체 가격: {tot_price}')



    # pizza_select(select())
    # drink_select(select())