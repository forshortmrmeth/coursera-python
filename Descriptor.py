class Value:
    def __init__(self):
        self.amount = 0

    def __set__(self, instance, value):
        self.amount = value - (value * instance.commission)

    def __get__(self, instance, owner):
        return self.amount


class Account:
    amount = Value()

    def __init__(self, commission):
        self.commission = commission


if __name__ == '__main__':
    new_account = Account(0.1)
    new_account.amount = 100