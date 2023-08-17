#include <stdio.h>
#include <graphics.h>
void midp(int r, int xc, int yc)
{
    int x, y;
    float d;
    d = 1.25 - r;
    x = 0;
    y = r;
    do
    {
        if (d < 0)
        {
            x = x + 1;
            d = d + 2 * x + 1;
        }
        else
        {
            x = x + 1;
            y = y - 1;
            d = d + 2 * x - 2 * y + 10;
            delay(100);
        }
        putpixel(xc + x, yc + y, 5);
        putpixel(xc - y, yc - x, 6);
        putpixel(xc + y, yc - x, 7);
        putpixel(xc - y, yc + x, 8);
        putpixel(xc + y, yc + x, 9);
        putpixel(xc - x, yc - y, 4);
        putpixel(xc + x, yc - y, 3);
        putpixel(xc - x, yc + y, 2);
    } while (x < y);
}
int main()
{
    int gd = DETECT, gm;
    int xc, yc, r;
    xc = 300;
    yc = 300;
    r = 100;
    initgraph(&gd, &gm, "");
    midp(r, xc, yc);
    delay(1500);
    getch();
    closegraph();
    return 0;
}
