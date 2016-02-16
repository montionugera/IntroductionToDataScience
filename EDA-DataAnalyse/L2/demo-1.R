getwd()
setwd('~/WorkSpace/Udemy-Datascience/IntroductionToDataScience/EDA-DataAnalyse/L2')
st_info <- read.csv('stateData.csv')

subset(st_info,state.region == 1)

st_info[st_info$state.region == 1,]

subset(st_info,highSchoolGrad >= 50)

