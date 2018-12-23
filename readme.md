Веб-сервис для демонстрации заказчику модели сентимент-анализа отзывов на кино.

Чтобы запустить сервис на своем localhost'e необходимо:
1. Установить докер
2. В директории со скачанным проектом выполнить комманду $ docker-compose up --build

Теперь по адресу https://localhost:5000 доступна приветственная страница, а по адресу https://localhost:5000/sentiment-demo - страница с демонстрацией модели.

Возможно, сервис сейчас крутится на http://ec2-3-17-128-84.us-east-2.compute.amazonaws.com:5000/sentiment-demo
















docker exec -it flask-hello_flask_1 bash

docker exec -it a26adcbc0c4e python model.py

docker kill $(docker ps -q)

git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/Rezyapkin-Vyacheslav/sentiment-flask-docker.git
git push -u origin master

ssh -i "seti.pem" ec2-user@ec2-3-17-128-84.us-east-2.compute.amazonaws.com
