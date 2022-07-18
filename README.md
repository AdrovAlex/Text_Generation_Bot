# Text_Generation_Bot
Бот генерирует добрые и злые новостные заголовки

Установка:

git clone

pip install -r requirements.txt

echo TOKEN = 'Your token here' > config

Загрузите веса моделей в 6 и 7 строчку в файле models (получить веса можно использовав код проекта, Text_Generation) 

model_bad = torch.load('YOUR PATH HERE')
model_good = torch.load('YOUR PATH HERE')

run

python bot

