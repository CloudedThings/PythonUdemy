import datetime
import pytz


class Account:
    """ Simple account class with balance """

    @staticmethod
    def _current_time(self):
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance
        self._transaction_list = [(Account._current_time(self), self.__balance)]
        print("Account created for " + self._name)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.show_balance()
            self._transaction_list.append((Account._current_time(self), amount))

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self._transaction_list.append((Account._current_time(self), -amount))
        else:
            print("The amount must be greater then zero and no more then your account balance")
        self.show_balance()

    def show_balance(self):
        print("Balance is {}".format(self.__balance))

    def show_transactions(self):
        for date, amount in self._transaction_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print("{:6} {} on {} (local time was {})".format(amount, tran_type, date, date.astimezone()))


if __name__ == '__main__':
    les = Account("Les", 0)
    les.show_balance()

    les.deposit(1000)
    les.withdraw(505)
    les.withdraw(2000)
    les.show_transactions()

    tim = Account("Tim", 800)
    tim.__balance = 200
    tim.deposit(100)
    tim.withdraw(200)
    tim.show_transactions()
    print(tim.__dict__)

