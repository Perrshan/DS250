#%%
import plotly.express as px
data = px.data.iris()
data.head()

#%%
px.scatter(data,
    x="sepal_width", 
    y="sepal_length", 
    color = "species", 
    size = "petal_length",
    symbol = "species",
    hover_data=["species", "petal_width"], 
    title = "The relationship between sepal width and sepal length"
)
# %%
