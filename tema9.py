import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
from sklearn.feature_selection import RFE
from sklearn.svm import SVR

datos = r'/home/noe/Git_Repos/inap/Datos-tema9/Advertising.csv'

data = pd.read_csv(datos)
print(data.head())

data.plot(kind='scatter', x='TV', y='Sales')
#plt.show()

lm = smf.ols(formula='Sales~TV', data=data).fit()
print(lm.params)
print(lm.summary())

lm2 = smf.ols(formula='Sales~TV+Newspaper', data=data).fit()
print(lm2.params)
print(lm2.summary())

x = data[['TV', 'Radio', 'Newspaper']]
y = data['Sales']
estimator = SVR(kernel='linear')
selector = RFE(estimator, n_features_to_select=2, step=1)
selector = selector.fit(x,y)
print(selector.support_)

