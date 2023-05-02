# Создайте класс Clock со статичным методом Say_time,
# который будет выводить на экран текущее время.
#
# Подсказка: для этого можете воспользоваться стандартной библиотекой time.

from time import time, localtime
class Clock():
    @staticmethod
    def Say_time():
        rez = localtime(time())
        print(f'{rez.tm_hour}:{rez.tm_min}:{rez.tm_sec}')  # 10:29:45


a = Clock.Say_time()