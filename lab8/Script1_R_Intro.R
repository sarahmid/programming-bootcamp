### R basics. This code is designed to run line by line and teach the basics of R
## 1. Evaluating basic expressions
1+1 # No surprises...

## 2. Variable assignment
x <- 7*12+2                 # A scalar
mystr <- "Hello World!"     # A string
myvec <- c(1,8,3,2,6,4,5,7) # A (numeric) vector

## 3. Multiple ways to print
print(x) 
x        # This is equivalent to print(x), so why type more when you don't have to?
mystr    # Equivalent to print(mystr)
myvec    # Equivalent to print(myvec)

## 4. Mixing data types
mixvec <- c(1, 'a', 3)      
mixvec                      # Oops! All the data got "promoted" to strings... 
mixlist <- list(1, 'a', 3)
mixlist                     # Data types are preserved in a list

## 5. Vector assignment
# These are all equivalent
myvec <- c(1,2,3,4,5,6,7,8)
myvec <- seq(1,8)
myvec <- 1:8
myvec 

## 6. How to ask R for help
# These are both equivalent
help(seq) # This works for any function! :) Try it on some others!
?seq      # This works for any function! :) Try it on some others!

# Based on the documentation, let's make a different sequence...
seq(1, 8, 2) # How would you change this to get the even numbers?

## 7. Vectorization in R
myvec # Let's remind ourselves what myvec is by printing it

myvec + 1 # What does this do?
myvec * 3 # How about this?
1 / myvec # And this?

# Let's make some big vectors
bignum <- 10000000
x <- 1:bignum
y1 <- rep(NA, bignum)
y2 <- rep(NA, bignum)

# The following two lines of code accomplish the same thing, but the
# 1st line takes advantage of vectorization whereas the 2nd does not.
# We call system.time() on each expression to see the runtime of each in seconds
system.time(y1 <- x + 1)                          # FAST!!!
system.time(for(i in 1:bignum) y2[i] <- x[i] + 1) # Very slow... don't do this!

all(y1 == y2) # Just to prove that y2 

## 8. A few useful functions
sum(myvec)
mean(myvec)
sd(myvec)
max(myvec)
min(myvec)
sample(myvec,4)
sample(myvec,4, replace=T)
rep(myvec, 3)
rep(myvec, each=3)
matrix(myvec,nrow=2)#column major
myvec[myvec>3]
myvec[myvec==5]

## 9. Writing our own functions in R
mymean <- function(x) sum(x) / length(x)
mysd <- function(x) {
  sumsq <- sum((x - mean(x))^2)
  return(sqrt(sumsq / (length(x) - 1)))
}
mymax <- function(x) sort(x)[length(x)]
mymin <- function(x) sort(x)[1]

mymean(myvec) == mean(myvec) 
mysd(myvec) == sd(myvec) 
mymin(myvec) == min(myvec) 
mymax(myvec) == max(myvec) 

## 10. Loading and manipulating tabular data
# Using read.table() to load tabular data in R
setwd("") # Set your working directory to where the data is
data <- read.table("genes.table", header=TRUE) # Always make sure to use the right header argument!
dim(data)
summary(data)

# Subselecting your data
head(data)
tail(data)
data[72,]
data[,3]
data[72:82,1:3]

# Let's look at a histogram of geneA...
hist(data$geneA, freq=FALSE)
aMean <- mean(data$geneA)
aSd <- sd(data$geneA)

# Looks pretty "normal" and centered at zero, but let's check a few things...
curve(dnorm(x, mean = 0, sd = 1), add = T) # Seems to fit the "standard normal" curve okay
t.test(data$geneA, mu = 0)                 # We don't reject the null hypothesis that mean == 0

# Two-sample T-tests are also easy
t.test(data$geneA, data$geneB)
t.test(data$geneA, data$geneD)

# Basic linear regression
plot(data$geneA, data$geneB)
regline <- lm(data$geneB ~ data$geneA) # Calculate the linear regression of geneB vs geneA
abline(regline, col="red") # Add regression line to plot
summary(regline) # This is useful for getting p-values, R^2, etc

# Fun with boxplots
boxplot(data$geneA, data$geneB, data$geneC, data$geneD) # Too long
boxplot(data) # This works better

# Plotting multi-panel figures
par(mfrow=c(2,2)) # Give me a 2x2 panel
xmin <- min(data)
xmax <- max(data)
hist(data$geneA, col="green", freq=FALSE, xlim=c(xmin,xmax), ylim=c(0,0.5), breaks=15)
hist(data$geneB, col="red",   freq=FALSE, xlim=c(xmin,xmax), ylim=c(0,0.5), breaks=15)
hist(data$geneC, col="black", freq=FALSE, xlim=c(xmin,xmax), ylim=c(0,0.5), breaks=15)
hist(data$geneD, col="blue",  freq=FALSE, xlim=c(xmin,xmax), ylim=c(0,0.5), breaks=15)

# Make a scatter plot of gene expression vs. sample for each gene in data
par(mfrow=c(1,1))
samples <- 1:nrow(data)
plot(samples,   data$geneA, col="green", pch=20, ylim=c(xmin,xmax), xlab="Samples", ylab="Expression Level")
points(samples, data$geneB, col="red",   pch=22)
points(samples, data$geneC, col="black", pch=23)
points(samples, data$geneD, col="blue",  pch=24)
legend("topright", legend=c("geneA","geneB","geneC","geneD"), pch=c(20,22,23,24), col=c("green","red","black","blue"))

# Data subselection
data$geneA <= -2        # Returns boolean vector
which(data$geneA <= -2) # Returns indexes where boolean vector is TRUE

# These are equivalent ways of subselecting elements where geneA < -2
data$geneA[which(data$geneA <= -2)]
data$geneA[data$geneA <= -2]
data[which(data[,1] <= -2),1]
data[data[,1] <= -2,1]
data[which(data[,1] <= -2),"geneA"]
data[data[,1] <= -2,"geneA"]

# Ordering data
sort(data$geneA) # This orders our data, but what if we want to reorder the whole table?
order(data$geneA) # This is an ordering permutation, and turns out to be far more useful...

sort(data$geneA) == data$geneA[order(data$geneA)] # These are equivalent

data <- data[order(data$geneA),] # We've reordered our table!
head(data, 20)                   # Let's check the first 20 elements to see what happened

data <- data[order(data$geneA, data$geneB),] # Nested orderings are also possible, and this is the syntax

# 11. Apply functions are (very very) useful
apply(data, 1, mean) # This computes row means efficiently across our table
apply(data, 2, mean) # This computes col means efficiently across our table

mylist <- list('a', 1:8, data)
lapply(mylist, length) # Use lapply for lists

# Just making up some data for illustration here
df <- data.frame(
  Condition = rep(c("Cond1", "Cond2", "Cond3", "Cond4", "Cond5"), 3),
  Genes = rep(c("GeneA", "GeneB", "GeneC"), each=5),
  Data = 1:60
)
df # Print the data frame, to show what was built in the code immediately above

# Use tapply to compute efficiently over categorical variables
tapply(df$Data, df$Condition, mean)
tapply(df$Data, df$Genes, mean)
tapply(df$Data, list(df$Genes, df$Condition), mean)

# Use the table() function to get category counts (i.e. make contingency tables)
table(df$Genes)
table(df$Condition)
table(df$Genes, df$Condition)

