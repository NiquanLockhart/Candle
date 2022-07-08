import pandas as pd
data = pd.read_csv("/Users/niquanlockhart/PycharmProjects/pythonProject5/SPY.csv")
import plotly.graph_objects as go
figure = go.Figure(data=[go.Candlestick(x=data["Date"],
                                        open=data["Open"],
                                        high=data["High"],
                                        low=data["Low"],
                                        close=data["Close"])])
figure.update_layout(title = "SPY Stock Price Analysis",
                     xaxis_rangeslider_visible=False)
figure.show()
