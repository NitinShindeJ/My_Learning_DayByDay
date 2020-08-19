def my_data():
    indf = input('Give the Name Of Excel File: ')
    #global inSup, inCat
    inSup = input('Give Supplier Name: ')
    inCat = input('Give Catalog ID: ')
    global df 
    df = pd.read_excel(indf+'.xlsx')