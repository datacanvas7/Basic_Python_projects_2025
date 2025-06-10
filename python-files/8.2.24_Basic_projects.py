# %% [markdown]
# # Basic Python Projects - February 2025

# %% [markdown]
# ## 1-Temperature Data Visualization

# %%
import plotly.express as px
import pandas as pd

# Data
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
temperatures = [22, 24, 21, 25, 23, 26, 24]

# Create a DataFrame
df = pd.DataFrame({"Day": days, "Temperature (°C)": temperatures})

# Interactive line chart
fig = px.line(df, x="Day", y="Temperature (°C)", title="Weekly Temperature Trend", markers=True)
fig.show()

# %% [markdown]
# ## 2- Sales Data Visualization

# %%
import plotly.express as px
import pandas as pd

# Data
products = ["Mobiles", "Tablets", "Chromebooks", "Laptops"]
sales = [150, 200, 180, 220]

# Create a DataFrame
df = pd.DataFrame({"Products": products, "Sales (Units)": sales})

# Interactive bar chart
fig = px.bar(df, x="Products", y="Sales (Units)", title="Product Sales", color="Products")
fig.show()

# %% [markdown]
# ## 3-Student Performance Visualization

# %%
import plotly.express as px
import pandas as pd

# Data
grades = ["A", "B", "C", "D"]
students = [15, 25, 10, 5]

# Create a DataFrame
df = pd.DataFrame({"Grades": grades, "Students": students})

# Interactive pie chart
fig = px.pie(df, values="Students", names="Grades", title="XII-B Student Performance", hole=0.3)
fig.show()

# %% [markdown]
# ## 4-Population Growth Visualization

# %%
import plotly.express as px
import pandas as pd

# Data
years = [2018, 2019, 2020, 2021, 2022, 2023]
population = [100000, 120000, 140000, 160000, 180000, 200000]

# Create a DataFrame
df = pd.DataFrame({"Year": years, "Population": population})

# Interactive line chart
fig = px.line(df, x="Year", y="Population", title="City Population Growth", markers=True)
fig.show()

# %% [markdown]
# ## 5-Movie Ratings Visualization

# %%
import plotly.express as px
import pandas as pd
import random

# Data
movies = ["Inception", "Titanic", "Avatar", "Gladiator", "Jaws"]
ratings = [random.uniform(1, 10) for _ in range(5)]
reviews = [random.randint(100, 1000) for _ in range(5)]

# Create a DataFrame
df = pd.DataFrame({"Movies": movies, "Ratings": ratings, "Reviews": reviews})

# Interactive scatter plot
fig = px.scatter(df, x="Ratings", y="Reviews", title="Movie Ratings vs Reviews", color="Movies", size="Reviews")
fig.show()

# %%



