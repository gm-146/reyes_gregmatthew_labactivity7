import requests
import pandas as pd
import plotly.express as px

# Manila coordinates
latitude = 14.5995
longitude = 120.9842

url = (
    f"https://api.open-meteo.com/v1/forecast?"
    f"latitude={latitude}&longitude={longitude}"
    f"&hourly=temperature_2m"
)

response = requests.get(url)
data = response.json()

if "hourly" not in data:
    print("Failed to retrieve weather data.")
    exit()

df = pd.DataFrame({
    "Time": data["hourly"]["time"],
    "Temperature": data["hourly"]["temperature_2m"]
})

print("\nFirst 10 Records:")
print(df.head(10))

fig = px.line(
    df,
    x="Time",
    y="Temperature",
    title="Hourly Temperature Forecast in Manila",
    markers=True
)

fig.update_layout(
    xaxis_title="Date and Time",
    yaxis_title="Temperature (°C)"
)

fig.show()