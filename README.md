# Text_Generation_Bot
Бот генерирует добрые и злые новостные заголовки

Установка:
```bash
git clone
```
```python
pip install -r requirements.txt
```
```bash
echo TOKEN = 'Your token here' > config.py
```

Загрузите веса моделей в 6 и 7 строчку в файле models (получить веса можно использовав код проекта, Text_Generation) 
```python
model_news = torch.load('YOUR PATH HERE')
model_congr = torch.load('YOUR PATH HERE')
```
run
```bash
python bot.py
```

