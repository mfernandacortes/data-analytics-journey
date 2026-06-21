
prod= pd.read_sql("select ProductID, ProductName, CategoryID, UnitPrice from Products", engine)
cat= pd.read_sql("select CategoryID, CategoryName from Categories", engine)

od_prod_cat= pd.merge(prod, cat, on ="CategoryID")


#print(od_prod_cat)



precio_maximo= od_prod_cat.groupby(['CategoryID', 'CategoryName'])["UnitPrice"].max().sort_values(ascending=False)
print(precio_maximo)

#df.groupby("col").agg({"col1": ["mean", "max"], "col2": "size"})

od_prod_cat= od_prod_cat.groupby(['CategoryID', 'CategoryName']).agg({"UnitPrice": ["max", "min"]})


print(od_prod_cat)
