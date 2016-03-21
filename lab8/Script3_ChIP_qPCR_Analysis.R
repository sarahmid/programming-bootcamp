setwd("~/Desktop/Bootcamp")

# Code to plot error bars
error.bar <- function(x, y, upper, lower=upper, length=0.1,...){
  if(length(x) != length(y) | length(y) !=length(lower) | length(lower) != length(upper))
    stop("vectors must be same length")
  arrows(x,y+upper, x, y-lower, angle=90, code=3, length=length, ...)
}

# Read in data
data <- read.delim("Some_Random_ChIP_PCR_Data.txt", stringsAsFactors=F, header=T)
data <- data[, colnames(data) != "Quantity"]
data$Ct[data$Ct == "Undetermined"] <- 40
data$Ct <- as.numeric(data$Ct)

# Outlier detection and exclusion
outlierThresh <- 1

min <- tapply(data$Ct, list(data$Sample.Name, data$Detector.Name), min)
mid <- tapply(data$Ct, list(data$Sample.Name, data$Detector.Name), median)
max <- tapply(data$Ct, list(data$Sample.Name, data$Detector.Name), max)
std <- tapply(data$Ct, list(data$Sample.Name, data$Detector.Name), sd)

# Assuming triplicate data, get min, mid, max indices
idxMin <- tapply(1:nrow(data), list(data$Sample.Name, data$Detector.Name), function(idx) {rnk <- rank(data$Ct[idx], ties.method="first"); idx[which(rnk == 1)]})
idxMid <- tapply(1:nrow(data), list(data$Sample.Name, data$Detector.Name), function(idx) {rnk <- rank(data$Ct[idx], ties.method="first"); idx[which(rnk == 2)]})
idxMax <- tapply(1:nrow(data), list(data$Sample.Name, data$Detector.Name), function(idx) {rnk <- rank(data$Ct[idx], ties.method="first"); idx[which(rnk == 3)]})

idxLowCt  <- which(mid - min >= outlierThresh, arr.ind=T) 
idxHighCt <- which(max - mid >= outlierThresh, arr.ind=T) 

# Get rid of outliers
data <- data[! 1:nrow(data) %in% c(idxMin[idxLowCt], idxMax[idxHighCt]),]

# Standard Curve
data$isStd <- grepl("Input", data$Sample.Name)
stdCurveAnnot <- unique(data[data$isStd, c("Sample.Name", "Detector.Name")])
stdCurveAnnot$Sample.Group <- gsub("_.....$", "", stdCurveAnnot$Sample.Name)
stdCurveAnnot$Quantity <- as.numeric(gsub(".*_", "", stdCurveAnnot$Sample.Name))
stdCurveAnnot <- stdCurveAnnot[order(stdCurveAnnot$Sample.Group, stdCurveAnnot$Detector.Name),]

data <- merge(data, stdCurveAnnot, all.x=T)
data <- data[order(data$Well),]
data$StdGroup <- NA
data$StdGroup[!data$isStd] <- data$Sample.Name[!data$isStd]
data$StdGroup <- gsub("_[^_]*$", "_Input", data$StdGroup)

stdCurveResults <- unique(stdCurveAnnot[,c("Sample.Group", "Detector.Name")])
stdCurveResults$slope <- NA
stdCurveResults$intercept <- NA
stdCurveResults$r.squared <- NA
stdCurveResults$efficiency <- NA
stdCurveResults$MedianCt1x <- NA

pdf("StdCurve.pdf")
for(i in 1:nrow(stdCurveResults)) {
  group    <- stdCurveResults$Sample.Group[i]
  detector <- stdCurveResults$Detector.Name[i]
  samples  <- unique(stdCurveAnnot$Sample.Name[stdCurveAnnot$Sample.Group == group])
  
  stdCurveData <- data[data$Sample.Name %in% samples & data$Detector.Name == detector, ]
  fit <- lm(stdCurveData$Ct ~ log10(stdCurveData$Quantity))
  stdCurveResults$intercept[i] <- fit$coefficients[1]
  stdCurveResults$slope[i] <- fit$coefficients[2]
  stdCurveResults$r.squared[i] <- summary(fit)$r.squared
  stdCurveResults$efficiency[i] <- 10^(-1 / stdCurveResults$slope[i]) - 1
  stdCurveResults$MedianCt1x[i] <- median(stdCurveData$Ct[stdCurveData$Quantity == 1])
  plot(log10(stdCurveData$Quantity), stdCurveData$Ct, xlab="Log10 Quantity", ylab="Ct", main = paste(group, detector, sep=":"))
  abline(fit, lty=2, col="red")
}
dev.off()

# Normalize
for(i in 1:nrow(stdCurveResults)) {
  group    <- stdCurveResults$Sample.Group[i]
  detector <- stdCurveResults$Detector.Name[i]
  idx <- which(data$StdGroup == group & data$Detector.Name == detector)
  log10Quant <- (data$Ct[idx] - stdCurveResults$intercept[i]) / stdCurveResults$slope[i]
  data$Quantity[idx] <- 10^log10Quant
}

# Plot 
final <- data[!data$isStd & data$Sample.Name != "Water",]
group1 <- final$Quantity[final$Sample.Name == "Exp1_LineOfInterest_FavTF" & final$Detector.Name == "FavTFBS"]
group2 <- final$Quantity[final$Sample.Name == "Exp1_LineOfInterest_IgG" & final$Detector.Name == "FavTFBS"]
t.test(group1, group2)

ctMedian <- tapply(final$Quantity*100 / 5, list(final$Sample.Name, final$Detector.Name), median)
ctStDev  <- tapply(final$Quantity*100 / 5, list(final$Sample.Name, final$Detector.Name), sd)

reorder <- c(2, 1, 4, 3, 6, 5, 8, 7)
ctMedian <- ctMedian[reorder,]
ctStDev <- ctStDev[reorder,]

pdf("My_ChIP_Results.pdf")
par(mar = c(5,4,4,1)+0.1)
key <- grep("Exp1", rownames(ctMedian))
bar <- barplot(ctMedian[key,], las=1, cex.names=0.8, beside=T, ylab="Percent Input", main="Experiment 1", ylim=c(0, 20))
error.bar(bar, ctMedian[key,], 1.96 * ctStDev[key,])
legend("topleft", col=gray.colors(nrow(ctMedian)), rownames(ctMedian[key,]), pch=15)

key <- grep("Exp2", rownames(ctMedian))
bar <- barplot(ctMedian[key,], las=1, cex.names=0.8, beside=T, ylab="Percent Input", main="Experiment 2", ylim=c(0, 2.5))
error.bar(bar, ctMedian[key,], 1.96 * ctStDev[key,])
legend("topleft", col=gray.colors(nrow(ctMedian)), rownames(ctMedian[key,]), pch=15)
dev.off()
