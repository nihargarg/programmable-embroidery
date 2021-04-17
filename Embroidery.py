# MECE E4606 - Digital Manufacturing
# @Author: Nihar Garg (nng2108), Saritha Krishna Kumar (sk4839)
# @Description: Assignment 3 - PROGRAMMABLE EMBROIDERY

import math

pi = 3.14
max_stitch = 10 #assume max distance between 2 points is 1mm

dimension = 5

def getStitches():
    stitches = [128, 2] # 128 = escape_character -> 2 = Move followed by 8 bit displacement X,Y
    stitches += [0, 0, 30, 30] # spacing
    stitches += square(dimension)
    stitches += zig_zag(square(dimension))
    

    stitches += [0, 0, 30, 80] # spacing
    circle_stitches = circle(dimension)
    stitches += zig_zag(circle_stitches)
    

    stitches += [0, 0, 256-30, 120] # spacing
    stitches += triangle(dimension)
    stitches += zig_zag(triangle(dimension))
       
    # Change thread
    stitches += [128, 1] # 128 = escape_character -> 1 = Change to next thread in list
    stitches += [65, 0, 107, 256-120] # spacing
    iterations = 2
    stitches += zig_zag(fractal())

    stitches += [128, 1] # 128 = escape_character -> 1 = Change to next thread in list
    stitches += [256-30, 50, 256-30, 100] # spacing
    stitches += square(dimension)
    stitches += zig_zag(square(dimension))
    
    
    stitches += [50, 0, 80, 0] # spacing  
    circle_stitches = circle(dimension)
    stitches += zig_zag(circle_stitches)
    
    stitches += [30, 1, 50, 5] # spacing  
    stitches += triangle(dimension)
    stitches += zig_zag(triangle(dimension))
    
    stitches += [128, 1] # 128 = escape_character -> 1 = Change to next thread in list
    stitches += [0, 256-35, 0, 256-50] # spacing
    stitches += square(dimension)
    stitches += zig_zag(square(dimension))
    
    stitches += [10, 256-55, 10, 256-50] # spacing
    circle_stitches = circle(dimension)
    stitches += zig_zag(circle_stitches)
    
    stitches += [0, 256-50, 256-10, 256-20] # spacing
    stitches += triangle(dimension)
    stitches += zig_zag(triangle(dimension))
    
    stitches += [128, 1] # 128 = escape_character -> 1 = Change to next thread in list
    stitches += [256-35, 256-5, 256-50, 256-5] # spacing
    stitches += square(dimension)
    stitches += zig_zag(square(dimension))
    
    stitches += [256-35, 256-3, 256-50, 256-5] # spacing
    circle_stitches = circle(dimension)
    stitches += zig_zag(circle_stitches)
    
    stitches += [256-50, 5, 256-80, 5] # spacing
    stitches += triangle(dimension)
    stitches += zig_zag(triangle(dimension))

    stitches += [256-50, 256-35, 256-50, 256-80] # spacing
    stitches += zig_zag(square(55))
    
    loops = 2
    for n in range(0,loops):
        stitches += [10, 10, 15, 15] # spacing
        stitches += zig_zag(square(50-n*5))

    stitches += [128, 16]   # 128 = escape_character -> 16 = last_stitch 

    #print(stitches)
    return stitches

def fractal():
    fractal_stitches = []

    while True:
        complexity = int(input('Enter the complexity: '))
        #complexity = 3
        if complexity <= 0:
            print ('Please enter a positive number.')
        elif complexity > 7:
            print ('Please enter a complexity less than 7.')
        else:
            break

    while True:
        frac_len = int(input('Enter the fractal length: '))
        #frac_len = 5
        if frac_len <= 0:
            print ('Please enter a positive number.')
        elif frac_len > 5:
            print ('Please enter a fractal length less than 5mm.')
        else:
            break

    for n in range(1, complexity+1):
        for i in range(0,int(frac_len)):
            fractal_stitches += [ max_stitch , 0,]

        for i in range(0,int(frac_len)):
            fractal_stitches += [ 0, max_stitch,]

        frac_len = frac_len*1.25

        for i in range(0,int(frac_len)):
            fractal_stitches += [256-max_stitch, 0,]
        
        for i in range(0,int(frac_len)):
            fractal_stitches += [0, 256-max_stitch,]
        
        frac_len = frac_len*1.25

    return fractal_stitches

def triangle(dimension):
    triangle_stitches = []

    for t in range(0,dimension):
        triangle_stitches += [ int(max_stitch*math.cos(pi/3)), int(max_stitch*math.sin(pi/3)),]
    for t in range(0,dimension):
        triangle_stitches += [ int(max_stitch*math.cos(pi/3)), 256-int(max_stitch*math.sin(pi/3)),]
    for t in range(0,dimension):
        triangle_stitches += [256-max_stitch, 0,]

    return triangle_stitches

