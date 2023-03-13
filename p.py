# you can combine multiple series along a particular axis (column-wise or row-wise)
import pandas as pd

# Create pandas Series
courses = pd.Series(["Spark","PySpark","Hadoop"])
fees = pd.Series([22000,25000,23000])
discount  = pd.Series([1000,2300,1000])

# Combine two Series
df = pd.concat([courses, fees], axis=1)
print("Concat 2 lists ...\n", df)

# Combine multiple Series
df = pd.concat([courses, fees, discount], axis=1)
print("\nConcat 3 lists ...\n", df)