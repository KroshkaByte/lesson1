def discounted(price, discount, max_discount=20):
    try:
        price = abs(float(price))
        discount = abs(float(discount))
        max_discount = abs(int(max_discount))
        if max_discount >= 100:
            raise ValueError("Слишком большая максимальная скидка")
        if discount >= max_discount:
            return price
        else:
            return price - (price * discount / 100)
    except (ValueError, TypeError):
        print("Введите корректное значение !")


price = input()
discount = input()
print(discounted(price, discount))
