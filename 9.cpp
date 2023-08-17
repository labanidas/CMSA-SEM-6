
#include <conio.h>
#include <graphics.h>
#include <stdio.h>
int main()
{
    int gd = DETECT, gm;
    int x, y, x1, y1, x2, y2, tx, ty;
    x = 200;
    y = 200;
    x1 = 100;
    y1 = 300;
    x2 = 300;
    y2 = 300;
    initgraph(&gd, &gm, "");
    line(x, y, x1, y1);
    line(x1, y1, x2, y2);
    line(x2, y2, x, y);
    tx = 50;
    ty = 50;
    setcolor(RED);
    line(x + tx, y + ty, x1 + tx, y1 + ty);
    line(x1 + tx, y1 + ty, x2 + tx, y2 + ty);
    line(x2 + tx, y2 + ty, x + tx, y + ty);
    getch();
    closegraph();
}
