# scrapper-project


# info

* this code donwloads threat data from threatIntelligenceurls (data.py) and put it in elasticsearch( elastic.py ) then in main.py we will check for next trigger.


![image](https://user-images.githubusercontent.com/39967064/173341879-c41e4295-1448-4c37-8de9-78524088c7cd.png)



# install

the project needs docker for begginnig.

* istalling docker : https://docs.docker.com/get-docker/



# RUN

```
~ docker-compose build
~ docker-compose up -d
```

for see the result of code
```
~ docker logs [container_name] 
```
this project container_name is: searcher_project

