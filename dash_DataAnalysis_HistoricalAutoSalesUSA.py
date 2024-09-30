#download the template file
# import requests

# url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/InaFqKi-TlmTZwlzKvlNaQ/DV0101EN-Final-Assign-Part-2-Questions.py'
# response = requests.get(url)

# if response.status_code == 200:
#     with open('DV0101EN-Final-Assign-Part-2-Questions.py', 'wb') as f:
#         f.write(response.content)
#     print("File downloaded successfully.")
# else:
#     print("Failed to download file.")

import dash
import more_itertools
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px

# Load the data using pandas
data = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv')

# Initialize the Dash app
app = dash.Dash(__name__)

# Set the title of the dashboard
app.title = "Automobile Statistics Dashboard"

#---------------------------------------------------------------------------------
# Create the dropdown menu options
dropdown_options = [
    {'label': 'Yearly Statistics', 'value': 'Yearly Statistics'},
    {'label': 'Recession Period Statistics', 'value': 'Recession Period Statistics'}
]
# List of years 
year_list = [i for i in range(1980, 2024, 1)]
#---------------------------------------------------------------------------------------
# Create the layout of the app
app.layout = html.Div([
    #TASK 2.1 Add title to the dashboard #Include style for title
    html.H1("Automobile Sales Statistics Dashbord",
            style={'textAlign': 'center', 'color': '#503D36','font-size': 24}),
# ])
    
    #TASK 2.2: Add two dropdown menus
    html.Div([
        html.Label("Select Statistics:"),
        dcc.Dropdown(
            id='dropdown-statistics',
            options=[
                {'label': 'Yearly Statistics', 'value': 'Yearly Statistics'},
                {'label': 'Recession Period Statistics', 'value': 'Recession Period Statistics'}
            ],
            placeholder='Select a report type',
            style={'textAlign': 'center',
                    # 'color': '#503D36',
                    'font-size': '20px',
                    'width':'80%',
                    'padding' : '3px'
            }
        )
    ]),
    html.Div(dcc.Dropdown(
            id='select-year',
            options=[{'label': i, 'value': i} for i in year_list],
            value='Select-year',
            placeholder= 'Select-year',
            style={'textAlign': 'center',
                    # 'color': '#503D36',
                    'font-size': '20px',
                    'width':'80%',
                    'padding' : '3px'}
    )),
    #TASK 2.3: Add a division for output display
    html.Div([
        html.Div(id='output-container', className='chart-grid', style={'display':'flex'}),
    ]),
])


#TASK 2.4: Creating Callbacks #gets triggered when input changes
# Define the callback function to update the input container based on the selected statistics
#if user selection Recession Period Statistics(fornt=end) then Select Year(id=select-year) - disables - doesn't show options
#if user chooses Yearly Statistics(front-end) then Select Year
@app.callback(
    Output(component_id='select-year', component_property='disabled'),
    Input(component_id='dropdown-statistics',component_property='value')) #either Recession Period Statistics or Yearly Statistics
#reads the selected value decides to update the container or leave as is origninal state is disabled
def update_input_container(selected_statistics):
    if selected_statistics =='Yearly Statistics': 
        return False #This likely indicates that certain UI components (like a dropdown or input field) should be enabled or visible when this statistic is selected
    else: 
        return True #is anything else, the function returns True, which may indicate that those components should be disabled or hidden.

# #Callback for plotting #gets triggered when input changes
# # Define the callback function to update the input container based on the selected statistics
@app.callback(
    Output(component_id='output-container', component_property='children'),
    [Input(component_id='dropdown-statistics', component_property='value'), 
      Input(component_id='select-year', component_property='value')])


def update_output_container(report_type, recession_year ):
    if report_type == 'Recession Period Statistics':
        # Filter the data for recession periods
        recession_data = data[data['Recession'] == 1] 
        # Check if recession_data is empty
        if recession_data.empty:
            return "No data available for recession periods."
    # else:
    #     return None 
         
        
# #TASK 2.5: Create and display graphs for Recession Report Statistics

# # #Plot 1 Automobile sales fluctuate over Recession Period (year wise)
# #         # use groupby to create relevant data for plotting
        yearly_rec=recession_data.groupby('Year')['Automobile_Sales'].mean().reset_index()
        R_chart1 = dcc.Graph(
            figure=px.line(yearly_rec, 
            x='Year',
            y='Automobile_Sales',
            title="Average Automobile Sales Fluctuation Over Recession Period"))

# #Plot 2 Calculate the average number of vehicles sold by vehicle type       
        
#         # use groupby to create relevant data for plotting
#         #Hint:Use Vehicle_Type and Automobile_Sales columns
        average_sales = recession_data.groupby('Vehicle_Type')['Automobile_Sales'].mean().reset_index()                 
        R_chart2  = dcc.Graph(
            figure=px.bar(average_sales,
            x='Vehicle_Type',
            y='Automobile_Sales',
            title="Average Automobile Sales by Vehicle Type over Recession Period"))

        
# # Plot 3 Pie chart for total expenditure share by vehicle type during recessions
#         # grouping data for plotting
	# Hint:Use Vehicle_Type and Advertising_Expenditure columns
        exp_rec= recession_data.groupby('Vehicle_Type')['Advertising_Expenditure'].mean().reset_index()
        R_chart3 = dcc.Graph(
            figure= px.pie(exp_rec,
            values= 'Advertising_Expenditure',
            names='Vehicle_Type',
            title="Total Advertising Expediture by Vehicle Type during Recession Periods"))
              

