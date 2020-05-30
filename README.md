# Overview
Project created to learn the Python [Dash](https://dash.plotly.com/) framework. The goal of the project was to visualize the data of [Stack Overflow Survey 2019](https://insights.stackoverflow.com/survey).

# Build & Run

## Local preview
From the project directory run:
```
pip install -r requirements.txt
python ./index.py
```
Now visit http://0.0.0.0:8050/

## Docker preview
From the project directory run:
```
docker build -t dash-analysis:latest .
docker run -d -p 8050:8050 dash-analysis:latest
```
Now visit http://0.0.0.0:8050/

## Heroku deployment
From the project directory run:
```
heroku login
heroku container:login
heroku container:push web -a frezzu-siwb-dash-analysis 
heroku container:release web -a frezzu-siwb-dash-analysis   
heroku logs -t -a frezzu-siwb-dash-analysis
```
Now visit https://frezzu-siwb-dash-analysis.herokuapp.com/