from sklearn.neural_network import MLPClassifier
import pandas as pd

df = pd.read_csv("data.csv")

y = df.id_move

df = df.drop("id_move", axis=1)

x = df

clf = MLPClassifier().fit(x, y)

print(clf.predict([[250,425,250,150]]))
