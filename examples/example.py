from binary_feature import binary_feature

df = binary_feature(
    name='https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data',
    colum='petal_width',
    names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'],
    verbose=True
)
df.to_csv('out.csv')


df = binary_feature(
    name='out.csv',
    colum='sepal_length',
    index_col=0,
    verbose=True
)
df.to_csv('out2.csv')
