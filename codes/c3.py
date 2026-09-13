import matplotlib.pyplot as plt
import pandas as pd

list_ex = ["example1", "example2", "example3", "example4"]


def bar_plot(path_f):

    try:
        if path_f in list_ex:
            df = pd.read_csv(f"../datas/{path_f}.csv")
        else:
            df = pd.read_csv(path_f)
        label= input("enter label col: ")
        data = input("enter value col: ")

        plt.bar(df[label], df[data])
        plt.show()

    except KeyError :
        print('col is not defind')
