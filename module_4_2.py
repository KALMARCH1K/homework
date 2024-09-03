def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()

test_function()
inner_function()  # при реализации кода появится ошибка из-за того, что функция не определена
                  # в глобальном пространстве имен