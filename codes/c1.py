from pathlib import Path

import pandas as pd

list_ex=['example1','example2','example3','example4']
def group (path_f):
    try:
        
        if path_f in list_ex:
            df=pd.read_csv(f"../datas/{path_f}.csv")
        else:    
            df=pd.read_csv(path_f)
        a=input('Enter col name :')
            
        
        gruop=df.groupby(a)


        size=gruop.size()
        

        sorted_size=size.sort_values(ascending=False)
        return sorted_size

    except KeyError :
        print('col is not defind')
def output(df):
    try:
        sug = input('do you want to export data as a csv file (y:yes):')
        if sug == 'y':
            out_path = input('where do you want to save data:')
            out_name = input("enter output data name(without file name extension):")
            output_path=Path(out_path) / f"{out_name}.csv"
            df.to_csv (output_path,index=True)
            
    except:
        print('error to save data')
            

    