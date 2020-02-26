To run with docker:

unzip the project and go to directory:
cd arsens-test

To build the Docker image:
$ docker build -t arsens-test .

To run the Docker image, run the following:
$ docker run -it -p 8081:8081 -v $(pwd):/app  arsens-test

(For port I have chosen 8081, because my 8080 was busy with another application)

Now you should be able to access the API at http://localhost:8081/

Here you will see statistical data for mean, reading count, variance.
Try to add(post) some data and see that numbers will be updated

Request endpoints:

GET:
curl -i -u arsens:python http://localhost:8081/api/tasks

GET particular task:
curl -i -u arsens:python http://localhost:8081/api/tasks/2

POST:
curl -i -u arsens:python -H "Content-Type: application/json" -X POST -d '{"value":32.46}' http://localhost:8081/api/tasks

PUT:
curl -i -u arsens:python -H "Content-Type: application/json" -X PUT -d '{"value":11.12}' http://localhost:8081/api/tasks/3

DELETE:
curl -i -u arsens:python -H "Content-Type: application/json" -X DELETE http://localhost:8081/api/tasks/3

Run pytest:
pytest test-pytest.py
