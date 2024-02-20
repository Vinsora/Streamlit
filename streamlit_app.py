import streamlit as st
import altair as alt
import pandas as pd
import plotly.express as px
import seaborn as sns

st.header("Vincenzo App")
st.subheader("this was my first attempt")
st.text("hope the link works")

url= "https://www.youtube.com/watch?v=D-D6ZmadzPE"

col1, col2 = st.columns(2)
option = st.sidebar.radio("Select one:", ["image", "video"])
if option == "image":
    st.image("/Users/vincenzosoragnese/Desktop/DSR-37/Streamlit/img.png")
else:
    st.video(url)

data =st.file_uploader("Upload a CSV", type=["csv"])
penguins = pd.read_csv(data)

# title for pandas
st.title("Bar chart with pandas")
# visualise the dataset
st.bar_chart(penguins["species"].value_counts())# title for seaborn
st.title("Scatter plot with seaborn")
# plot a scatter plot
st.pyplot(sns.pairplot(penguins, hue="species"))# title for altair
st.title("Scatter plot with altair")
# plot with altair with x-axis from 160 to 240 and y-axis from 12 to 22
chart = alt.Chart(penguins).mark_point().encode(
    x=alt.X('flipper_length_mm', scale=alt.Scale(domain=(160, 240))),
    y=alt.Y('bill_depth_mm', scale=alt.Scale(domain=(12, 22))),
    color='species'
)
st.altair_chart(chart, use_container_width=True)# title for plotly
st.title("Scatter plot with plotly")
# plot with plotly
import plotly.express as px
fig = px.scatter(penguins, x="flipper_length_mm", y="bill_depth_mm", color="species")
st.plotly_chart(fig)

def display_map_chart(df):
    # Extract unique values from the 'island' column
    islands = df['island'].unique()

    # Plot map chart
    fig = px.choropleth_mapbox(df, 
                                locations='island', 
                                color='island',
                                color_discrete_map="Viridis",
                                mapbox_style="carto-positron",
                                center={"lat": 0, "lon": 0},
                                zoom=1)
    
    # Display map chart
    st.plotly_chart(fig)

display_map_chart(penguins)