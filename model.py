import pandas 
import sklearn.linear_model from LinearRegression


db = pandas.read_csv("dataset.csv")
X= db["hrs"].values.reshape(-1,1)
Y= db["marks"]

mind = LinearRegression()
mind.fit(X,Y)
hours= int(input("enter the no of hours you study :" ))
print("your marks wil be approx :" ,mind.predict([[hours]]))
