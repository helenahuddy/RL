Запуск:

docker run -it sequenceiq/hadoop-docker:2.7.1 /etc/bootstrap.sh -bash 
cd $HADOOP_PREFIX

Копирование файлов в докер:

docker cp /Users/helenahuddy/BigData/star2002-sample.csv 65225c58610b:/star2002-sample.csv
docker cp /Users/helenahuddy/BigData/mapper1.py 65225c58610b:/mapper1.py
docker cp /Users/helenahuddy/BigData/mapper2.py 65225c58610b:/mapper2.py
docker cp /Users/helenahuddy/BigData/Reducer1.py 65225c58610b:/Reducer1.py
docker cp /Users/helenahuddy/BigData/Reducer2.py 65225c58610b:/Reducer2.py

Создание директории на hdfs и добавление в неё файла:

hdfs dfs -mkdir small_sample
bin/hdfs dfs -put /star2002-sample.csv ./small_sample/

Запуск для hadoop-streaming:

hadoop jar hadoop-streaming.jar \
> mapper mapper1.py\
> reducer Reducer1.py\
> input small_sample\
> output out1\
[> file mapper1.py\
> file Reducer1.py ]


hadoop jar hadoop-streaming.jar \
> mapper mapper2.py\
> reducer Reducer2.py\
> input small_sample\
> output out1\
[> file mapper2.py\
> file Reducer2.py ]
