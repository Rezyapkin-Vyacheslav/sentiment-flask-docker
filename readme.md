<<<<<<< HEAD
docker exec -it a26adcbc0c4e bash
=======
Веб-сервис для демонстрации заказчику модели сентимент-анализа отзывов на кино 















docker exec -it flask-hello_flask_1 bash
>>>>>>> 84b7e354aedd9c3b36b5184ae4c9949cae10f902

docker exec -it a26adcbc0c4e python model.py



curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"flower":"1,2,3,7"}' \
  http://localhost:5000/iris_post

  docker kill $(docker ps -q)
<<<<<<< HEAD

  echo "# sentiment-flask-docker" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/Rezyapkin-Vyacheslav/sentiment-flask-docker.git
git push -u origin master
=======
>>>>>>> 84b7e354aedd9c3b36b5184ae4c9949cae10f902
