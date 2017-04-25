val day=20
val month=4
val year=2017

val rdd = sc.cassandraTable("testing", "all_tweets")


val list = scala.collection.mutable.MutableList[String]()


rdd.filter(row => row.getInt("created_at_month").equals(month)&&row.getInt("created_at_day").equals(day)&&row.getInt("created_at_year").equals(year)).map{row => row.getSet[String]("hashtags")}.collect.foreach(set => set.map{tag => tag.toLowerCase}.foreach(item => list += item))


val dict=list.groupBy(l => l ).map(item => (item._1, item._2.length))
val sortedList=dict.toList.sortBy(_._2)
sortedList.foreach(println)

