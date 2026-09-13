import matplotlib.pyplot as plt
import pandas as pd

list_ex=['example1','example2','example3','example4']
def line_plot (path_f):
    
    try :
        if path_f in list_ex:
            df=pd.read_csv(f"../datas/{path_f}.csv")
        else:    
            df=pd.read_csv(path_f)
        x=input('enter x col: ')
        y=input('enter y col: ')

        plt.plot(df[x],df[y])
        plt.show()
    except:
        print('unknown prompt')
    