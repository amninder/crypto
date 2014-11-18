mean=579.8759425;
sd=416.2212605;
x=seq(mean-4*sd, mean+4*sd, length=200);
y=dnorm(x, mean=mean, sd=sd);
plot(x, y, type="l", xlab="Encryption and decryption / second", ylab="");
title("Secure RSA Normal Distribution");
dev.copy(jpeg,filename="plotRandomNumber.jpg");
dev.off ();