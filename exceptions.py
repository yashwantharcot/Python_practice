class ValueTooHighError(Exception):
    pass
class ValueTooSmallError(Exception):
    def __init(self, message, value):
        self.message = message
        self.value = value
def test_value(x):
    if x > 100:
        raise ValueTooHighError('value is too high')
    if x < 5:
        raise ValueTooSmallError('value is too small', x)

try:
    test_value(2)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message, e.value)