#====================================================================
# Sarah Middleton
# 
# graph_gc.r
#====================================================================

#get command line args
args<-commandArgs(TRUE) 
inFile <- args[1]

# graph gc content
library('ggplot2')
tab <- read.table(inFile, header=T)

png('gc_content_dist.png')
ggplot(tab, aes(x=GC)) + geom_density() + ggtitle("Distribution of GC content across sequences") 
dev.off()

