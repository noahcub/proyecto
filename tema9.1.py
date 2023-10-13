import pandas as pd
from sklearn.linear_model import LinearRegression

datos = r'/home/noe/Git_Repos/inap/Datos-tema9/Advertising.csv'
data = pd.read_csv(datos)
print(data.head())


x_pred = data[['TV', 'Radio']]
y = data['Sales']

lm = LinearRegression()
lm.fit(x_pred, y)

print(lm.intercept_)
print(lm.coef_)
print(lm.score(x_pred, y))