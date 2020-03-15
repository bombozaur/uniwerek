#zadanie 1 ####

#istneije 


#zadanie 2 ####


x<-c(rep( TRUE, 3), rep(FALSE,5), rep(TRUE,2),rep(FALSE,5))
y<-x*1



# zadanie 3 ---------------------------------------------------------------

d<-c(rep(1:20),rep(0,10),seq(22,42,by=2))

b<-rev(d)
f<-c(d,b)

# zadanie 4 ---------------------------------------------------------------
l<-c(letters[5],letters[10],letters[15] ,letters[20],letters[25])
h<-c(letters[seq(5,25, by=5)])

# zadanie 5 ---------------------------------------------------------------
tys<-1:1000
tys[tys%%2==0]=1/tys[tys%%2==0]


# zadanie 6 ---------------------------------------------------------------

wek<-c(6,3,4,5,2,3)
weksor<-order(wek,decreasing=TRUE)
