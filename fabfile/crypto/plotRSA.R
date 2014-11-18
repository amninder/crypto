# Define 2 vectors
ours <- c(803.031952, 673.387028, 539.739759, 461.6895297, 569.0413317, 432.3660556)

pdf(file="/Users/iNarota/Desktop/encryptionTime.pdf", height=7, width=10)

plot(ours, type="l", col="blue", ylim=c(0,2000), xlab="bits", ylab="Seconds", axes=FALSE, ann=FALSE)
axis(1, at=1:6, lab=c(32, 65, 94, 127, 160, 320))

axis(2)

title(main="", col.main="red", font.main=4, xlab="bits", ylab="miliseconds")

legend("topleft", # places a legend at the appropriate place 
c("Encryption & Decryption Time"), # puts text in the legend 

lty=c(1,1), # gives the legend appropriate symbols (lines)

lwd=c(5,5),col=c("blue","red")) # gives the legend lines the correct color and width

dev.off()











