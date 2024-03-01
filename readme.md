# Система обучения

## 1. Описание проекта:
 по организации системы обучения

## 2. Установка и запуск

### Клонируйте репозитторий и перейдите в корень проекта:
- git clone https://github.com/gubkobob/system_of_learning.git
- cd system_of_learning
### Для запуска :
- наберите в терминале в корне проекта
   * docker compose up --build
### Для работы с приложением необходимо создать суперюзера для этого:
- в другом окне терминала набираем
    * docker-compose run app python3 manage.py createsuperuser
### Все, можно пользоваться 
### Для удобства заполнения данных слелана админ панель по адресу
    * http://0.0.0.0:8000/admin/
## 3. Комментарии:
### Группы создаются автоматически при добавлении доступа юзера к продукту по адресу
 * http://0.0.0.0:8000/<int:product_pk>/add_student/<int:user_pk>
###  Когда место в группе закончилось, создается новая, и при условиях задания происходит переопределение в группах

###  API на список продуктов, доступных для покупки
- http://0.0.0.0:8000/products
###  API с выведением списка уроков по конкретному продукту к которому пользователь имеет доступ:
- http://0.0.0.0:8000/products/<int:product_pk>/lessons
###  API для отображения статистики по продуктам
- http://0.0.0.0:8000/products/statistic