# # Plot 4 bar chart for the effect of unemployment rate on vehicle type and sales
#         #grouping data for plotting
# 	# Hint:Use unemployment_rate,Vehicle_Type and Automobile_Sales columns
        unemp_data = recession_data.groupby(['unemployment_rate', 'Vehicle_Type'])['Automobile_Sales'].mean().reset_index()
        if unemp_data.empty:
            return "No data available for the effect of unemployment rate on vehicle type and sales."
        R_chart4 = dcc.Graph(
            figure=px.bar(unemp_data,
            x='Vehicle_Type',
            y='Automobile_Sales',
            color='unemployment_rate',
            labels={'unemployment_rate': 'Unemployment Rate', 
                        'Automobile_Sales': 'Average Automobile Sales'},
            # labels={'Vehicle_Type': 'Vehicle Type', 'Automobile_Sales': 'Average Automobile Sales'},
            title='Effect of Unemployment Rate on Vehicle Type and Sales'))


        return [
            html.Div(
                className='chart-row',
                children=[
                    html.Div(children=R_chart1, style={'flex': '1 1 45%', 'margin': '10px'}),
                    html.Div(children=R_chart2, style={'flex': '1 1 45%', 'margin': '10px'})
                ],
                style={'display': 'flex', 'flexWrap': 'wrap'}
            ),
            html.Div(
                className='chart-row',
                children=[
                    html.Div(children=R_chart3, style={'flex': '1 1 45%', 'margin': '10px'}),
                    html.Div(children=R_chart4, style={'flex': '1 1 45%', 'margin': '10px'})
                ],
                style={'display': 'flex', 'flexWrap': 'wrap'}
            )
                ]
    
    # else:
    #      return None 

# # # TASK 2.6: Create and display graphs for Yearly Report Statistics
# #  # Yearly Statistic Report Plots
# #     # Check for Yearly Statistics.  
#     # elif (recession_year and selected_statistics=='Yearly Statistics')  
#     elif (report_type =='Yearly Statistics') :                         
#     # elif (recession_year and report_type == True) :
#         yearly_data = data[data['Year'] == recession_year]

# #Filter the data by year
    elif report_type == 'Yearly Statistics':
        recession_year_data = data[data['Year'] == recession_year] 
        all_data= data
        # if recession_year_data.empty:
        #     return "No data available for recession periods."
        # return recession_year_data
                              

                              
# # #plot 1 Yearly Automobile sales using line chart for the whole period.
# #         # grouping data for plotting.
# #         # Hint:Use the columns Year and Automobile_Sales.
        yas= all_data.groupby('Year')['Automobile_Sales'].mean().reset_index()
        Y_chart1 = dcc.Graph(
           figure=px.line(yas,
            x= "Year",
            y= 'Automobile_Sales',
            title= "Automobile Sales by Year"))
            
# # # Plot 2 Total Monthly Automobile sales using line chart.
# #         # grouping data for plotting.
# # 	# Hint:Use the columns Month and Automobile_Sales.
        mas=recession_year_data.groupby('Month')['Automobile_Sales'].mean().reset_index()
        Y_chart2 = dcc.Graph(
            figure=px.line(mas,
            x='Month',
            y='Automobile_Sales',
            title='Total Monthly Automobile Sales'))

# #   # Plot bar chart for average number of vehicles sold during the given year
# #          # grouping data for plotting.
# #          # Hint:Use the columns Year and Automobile_Sales
        avr_vdata=recession_year_data.groupby('Month')['Automobile_Sales'].mean().reset_index()
        Y_chart3 = dcc.Graph(
            figure= px.bar(avr_vdata,
            x= 'Month',
            y="Automobile_Sales",
            title='Average Vehicles Sold by Vehicle Type in the year {}'.format(recession_year)))

# #     # Total Advertisement Expenditure for each vehicle using pie chart
# #          # grouping data for plotting.
# #          # Hint:Use the columns Vehicle_Type and Advertising_Expenditure
        exp_data=recession_year_data.groupby("Vehicle_Type")['Advertising_Expenditure'].mean().reset_index()
        Y_chart4 = dcc.Graph(
            figure= px.pie(exp_data,
            values= "Advertising_Expenditure",
            names="Vehicle_Type",
            title= 'Total Advertisment Expenditure for Each Vehicle'))

# # #TASK 2.6: Returning the graphs for displaying Yearly data
        return [
            html.Div(
                className='chart-row',
                children=[
                    html.Div(children=Y_chart1, style={'flex': '1 1 45%', 'margin': '10px'}),
                    html.Div(children=Y_chart2, style={'flex': '1 1 45%', 'margin': '10px'})
                ],
                style={'display': 'flex', 'flexWrap': 'wrap'}
                    ),
            html.Div(
                className='chart-row',
                children=[
                    html.Div(children=Y_chart3, style={'flex': '1 1 45%', 'margin': '10px'}),
                    html.Div(children=Y_chart4, style={'flex': '1 1 45%', 'margin': '10px'})
                ],
                style={'display': 'flex', 'flexWrap': 'wrap'}
        )
        ]
        # return [
        #      html.Div(className='chart-item', children=[html.Div(children=Y_chart1),html.Div(children=Y_chart2)],style={'display':'flex'}),
        #     html.Div(className='chart-item', children=[html.Div(children=Y_chart3),html.Div(children=Y_chart4)],style={'display': 'flex'})
        #     ]
        
# else:
#      return None

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)