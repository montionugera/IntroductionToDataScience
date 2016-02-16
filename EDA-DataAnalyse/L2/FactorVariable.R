getwd()
setwd('~/WorkSpace/Udemy-Datascience/IntroductionToDataScience/EDA-DataAnalyse/L2')
reddit <- read.csv('reddit.csv')
reddit
table(reddit$employment.status)
summary(reddit)
levels(reddit$age.range)
set.seed(124)
schtyp <- sample(0:1, 20, replace = TRUE)
is.factor(schtyp)
is.numeric(schtyp)
install.packages('ggplot2', dep = TRUE)
library(ggplot2)
qplot(data = reddit,x = age.range)
levels(reddit$gender)
levels(reddit$military.service)
levels(reddit$children)
levels(reddit$country)
levels(reddit$state)
levels(reddit$income.range)
levels(reddit$cheese)

schtyp.f <- c((schtyp, labels = c("private", "public"))
is.factor(schtyp.f)
ses <- c("low", "middle", "low", "low", "low", "low", "middle", "low",
         "middle", "middle", "middle", "middle", "middle", "high", "high",
         "low", "middle", "middle", "low", "high")

is.factor(ses)
ses.f.bad.order <- factor(ses)
is.factor(ses.f.bad.order)
levels(ses.f.bad.order)
ses.f <- factor(ses, levels = c("low", "middle", "high"))
is.factor(ses.f)
levels(ses.f)
ses.order <- ordered(ses, levels = c("low", "middle", "high"))

reddit$age.range <- ordered(reddit$age.range, levels = 
                              c("Under 18", "18-24", "25-34", "35-44",
                                "45-54", "55-64", "65 or Above"))

qplot(data = reddit,x = age.range)
