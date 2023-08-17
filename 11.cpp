#include <graphics.h>
void scaleTriangle(int x1, int y1, int x2, int y2, int x3, int y3, float sx, float sy)
{
    int cx = (x1 + x2 + x3) / 3;
    int cy = (y1 + y2 + y3) / 3;
    // Calculate the scaled coordinates with respect to the centroid
    int nx1 = cx + (x1 - cx) * sx;
    int ny1 = cy + (y1 - cy) * sy;
    int nx2 = cx + (x2 - cx) * sx;
    int ny2 = cy + (y2 - cy) * sy;
    int nx3 = cx + (x3 - cx) * sx;
    int ny3 = cy + (y3 - cy) * sy;

    // Draw the scaled triangle
    line(nx1, ny1, nx2, ny2);
    line(nx2, ny2, nx3, ny3);
    line(nx3, ny3, nx1, ny1);
}
int main()
{
    int gd = DETECT, gm;
    initgraph(&gd, &gm, "");

    // Original triangle coordinates
    int x1 = 200, y1 = 200;
    int x2 = 100, y2 = 300;
    int x3 = 300, y3 = 300;

    // Scaling parameters
    float sx = 2;
    float sy = 2;

    // Draw the original triangle
    line(x1, y1, x2, y2);
    line(x2, y2, x3, y3);
    line(x3, y3, x1, y1);
    setcolor(YELLOW);
    // Scale the triangle and draw the scaled triangle
    scaleTriangle(x1, y1, x2, y2, x3, y3, sx, sy);
    getch();
    closegraph();
    return 0;
}