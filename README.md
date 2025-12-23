#### Volatility Modeling for Commodities and Equity Indices
This project implements and extends the volatility modeling framework presented in “Volatility Modelling in Crude Oil and Natural Gas Prices” by Saltık et al. (2016). It translates the paper’s empirical methodology into a modular, reproducible computational application designed to model and forecast volatility in key energy commodities and equity index markets using advanced GARCH-family models.

The application focuses on capturing the nonlinear dynamics, volatility clustering, asymmetry, and long-memory behavior commonly observed in financial return series. It applies these models to markets such as WTI crude oil, Henry Hub natural gas, and the S&P 500 Index, enabling both cross-asset comparison and practical risk analysis.

#### Core Functionality
📈 Conditional Volatility Forecasting
The system generates rolling, out-of-sample volatility forecasts using GARCH-family models such as EGARCH and FIGARCH. These models are specifically chosen for their ability to capture asymmetric responses to shocks and persistent volatility dynamics that standard GARCH models may fail to represent.

📊 Model Performance Evaluation
Forecast accuracy is evaluated using Mean Squared Error (MSE) and Mean Absolute Error (MAE), consistent with the loss-function-based assessment framework employed in the original research. This allows objective comparison of model performance across different assets and time periods.

🔍 Cross-Asset Volatility Comparison
By applying identical model specifications to both energy commodities and an equity index, the project facilitates comparative analysis of volatility structures, persistence, and sensitivity to market shocks—mirroring the multi-market perspective of the source paper.

🛡️ Risk Management and Hedging Applications
Forecasted conditional volatilities can be used to derive optimal hedge ratios, supporting informed decision-making for traders, portfolio managers, policymakers, and risk analysts. This reflects the paper’s emphasis on minimizing loss and managing risk in volatile energy markets.

#### Models Implemented
The following models are included based on their empirical relevance and practical applicability in volatility forecasting and hedging:

GARCH — Baseline symmetric volatility model

EGARCH — Exponential GARCH capturing asymmetric and leverage effects

FIGARCH — Fractionally integrated GARCH modeling long-memory volatility

These models are particularly useful for developing risk-minimizing hedge strategies in both commodity and equity markets.

#### Project architecture

volatility_model_app/\
│
├── [main.py](https://github.com/manuelmusngi/Volatility-Modeling-Index-and-Commodities/blob/main/main.py)                            
├── config/\
│   └── [settings.py](https://github.com/manuelmusngi/Volatility-Modeling-Index-and-Commodities/blob/main/config/settings.py)                    
├── data/\
│   └── [loader.py](https://github.com/manuelmusngi/Volatility-Modeling-Index-and-Commodities/blob/main/data/loader.py)                      
├── models/\
│   └── [model_factory.py](https://github.com/manuelmusngi/Volatility-Modeling-Index-and-Commodities/blob/main/models/model_factory.py)               
│   └── [forecasting.py](https://github.com/manuelmusngi/Volatility-Modeling-Index-and-Commodities/blob/main/models/forecasting.py)                 
├── evaluation/\
│   └── [metrics.py](https://github.com/manuelmusngi/Volatility-Modeling-Index-and-Commodities/blob/main/evaluation/metrics.py%20python%20Copy%20Edit)                     
├── utils/\
│   └── [logger.py](https://github.com/manuelmusngi/Volatility-Modeling-Index-and-Commodities/blob/main/utils/logger.py)                      
│   └── [plotter.py](https://github.com/manuelmusngi/Volatility-Modeling-Index-and-Commodities/blob/main/utils/plotter.py)                     
├── reports/\
│   └── results.csv
\
|   └── [requirements.txt](https://github.com/manuelmusngi/Volatility-Modeling-Index-and-Commodities/blob/main/requirements.txt)

#### Dependencies
- [requirements.txt](https://github.com/manuelmusngi/Volatility-Modeling-Index-and-Commodities/blob/main/requirements.txt)

#### Reference
- [Volatility Modelling in Crude Oil and Natural Gas Prices](https://www.sciencedirect.com/science/article/pii/S2212567116302192)

#### License
This project is licensed under the [MIT License](https://github.com/manuelmusngi/regime_switching_models/edit/main/LICENSE).  
