#include <stdio.h>
#include <conio.h>
#include <graphics.h>

// Hermite curve function
int hermite(int p0, int p1, int r0, int r1, double t) {
    double t2 = t * t;
    double t3 = t2 * t;
    
    // Hermite basis functions
    double h1 = 2 * t3 - 3 * t2 + 1;
    double h2 = -2 * t3 + 3 * t2;
    double h3 = t3 - 2 * t2 + t;
    double h4 = t3 - t2;
    
    // Calculate and return the point on the Hermite curve
    return (int) (h1 * p0 + h2 * p1 + h3 * r0 + h4 * r1);
}

int main() {
    int gd = DETECT, gm;
    initgraph(&gd, &gm, "C:\\TC\\BGI"); // Update the path according to your setup
    
    int p0x = 100, p0y = 100; // Start point
    int p1x = 400, p1y = 400; // End point
    int r0x = 200, r0y = 200; // Start tangent
    int r1x = 300, r1y = 100; // End tangent
    
    double t;
    int x, y;
    
    setcolor(WHITE);
    line(p0x, p0y, p1x, p1y); // Draw the control line in white
    
    setcolor(YELLOW);
    for (t = 0; t <= 1; t += 0.01) {
        x = hermite(p0x, p1x, r0x, r1x, t);
        y = hermite(p0y, p1y, r0y, r1y, t);
        putpixel(x, y, YELLOW);
    }
    
    getch();
    closegraph();
    return 0;
}

