def subdivide(counter, note, money, keys, total):
    if total == 0:
        return True

    if counter % 2 == 0 or money[note] == 0 or total < note:
        del money[note]
        if not money:
            return False
        note = keys[0]
        del keys[0]

    if counter % 2 == 1 and total >= note and money[note] > 0:
        total -= note
        money[note] -= 1

    return subdivide(counter + 1, note, dict(money), keys[:], total) \
        or subdivide(counter + 2, note, dict(money), keys[:], total)


class CashDesk:
    def __init__(self):
        self.money = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}

    def take_money(self, money):
        for note in money:
            self.money[note] += money[note]

    def total(self):
        return sum([note * self.money[note] for note in self.money])

    def can_withdraw_money(self, total):
        if self.total() < total:
            return False
        keys = [50, 20, 10, 5, 2, 1]
        note = 100
        return subdivide(1, note, dict(self.money), keys[:], total) \
            or subdivide(2, note, dict(self.money), keys[:], total)


def main():
    my_cash_desk = CashDesk()
    my_cash_desk.take_money({1: 2, 50: 1, 20: 1})
    print(my_cash_desk.total())  # 72
    print(my_cash_desk.can_withdraw_money(30))  # False
    print(my_cash_desk.can_withdraw_money(70))  # True

if __name__ == "__main__":
    main()
