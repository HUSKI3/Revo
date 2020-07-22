#include <stdio.h> 
 int main() { printf  ("REVO  compiled  code\n") ;
  ;
 FILE  *file ;
 char  c[1000] ;
  ;
 file  =  fopen  ("wow","r") ;
 fscanf  (file,"%[^\n]",  c) ;
 printf  (c) ;
  ;

return 0;
}