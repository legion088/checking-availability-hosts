import pytest
from my_packages.check_hosts_available import *


def test_check_validations():
    lines = ['server01', 'server-02', 'server03']
    file_lines = open_readlines_file("allowed.txt")
    assert check_validation_lines(file_lines) == lines


def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        open_readlines_file(" ")


def test_check_validations_forbidden_symbols():
    with pytest.raises(ValueError) as f_emp:
        check_validation_lines([
            ',', '~', ':', '!', ' ', '@', '#',
            '$', '%', '^', '&', '`', '()',
            '{}', '_'
        ])
    assert "Строка содержит запрещающий символ!" == f_emp.value.args[0]


def test_check_validations_empty_file():
    with pytest.raises(ValueError) as f_emp:
        check_validation_lines([])
    assert "Файл пустой!" == f_emp.value.args[0]
