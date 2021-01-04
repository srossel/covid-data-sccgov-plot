
#SANTA CLARA DATA
#https://data.sccgov.org/browse

#COVID-19 case counts by date
#https://data.sccgov.org/resource/6cnm-gchg.json


#Count of deaths with COVID-19 by date
#https://data.sccgov.org/resource/tg4j-23y2.json
import requests
import json
import pandas

url_1="https://data.sccgov.org/resource/6cnm-gchg.json"
url_2="https://data.sccgov.org/resource/tg4j-23y2.json"
data1 = json.loads(requests.get(url_1).text)
data2 = json.loads(requests.get(url_2).text)

#keys in url1 : date,total_cases,new_cases
#keys in url2 : [{"date":"2020-02-06T00:00:00.000","ltcf":"0","non_ltcf":"1","total":"1","cumulative":"1"}

# print(len(data1))
# print(len(data2))
# print(data1[0]['date'])

with open("data/covid-joint-data.csv", mode="w") as covid_joint_data:
    header = f"date,total_cases,new_cases,total_deaths,cumulative_deaths\n"
    covid_joint_data.write(header)

with open("data/covid-joint-data.csv", mode="a") as covid_joint_data:
    for i in range(len(data1)):
        for j in range(len(data2)):
            if data1[i]['date'] == data2[j]['date']:
                date = data1[i]['date']
                total_cases = data1[i]['total_cases']
                new_cases = data1[i]['new_cases']
                total_deaths = data2[j]['total']
                cumulative_deaths = data2[j]['cumulative']
                content = f"{date},{total_cases},{new_cases},{total_deaths},{cumulative_deaths}\n"
                covid_joint_data.write(content)

#date,total_cases,new_cases,total_deaths,cumulative_deaths
data_file3 = 'data/covid-joint-data.csv'
data3 = pandas.read_csv(data_file3)

#Creating the graph
import plotly.graph_objects as go

# Create traces
fig = go.Figure()
fig.add_trace(go.Scatter(x=data3['date'], y=data3['new_cases'],
                    mode='lines',
                    name='new_cases')
              )

fig.add_trace(go.Scatter(x=data3['date'], y=data3['cumulative_deaths'],
                    mode='lines',
                    name='cumulative_deaths')

              )
fig.show()