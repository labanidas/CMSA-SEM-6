#include <stdio.h>
#include <stdlib.h>
#include <graphics.h>

void scaleTriangle(int x1, int y1, int x2, int y2, int x3, int y3, float sx, float sy)
{
    int newX1, newY1, newX2, newY2, newX3, newY3;

    newX1 = x1 * sx;
    newY1 = y1 * sy;
    newX2 = x2 * sx;
    newY2 = y2 * sy;
    newX3 = x3 * sx;
    newY3 = y3 * sy;

    line(newX1, newY1, newX2, newY2);
    line(newX2, newY2, newX3, newY3);
    line(newX3, newY3, newX1, newY1);
}
int main()
{
    int gd, gm;
    gd = DETECT;
    initgraph(&gd, &gm, NULL);

    // Original triangle coordinates
    //    int x1 = 250, y1 = 100;
    //    int x2 = 300, y2 = 200;
    //    int x3 = 200, y3 = 200;
    int x1 = 200, y1 = 200;
    int x2 = 100, y2 = 300;
    int x3 = 300, y3 = 300;

    float sx = 2, sy = 2;

    // Draw the original triangle
    line(x1, y1, x2, y2);
    line(x2, y2, x3, y3);
    line(x3, y3, x1, y1);
    setcolor(YELLOW);
    // Scale the triangle
    scaleTriangle(x1, y1, x2, y2, x3, y3, sx, sy);
    getch();
    closegraph();
    return 0;
}
