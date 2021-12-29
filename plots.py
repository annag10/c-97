# Import necessary modules 
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Define a function 'app()' which accepts 'car_df' as an input.
def app(car_df):
  st.header('visualise data')
  st.set_option('deprecation.showPyplotGlobalUse', False)
  st.subheader('scatter plot')
  features_list=st.multiselect("select x axis values",('carwidth','enginesize','horsepower','drivefield_fwd','car_company_buick'))
  for i in features_list:
    st.subheader(f"scatter plot between {i} and price")
    plt.figure(figsize=(12,5))
    sns.scatterplot(x=i,y='price',data=car_df)
    st.pyplot()
  st.subheader('visualisation sector')

  plot_types=st.multiselect("select charts",('histogram','boxplot','heatmap'))
  if 'histogram' in plot_types:
  	st.subheader('HISTOGRAM')
  	columns=st.selectbox("select the column to create its histogram",('carwidth','enginesize','horsepower'))
  	plt.figure(figsize=(12,5))
  	plt.title(f"histogram for {columns}")
  	plt.hist(car_df[columns],bins='sturges',edgecolor="black")
  	st.pyplot()
  if 'boxplot' in plot_types:
  	st.subheader('BOXPLOT')
  	columns=st.selectbox("select the column to create its boxplot",('carwidth','enginesize','horsepower'))
  	plt.figure(figsize=(12,5))
  	plt.title(f"boxplot for {columns}")
  	sns.boxplot(car_df[columns])
  	st.pyplot()
  if 'heatmap' in plot_types:
  	st.subheader('HEATMAP')
  	plt.figure(figsize=(12,5))
  	plt.title(f"heatmap")
  	sns.heatmap(car_df.corr(),annot=True)
  	st.pyplot()