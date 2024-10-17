# Import required libraries
import pandas as pd
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")

# Create options for the dropdown
options = [{'label': 'All Sites', 'value': 'ALL'}] + [
    {'label': site, 'value': site} for site in spacex_df['Launch Site'].unique()
]

# Use the absolute path to the CSV file
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
                                # TASK 1: Add a dropdown list to enable Launch Site selection
                                # The default select value is for ALL sites
                                dcc.Dropdown(
                                            id='site-dropdown',
                                            options= options, #from above
                                            value='ALL', #default value
                                            placeholder="Select a launch site",
                                            searchable=True #enter keywords for 
                                ),
                                            
                                html.Br(),

                                # TASK 2: Add a pie chart to show the total successful launches count for all sites
                                # If a specific launch site was selected, show the Success vs. Failed counts for the site
                                html.Div(dcc.Graph(id='success-pie-chart')),

                                html.Br(),

                                html.P("Payload range (Kg):"),
                                # TASK 3: Add a slider to select payload range
                                dcc.RangeSlider(
                                                id='payload-slider',
                                                min=0, max=10000, step=1000,
                                                marks={0: '0',
                                                    100: '100'},
                                                value=[min_payload, max_payload]
                                ),
                                
                                html.Br(),

                                # TASK 4: Add a scatter chart to show the correlation between payload and launch success
                                html.Div(dcc.Graph(id='success-payload-scatter-chart')),
                                ])

# TASK 2:
# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output
@app.callback(Output(component_id='success-pie-chart', component_property='figure'),
              Input(component_id='site-dropdown', component_property='value')) # the value selected from the site dropdown menu

def get_pie_chart(selected_site):
    if selected_site == 'ALL':
        # # Use all rows in the dataframe to render pie chart for total successful launches for all sites
        # total_successes = spacex_df[spacex_df['class'] == 1].shape[0]
        # total_failures = spacex_df[spacex_df['class'] == 0].shape[0]
        
        # # Create a pie chart for total successes and failures
        # fig = px.pie(
        #     names=['Successful Launches', 'Failed Launches'],
        #     values=[total_successes, total_failures],
        #     title='Total Launch Outcomes for All Sites'
        # )
        # Calculate total successful launches by site
        success_counts = spacex_df[spacex_df['class'] == 1].groupby('Launch Site').size()
        failure_counts = spacex_df[spacex_df['class'] == 0].groupby('Launch Site').size()
        
        # Prepare data for pie chart
        # names = success_counts.index.tolist() + failure_counts.index.tolist()
        names = success_counts.index.tolist() 
        # values = success_counts.tolist() + failure_counts.tolist()
        values = success_counts.tolist() 
        
        # Create a pie chart for total successes by site
        fig = px.pie(
            names=names,
            values=values,
            title='Total Successful Launch Outcomes for All Sites',
            labels={'names': 'Launch Outcomes'},
            hole=0.3  # Optional: creates a donut chart effect
        )
    else:
        # Filter dataframe for the selected site
        filtered_df = spacex_df[spacex_df['Launch Site'] == selected_site]
        
        # Count successes and failures for the selected site
        success_count = filtered_df[filtered_df['class'] == 1].shape[0]
        failure_count = filtered_df[filtered_df['class'] == 0].shape[0]
        
        # Create a pie chart for the selected site's outcomes
        fig = px.pie(
            names=['Successful Launches', 'Failed Launches'],
            values=[success_count, failure_count],
            title=f'Launch Outcomes for {selected_site}'
        )

    return fig



# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output
@app.callback(Output(component_id='success-payload-scatter-chart', component_property='figure'),
              [Input(component_id='site-dropdown', component_property='value'), 
               Input(component_id="payload-slider", component_property="value")]
              )
def update_scatter_chart(selected_site, payload_range):
    # Filter DataFrame based on selected payload range
    filtered_df = spacex_df[
        (spacex_df['Payload Mass (kg)'] >= payload_range[0]) & 
        (spacex_df['Payload Mass (kg)'] <= payload_range[1])
    ]
    
    if selected_site == 'ALL':
        # Render scatter plot for all sites with selected payload range
        fig = px.scatter(
            filtered_df,
            x='Payload Mass (kg)',
            y='class',
            color='Booster Version Category',
            title='Payload vs. Launch Success for All Sites',
            labels={'class': 'Launch Success (1 = Success, 0 = Failure)'}
        )
    else:
        # Filter dataframe for the selected site
        filtered_df = filtered_df[filtered_df['Launch Site'] == selected_site]
        
        # Render scatter plot for the selected site with selected payload range
        fig = px.scatter(
            filtered_df,
            x='Payload Mass (kg)',
            y='class',
            color='Booster Version Category',
            title=f'Payload vs. Launch Success for {selected_site}',
            labels={'class': 'Launch Success (1 = Success, 0 = Failure)'}
        )

    return fig
# Run the app
if __name__ == '__main__':
    app.run_server()
