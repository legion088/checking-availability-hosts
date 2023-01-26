## Описание:
> Проверяем доступность сетевых ресурсов с помощью асинхронного `aioping`.<br />
#### Проблема доступности сервисов команды с помощью команды `ping`
> При проверке сетевых ресурсов с помощью стандартной команды `ping` возникает проблема ожидания вывода информации если они недоступны, так как ожидается время ответа и количество возвращаемых параметров.<br />
#### Почему асинхрон?
> При проведении тестов доступности сервисов с помощью `os.system()`, `subprocess.call()` результат аналогичный как при обычном `ping` - приходится ждать ответа, и именно с этой целью была реализована асинхронная проверка, т.е. если есть ожидание - выполни другую проверку и выдай результат.     

## Инструкция по установке:
Асинхронный `aioping`доступен для следующих версий Python: 3.5-3-8. Последний релиз - июль 2020. [История версий](https://pypi.org/project/aioping/#history)<br/>
Мой случай - Python 3.8.0, aioping 0.3.1 <br/>
1. Устанавливаем `Python: 3.5-3-8`
2. Создаём виртуальное окружение `python -m venv venv` и активируем его
3. Устанавливаем пакет `pip install aioping`
4. В текстовом файле добавляем сервисы через перенос строки либо делаем выгрузку
5. Запускаем код


## Примечание:
> 1. При потери пакетов или длительной задержки (aioping.ping(hostname) * 1000), проверяемый сервис может попасть в исключение TimeoutError<br />
> 2. При возникновении ошибки socket.error можно использовать ctypes.windll.shell32.IsUserAnAdmin()