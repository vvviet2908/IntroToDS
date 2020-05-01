x <- c(5,4,4,5,4,4,4,3.5,2,2.5,1.5,2,5,3,3,3,5,5,2)
p <- 1-pnorm(3,mean(x),sd(x))
cat("The probability distribution is", p) 