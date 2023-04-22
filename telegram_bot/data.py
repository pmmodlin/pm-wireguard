from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("TOKEN")
ADMINS = env.list("ADMINS")
WG_MANAGER_PATH = env.str("WG_MANAGER_PATH")


class ReturnCodes:
    SystemFail = 1
    PeerNotExists = 10
    ValidationError = 11
    PeerAlreadyExists = 12
    SubnetError = 24


class Text:
    MENU = "WireGuard Manager bot меню"
    HELP = "Обратитесь к администратору"
    START = "Приветствую, {name}"
    CLIENTS = "Клиенты"
    CLIENT = "Клиент \"{client_name}\""
    CLIENT_ADDED = "Клиент \"{client_name}\" добавлен!"
    CLIENT_DELETED = "Клиент \"{client_name}\" удалён!"
    CLIENT_DELETE_CONFIRM = "Вы действительно хотите удалить клиента \"{client_name}\"?"
    ASK_NAME = "Введите имя нового клиента (используйте латинские буквы, числа и знаки: \"-\", \"_\")"
    ERROR_1 = "Системная ошибка, проверьте логи"
    ERROR_11 = "Неверное имя, используйте латинские буквы, числа и знаки: \"-\", \"_\""
    ERROR_10 = "Клиента \"{client_name}\" нет в базе"
    ERROR_12 = "Клиент \"{client_name}\" уже существует"
    ERROR_24 = "24 net поддерживает только 253 подключения"


class ButtonText:
    ADD_CLIENT = "Добавить клиента"
    BACK_MENU = "Вернуться в меню"
    GET_QR = "QR-код"
    GET_FILE = "Файл"
    GET_RAW = "RAW"
    DELETE = "Удалить"
    CONFIRM = "Подтвердить!"
    CLIENTS = "Клиенты"