#include <stdio.h>
#include <conio.h>
#include <graphics.h>

// Define the clipping window coordinates
int xmin = 100, ymin = 100;
int xmax = 400, ymax = 300;

// Define the region codes
#define INSIDE 0
#define LEFT 1
#define RIGHT 2
#define BOTTOM 4
#define TOP 8

// Calculate the region code for a given point
int calculateRegionCode(int x, int y) {
    int code = INSIDE;
    
    if (x < xmin)
        code |= LEFT;
    else if (x > xmax)
        code |= RIGHT;
    
    if (y < ymin)
        code |= BOTTOM;
    else if (y > ymax)
        code |= TOP;
    
    return code;
}

// Clip the line using the Cohen-Sutherland algorithm
void cohenSutherlandClip(int x1, int y1, int x2, int y2) {
    int code1 = calculateRegionCode(x1, y1);
    int code2 = calculateRegionCode(x2, y2);
    int accept = 0;
    
    while (1) {
        if ((code1 == 0) && (code2 == 0)) {
            accept = 1; // Line is completely inside the window
            break;
        } else if (code1 & code2) {
            break; // Line is completely outside the window
        } else {
            int x, y;
            int code = (code1 != 0) ? code1 : code2;
            
            if (code & TOP) {
                x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1);
                y = ymax;
            } else if (code & BOTTOM) {
                x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1);
                y = ymin;
            } else if (code & RIGHT) {
                y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1);
                x = xmax;
            } else if (code & LEFT) {
                y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1);
                x = xmin;
            }
            
            if (code == code1) {
                x1 = x;
                y1 = y;
                code1 = calculateRegionCode(x1, y1);
            } else {
                x2 = x;
                y2 = y;
                code2 = calculateRegionCode(x2, y2);
            }
        }
    }
    
    if (accept) {
        setcolor(YELLOW);
        line(x1, y1, x2, y2); // Display the clipped line in yellow
    }
}

int main() {
    int gd = DETECT, gm;
    initgraph(&gd, &gm, "C:\\TC\\BGI"); // Update the path according to your setup
    
    setcolor(WHITE);
    rectangle(xmin, ymin, xmax, ymax); // Display the clipping window in white
    
    // Define the line endpoints
    int lines[][4] = {
        {150, 275, 300, 150},   // Line 1
        {300, 350, 450, 350},   // Line 2
        {200, 50, 500, 250}     // Line 3
    };
    
    // Display and clip each line
    for (int i = 0; i < sizeof(lines) / sizeof(lines[0]); i++) {
        int x1 = lines[i][0];
        int y1 = lines[i][1];
        int x2 = lines[i][2];
        int y2 = lines[i][3];
        
        setcolor(RED);
        line(x1, y1, x2, y2); // Display the original line in red
        
        cohenSutherlandClip(x1, y1, x2, y2); // Clip the line
    }
    
    getch();
    closegraph();
    return 0;
}

