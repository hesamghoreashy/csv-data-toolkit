import sys

import c1
import c2
import c3

if sys.argv[1] == "group":
    print(c1.group(sys.argv[2]))# type: ignore
    c1.output()
elif sys.argv[1] == "line_plot":
    c2.line_plot(sys.argv[2])
elif sys.argv[1]== 'bar_plot':
    c3.bar_plot(sys.argv[2])
elif sys.argv[1] == '--help' :
    out="""
    type [group] for grouping data and then type  your csv file path with file name extension
    or type (example1,example2,example3,example4) for using our testing data.
    type [line_plot] for drawing line plot of your data and then type  your csv file path with file name extension
    or type (example1,example2,example3,example4) for using our testing data.
    type [bar_plot] for drawing bar plot of your data and then type  your csv file path with file name extension
    or type (example1,example2,example3,example4) for using our testing data.
    type [--version] for see version of software.
    Thank you for using my code Hesam Ghoreashy 2026.
    """
    print(out)
    
elif sys.argv[1] == '--version' :
    print('1.0.0 by Hesam Ghoreashy')
    
    

else:
    print("unknown prompt")
a = input("press enter to exit:")
