import quandl
#get data from quandl.com for regression analysis and store it in a dataframe
df=quandl.get('WIKI/GOOGL')
# print(df.head()) to see the entire datasets. I am gonna filter the data by adj open,close, volume columns
df=df[['Adj. Open','Adj. Close','Adj. Volume']]
#define new label of open close percentage
df['PERCENT']=((df['Adj. Close']-df['Adj. Open'])/df['Adj. Open'])*100.0
#print data
print(df.head())