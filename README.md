### Columbia University in the City of New York
### The Fu Foundation School of Engineering and Applied Science
### Digital Manufacturing

# Embroidery in Python

## Executive Summary

The goal of this project was to perform software-controlled manufacturing. We wrote software that generated an embroidery JEF file to be produced using an automated embroidery machine.

## Software Description

### Design Concept:

The first section shows a simple circle pattern. The code for this pattern can be found in Appendix 1. Next, we decided to create a design that involves multiple shapes and a fractal. A rough sketch of the design is shown below.

### Code Logic:

The JEF file was created using python code. It is important to note that all dimensions mentioned in the code are in units of mm. The following functions were created to help with the pattern creation:
-	Fractal: For a user defined complexity (i.e. number of fractal repetitions), and fractal initial length, creates the fractal pattern shown in Figure 2-1. This function also has error checks to make sure that the complexity is less than 7 and length less than 5mm due to size constraints of the pattern. It also ensures user inputs are valid. The user can also specify if they want the fractal to have a zig zag pattern or not.
-	Triangle: This creates an equilateral triangle pattern by using cosine relation. There are three loops that create the 3 sides.
-	Circle: This creates the circular patterns by finding each x and y coordinate through the use of sine and cosine for different angles. 
-	Square: This has 4 for loops that create each side of the square. 
-	Zig_zag: This creates zig zag stitch type for each pattern. The logic used to create this was that we took 2 consecutive points, drew a perpendicular line to a line connecting the points and then found the difference of spacing between them. 
-	getStitches: Calls the various pattern creation functions mentioned above in varying order to create the design shown in Figure 2-1. This is the place where the location of each shape, and the thread color are specified. The function returns an array of stitches.
-	getJeffList: Takes the stitches array to create JEF code.
-	main: Passes the getStitches return array into the getJeffList to create a JEF file called nice_design.jef

The User can define certain parameters pertaining to the fractal. These factors are:
-	Initial Fractal length (needs to be 1-5 mm)
-	Complexity – fractal repetition number (needs to be 1-7)
-	Fractal stitch type (regular/ zig-zag)

1.	Import the math library to perform numerical calculations
2.	Define Parameters like pi value, max_stitch, dimension, and border_dimension. Max_stitch refers to the length of a single stitch while dimension and border_dimension refers to the length of elements and border respectively. 
3.	The getStitches function calls all the pattern creation function to create the design.
4.	Some of the parameters are user defined as mentioned above.
5.	The main function passes getStitches return array into the getJeffList function to create the nice_design JEF file.
