#include <stdio.h> 
 //draws  rectangles// ;
 main  () 
 { 
 int  a ;
 int  b ;
 printf  ("Height:  ") ;
 int  height  =  0 ;
 scanf  ("%d",&height) ;
 printf  ("Width:  ") ;
 int  width  =  0 ;
 scanf  ("%d",&width) ;
 for  (a  =  0;  a  !=  height;  a++) 
 { 
  ;
         for  (b  =  0;  b  !=  width;  b++  ) 
 { 
  ;
                 if  (a  ==  0  ||  a==  height-1  ) 
 { 
                         printf  ("+") ;
               }else{ ;
                         if(b  ==  0  ||  b  ==  width-1){ ;
                                 printf  ("+") ;
                         }else{ ;
                                 printf  ("  ") ;
                        
 } 
              
 } 
        
 } 
  ;
         printf  ("\n") ;

 } 

return 0;
}