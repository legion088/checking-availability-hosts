## Описание:
> Проверяем доступность сетевых ресурсов с помощью асинхронного `aioping`.<br />
#### Проблема ожидания вывода информации с помощью команды `ping`
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

### Description:
We check the availability of network resources using asynchronous aioping.

### The problem of the availability of the command services using the ping command 
When checking network resources using the standard ping command, there is a problem of waiting for information output if they are not available, since the response time and the number of parameters returned are expected.

### Why asynchronous?
When testing the availability of services using os.system(), subprocess.call(), the result is similar as with a normal ping - you have to wait for a response, and for this purpose asynchronous verification was implemented, i.e. if there is an expectation, perform another check and give the result.

### Installation Instructions:
Asynchronous aiorip is available for the following Python versions: 3.5-3-8 . The latest release is July 2020.<br/>
My case is Python 3.8.0, aioping 0.3.1<br/>1. Installing Python: 3.5-3-8<br/>
2. Creating a python -m venv venv virtual environment and activating it<br/>
3. Installing the pip install aioping package<br/>
4. In a text file, we add services via line break or make an upload<br/>
5. Running the code
### Note:
In case of packet loss or long delay (aioping.ping(hostname) * 1000), the service being checked may get into a TimeoutError exception<br/>
If a socket.error occurs, you can use ctypes.windll.shell32.IsUserAnAdmin()

