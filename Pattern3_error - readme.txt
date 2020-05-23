Unfortunately, there is an error in the pattern3 package. This means you will most likely get an error message when running "make". This is something you can easily fix by running the following code in your command line.


--- Please run the following command line for Mac: ---

sed -i '' '36s/.*/    pass/' <path where error occured> 


example: 

sed -i '' '36s/.*/    pass/' /Users/johnsmith/opt/anaconda3/lib/python3.7/site-packages/pattern3/text/tree.py



--- Please run the following command line for Windows: ---

sed -i 36s/.*/    pass/' <path where error occured> 


example:

sed -i '36s/.*/    pass/' /Users/johnsmith/opt/anaconda3/lib/python3.7/site-packages/pattern3/text/tree.py



--- If this does not work ---

Please go to the file where the error came from, and type:
	pass
in the 36th line. 