def square(dimension):
    square_stitches = []

    for i in range(0,dimension):
        square_stitches += [ max_stitch, 0,]
    for i in range(0,dimension):
        square_stitches += [ 0, max_stitch,]
    for i in range(0,dimension):
        square_stitches += [256-max_stitch, 0,]
    for i in range(0,dimension):
        square_stitches += [0, 256-max_stitch,]

    return square_stitches

def circle(radius):
    circle_stitches = []

    for t in range(0, int(2*pi*100), max_stitch):
        x = int(math.cos(t/100)*radius)
        y = int(math.sin(t/100)*radius)
        if x < 0:
            x = 256 + x
        if y < 0:
            y = 256 + y
        circle_stitches += [x, y]

    return circle_stitches

def zig_zag(stitches):
    #zig_stitches = stitches # shows original pattern as well
    zig_stitches = []

    for i in range(0,len(stitches)-1,2):
        in1x = stitches[i+1]
        in1y = stitches[i]

        in2x = stitches[i]-stitches[i+1]
        in2y = stitches[i+1]-stitches[i]

        if in2x < 0:
            in2x = 256 + in2x
        if in2y < 0:
            in2y = 256 + in2y

        zig_stitches += [in1x, in1y, in2x, in2y]

    return zig_stitches

def getJeffList(stitches):
    jefBytes = [    128, 0, 0, 0,   # The byte offset of the first stitch
                    10, 0, 0, 0,   # unknown command
                    ord("2"), ord("0"), ord("2"), ord("1"), #YYYY
                    ord("0"), ord("2"), ord("2"), ord("4"), #MMDD
                    ord("1"), ord("5"), ord("2"), ord("1"), #HHMM
                    ord("0"), ord("0"), 99, 0, #SS00
                      5, 0, 0, 0,   # Thread count no. (no of thread changes)
                    (len(stitches)//2) & 0xff, (len(stitches)//2) >> 8 & 0xff, 0, 0, # Number of stitches
                      3, 0, 0, 0, # Sewing machine Hoop
                    # Extent 1
                     50, 0, 0, 0, # Left boundary dist from center (in 0.1mm)
                     50, 0, 0, 0, # Top boundary dist from center (in 0.1mm)
                     50, 0, 0, 0, # Right boundary dist from center (in 0.1mm)
                     50, 0, 0, 0, # Bottom boundary dist from center (in 0.1mm)
                    # Extent 2
                     50, 0, 0, 0, # Left boundary dist from center (in 0.1mm)
                     50, 0, 0, 0, # Top boundary dist from center (in 0.1mm)
                     50, 0, 0, 0, # Right boundary dist from center (in 0.1mm)
                     50, 0, 0, 0, # Bottom boundary dist from center (in 0.1mm)
                    # Extent 3
                     50, 0, 0, 0, # Left boundary dist from center (in 0.1mm)
                     50, 0, 0, 0, # Top boundary dist from center (in 0.1mm)
                     50, 0, 0, 0, # Right boundary dist from center (in 0.1mm)
                     50, 0, 0, 0, # Bottom boundary dist from center (in 0.1mm)
                    # Extent 4
                     50, 0, 0, 0, # Left boundary dist from center (in 0.1mm)
                     50, 0, 0, 0, # Top boundary dist from center (in 0.1mm)
                     50, 0, 0, 0, # Right boundary dist from center (in 0.1mm)
                     50, 0, 0, 0, # Bottom boundary dist from center (in 0.1mm)
                    # Extent 5
                     50, 0, 0, 0, # Left boundary dist from center (in 0.1mm)
                     50, 0, 0, 0, # Top boundary dist from center (in 0.1mm)
                     50, 0, 0, 0, # Right boundary dist from center (in 0.1mm)
                     50, 0, 0, 0, # Bottom boundary dist from center (in 0.1mm)
                      9, 0, 0, 0, # Thread Color (pink)
                     12, 0, 0, 0, # Thread Color (green)
                      2, 0, 0, 0, # Thread Color (white)
                      7, 0, 0, 0, # Thread Color (blue)
                      6, 0, 0, 0, # Thread Color (green)
                      8, 0, 0, 0, # Thread Color (green)
                     13, 0, 0, 0, # Thread type (unknown)
                ] + stitches
    return jefBytes

def main():
    print('Welcome to Programmable Embroidery')

    data = bytes(getJeffList(getStitches()))
    with open("nice_design.jef", "wb") as f:
        f.write(data)

if __name__ == '__main__':
    main()