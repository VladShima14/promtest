В тестовому завданні виконані тести на додавання товару в список бажених
Тест кейси описані за посиланням https://docs.google.com/spreadsheets/d/1vNY2-6cQCnp8GAIdeoVkapJ60S_Aq831x7bKcp5zpdk/edit?usp=sharing

Для звітноcті з результатами запуску тестів був доданий allure.

Для запуску тестів треба виконати такі кроки:
1) git clone https://github.com/VladShima14/promtest.git
2) pip3 install -r requirements.txt
3) перейти до папки /tests
4) Виконати команди для запуску тестів:
    - Запустити тести з одним, який впаде. Зроблено, щоб подивитись, як в allure відображається скріншот та url при падінні тесту.  
      pytest -v 

    - Запустити тільки тести, які проходять успішно.
      pytest -v -k "not with_error"
5) Щоб подивитись звіт з виконанням тестів:
   allure serve allure-results/
