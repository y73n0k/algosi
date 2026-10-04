# Алгоритм Монтгомери умножения и возведения в степени в кольце вычетов.

В файле [util.py](util.py) представлены нахождение значений `R', N'` и `R^2 mod N`.

В файле [montgomery_general.py](montgomery_general.py), [montgomery_bn.py](montgomery_bn.py), [montgomery_2n.py](montgomery_2n.py) представлены реализации алгоритмов при произвольном `R`, при `R = b^n` и при `R = 2^n` соответсвенно.

В [test.py](test.py) представлены примеры использования алгоритма и проверка корректности.

Запуск программы:

```bash
python test.py
```