import os

from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов
IP = env.str("ip")  # Тоже str, но для айпи адреса хоста
URL_APPLES = "https://rozetka.com.ua/champion_a00225/p27223057"
URL_PEAR = "https://freshmart.com.ua/product/yabloko-gala-116.html"
"""
host = env.str("")
PG_USER = env.str("NULP_BOT")
PG_PASS = env.str("stranger")
"""