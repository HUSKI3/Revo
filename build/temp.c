#include <stdio.h> 
 int main() { //Revo  version  1.0.4  numberswapper.rv// ;
 double  first,  second,  temp   ;
 printf  ("Enter  first  number:  ")   ;
 scanf  ("%lf",  &first)   ;
 printf  ("Enter  second  number:  ")   ;
 scanf  ("%lf",  &second)   ;
 temp  =  first   ;
 first  =  second   ;
 second  =  temp   ;
 printf  ("\nAfter  swapping,  firstNumber  =  %.2lf\n",  first)   ;
 printf  ("After  swapping,  secondNumber  =  %.2lf\n",  second)   ;

return 0;
}