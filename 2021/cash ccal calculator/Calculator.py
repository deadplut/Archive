import datetime as dt


class Calculator:

    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, comment, amount, date='now'):
        if date == 'now':
            date = dt.datetime.now().date()
        else:
            date = dt.datetime.strptime(date, '%d.%m.%Y').date()
        self.records.append({
            'date': date,
            'comment': comment,
            'amount': amount
        })

    def get_today_stats(self):
        today_count = 0
        for rec in self.records:
            if rec['date'] == dt.datetime.now().date():
                today_count += rec['amount']
        return today_count

    def get_week_stats(self):
        week_count = 0
        week_ago = dt.date.today() - dt.timedelta(days=7)
        for rec in self.records:
            if week_ago <= rec['date'] <= dt.date.today():
                week_count += rec['amount']
        return week_count


class CashCalculator(Calculator):

    def add_waste(self, comment, amount, date='now'):
        return super().add_record(comment, amount, date)

    def get_week_stats(self):
        return super().get_week_stats()

    def get_today_stats(self):
        return super().get_today_stats()

    def get_today_cash_remained(self, currency='руб'):
        self.money = {
            'USD': 75,
            'EURO': 95,
            'руб':  1
        }
        self.diff = (self.limit - self.get_today_stats()) / self.money[currency]
        if self.diff > 0:
            return f'На сегодня осталось {self.diff} {currency}'
        elif self.diff == 0:
            return f'Денег больше нет, но и долга пока нет)'
        return f'Упс, твой долг: {self.diff} {currency}'

class CaloriesCalculator(Calculator):

    def get_week_stats(self):
        return super().get_week_stats()

    def get_today_stats(self):
        return super().get_today_stats()

    def add_meal(self, comment, amount, date='now'):
        return super().add_record(comment, amount, date)

    def get_calories_remained(self):
        diff = self.limit - self.get_today_stats()
        if diff > 0:
            return '«Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {} кКал»'.format(diff)
        return 'Сегодня ты переел, бро, на {} кКал»'.format(abs(diff))


d1 = CashCalculator(2000)
d1.add_waste('Творожок', 200)
d1.add_waste('Котлета', 200)
d1.add_waste('Рис', 200)
d1.add_waste('торт', 200)
d1.add_waste('Сырок', 200)
d1.add_waste('Творожок', 200)
d1.add_waste('Котлета', 200)
d1.add_waste('Рис', 200)
d1.add_waste('торт', 200)
d1.add_waste('Сырок', 200)
d1.add_waste('Творожок', 200)
d1.add_waste('Котлета', 200)
d1.add_waste('Рис', 200)
d1.add_waste('торт', 200)
d1.add_waste('Сырок', 200)
d1.add_waste('Мёд', 200, '21.02.2021')
d1.add_waste('Мёд', 5, '25.09.2021')
d1.add_waste('Мёд', 1, '21.09.2021')
d1.add_waste('Мёд', 1, '24.09.2021')
d1.add_waste('Мёд', 1, '28.09.2021')
print(d1.get_today_cash_remained())
print('wwek: ', d1.get_week_stats())
print('day: ', d1.get_today_stats())
print(d1.get_today_cash_remained('USD'))
print(d1.get_today_cash_remained("EURO"))
print(d1.get_today_cash_remained())
