#include <stdio.h>

void drawrect(int w, int h)
{
    int i, j;
    for (i = 0; i < w; i++)
	putchar('x');
    putchar('\n');
    for (i = 2; i < h; i++)
    {
        putchar('x');
        for (j = 2; j < w; j++)
	    putchar(' ');
	putchar('x');
	putchar('\n');
    }
    for (i = 0; i < w; i++)
	putchar('x');
    putchar('\n');
}

int main()
{
    drawrect(10,15);
    drawrect(3,5);
    drawrect(50,20);
    drawrect(10,10);
    drawrect(2,2);
}