import pandas as pd
dir(pd)

from plotly.offline import plot
import plotly.graph_objs as go 


#We read the data into a variable called df

df = pd.read_excel("STEM_BAPM.xlsx", sheet_name = "revenue")
df

#We use the Bar function of the go library

revenue = go.Bar(x= df["Year"], y=df["Revenue"],               
               marker = dict(color = "DarkGreen")
                )
                   
#We use the Layout function of the go library
titles = go.Layout(
                    #Define title of the graph
                    title = "Bureau Veritas Revenue FY2019 - FY2022",
                    
                    #Define title for x-axis
                    xaxis=go.layout.XAxis( 
                            title=go.layout.xaxis.Title(
                            text=" ", 
                        )
                    ),
                  
                    #Define title for y-axis
                    yaxis=go.layout.YAxis(
                            title=go.layout.yaxis.Title(
                            text="$ Millions",
                            )
                      )
                    )
                            
#We use Figure function of go library                           
fig = go.Figure(data=[revenue])

#We call the plot function from the plotly.offline library
plot(fig)



