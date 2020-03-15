# zadanie 1 ---------------------------------------------------------------


moja_lista <-
  list(c("Patryk", "Ga³ka"),
       3.14,
       sqrt ,
       c(0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1))
moja_lista[[1]] <- NULL
moja_lista[[2]] <- NULL
lapply(moja_lista, gamma)


# zadanie 2 ---------------------------------------------------------------



macierz <- matrix(c(1, 2, 1, 5, 0, 2, 3, 5, 1), nrow = 3, ncol = 3)
wyznacznik <- det(macierz)
x <- rowMeans(macierz)
y <- rowSums(macierz)
z <- colMeans(macierz)
h <- colSums(macierz)
macierz2 <- macierz %*% solve(macierz)
rankmat <- rankMatrix(macierz)
warwl <- eigen(macierz)

# zadanie 3 ---------------------------------------------------------------

zad3wek <- c(1:100)^2
table(zad3wek%%10)



# zadanie 4 ---------------------------------------------------------------

outer(c(1:5),c(1:5),FUN=function(x, y){{paste(x, "*",y,"=",x*y)}})


