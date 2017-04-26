val rdd=sc.cassandraTable("fromdjango", "trend_tweet")

var year=2017
var month=4
for( day <- 1 to 31){

var list = scala.collection.mutable.MutableList[String]()


rdd.filter(row => row.getInt("created_at_month").equals(month)&&row.getInt("created_at_day").equals(day)&&row.getInt("created_at_year").equals(year)).map{row => row.getSet[String]("hashtags")}.collect.foreach(set => set.map{tag => tag.toLowerCase}.foreach(item => list += item))


val dict=list.groupBy(l => l ).map(item => (item._1, item._2.length))
val sortedList1=dict.toList.sortBy(_._2)
val sortedList= sortedList1.takeRight(10)

println(year.toString+' '+ month.toString+' '+day.toString )
sortedList.foreach(println)

if(sortedList.size>0){
sortedList.map{case (hash,count)=>hash+ count.toString }
/* case class Trend(created_at_year: Int, created_at_month: Int, created_at_day: Int) */
val rrdout= sc.parallelize(Seq((year, month, day,sortedList)))
rrdout.saveToCassandra("trendcount","test2", SomeColumns("created_at_year","created_at_month","created_at_day","mystring"))
}
}
