docker exec -it a26adcbc0c4e bash

docker exec -it a26adcbc0c4e python model.py



curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"flower":"1,2,3,7"}' \
  http://localhost:5000/iris_post

  docker kill $(docker ps -q)

  echo "# sentiment-flask-docker" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/Rezyapkin-Vyacheslav/sentiment-flask-docker.git
git push -u origin master
