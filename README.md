# Data-Cleaning

Perform some data cleaning using the provided file, “patent_drawing.csv”. “Patent_drawing.csv” contains a list of patents and a short description of each drawing included with a patent grant. For example, patent number 0233365 (https://patents.google.com/patent/US20030233365A1/en) has 16 images. For each image, there is a brief description of the drawings. The description is included in the “text” field in patent_drawing.csv. 

Let’s say that we are interested in understanding:
How many of the field descriptions reference a perspective that is not standard (i.e. viewed from the top, bottom, front or rear)? Specifically, write code to count how many of the rows have the words "view" or "perspective" but do not include "bottom", "top", "front" or "rear" in  the text field?

What is the average number of drawing descriptions per patent? 
