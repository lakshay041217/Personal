# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    #print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
    #print_hi('PyCharm'# See PyCharm help at https://www.jetbrains.com/help/pycharm/

#import pandas as pd

#d = {'key' : ['x','y','x','y','z','x'],
#'X':[1,2,3,4,5,6],
#'Y':[5,7,8,9,1,1]
#}

#df = pd.DataFrame.from_dict(d,orient = 'columns')
#print(df)
#df.set_index("key", inplace = True)
#print(df)


if __name__ == '__main__':
    l1 =[]
    for _ in range(int(input())):
        print(_)
        name = input()
        score = float(input())
        l1.append([name,score])

    sorted_score = sorted(set([score for name,score in l1]))[1]
    print(sorted_score)
    l2='\n'.join(sorted([name for name,score in l1 if score ==sorted_score]))
    print(l2)

