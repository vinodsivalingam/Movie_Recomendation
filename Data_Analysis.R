mov_results <- read.csv(file = file.choose(),header = FALSE,sep=",")
str(mov_results)
z <- mov_results[,-c(1,1)]
m<- apply(z,2,mean)
s <- apply(z,2,sd)
z<- scale(z,m,s)
z

## increasing printing size on console
options(max.print= 99999999)

## print tail or head rows
tail(mov_results,n=50)
head(mov_results,n=10)
head(z,n=10)
length(readLines(file = file.choose()))

## perform Z-normalization on the file
library(clusterSim)
data(mov_results)
z1 <- data.Normalization(mydata,type="n1")
,normalization="column")

mydata = read.csv(file = file.choose())
data(mydata)
tail(mydata,n=20)
head(mydata,n=10)
write.csv(z1, file= "M:\\ZnormalizedData.csv")
round(mov_results,2)

## convert Factor data to numeric data
df <- data.frame(mov_results$X1,mov_results$X1488844,mov_results$X3)
df<- round(df,2)
head(df,n=100)
df <- read.csv(file = file.choose(),header = FALSE,sep=",")
df$V4 <- round(df$V4,2)	
str(df)
df[, 4] <- as.numeric(as.character( df[, 4] ))
write.csv(df, file= "M:\\ZnormalizedData.csv")
 


