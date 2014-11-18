# Define 2 vectors
ours <- c(0.078310144, 0.033817088, 0.160193792, 2.901262848, 4.219404032)
theirs <- c(0.027386368, 0.320994816, 0.96348288, 10.15514112, 33.8311593)

kara <- c(0.002838, 0.00623, 0.016622, 0.048354, 0.140272, 0.437445, 1.317523, 4.016064)
mul <- c(0.002703, 0.006141, 0.017437, 0.058411, 0.212314, 0.808407, 3.164557, 12.048193)

pdf(file="/Users/iNarota/Desktop/rsaVSjava.pdf", height=7, width=10)

plot(ours, type="l", col="blue", ylim=c(0,50), xlab="bits", ylab="Seconds", axes=FALSE, ann=FALSE)
axis(1, at=1:8, lab=c(8, 16, 32, 64, 128, 256, 512, 1024))

axis(2)

#box()

lines(theirs, type="l", pch=22, lty=1, col="red")

title(main="", col.main="red", font.main=4, xlab="bits", ylab="miliseconds")

legend("topleft", # places a legend at the appropriate place 
c("Our Result","Secure RSA"), # puts text in the legend 

lty=c(1,1), # gives the legend appropriate symbols (lines)

lwd=c(5,5),col=c("blue","red")) # gives the legend lines the correct color and width

dev.off()