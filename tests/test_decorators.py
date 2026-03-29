from src.decorators import log


def test_log(capsys):
    @log()
    def my_function(x, y):
        return x + y

    my_function(1, 2)
    captured = capsys.readouterr()
    assert "my_function" in captured.out

    @log()
    def my_function(x, y):
        return x + y

    my_function(1, "f")
    captured = capsys.readouterr()
    assert "Ошибка" in captured.out
