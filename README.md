#### Volatility Modeling for Commodities and Equity Indices
This project implements and extends the volatility modeling framework presented in “Volatility Modelling in Crude Oil and Natural Gas Prices” by Saltık et al. (2016). It translates the paper’s empirical methodology into a modular, reproducible computational application designed to model and forecast volatility in key energy commodities and equity index markets using advanced GARCH-family models.

The application focuses on capturing the nonlinear dynamics, volatility clustering, asymmetry, and long-memory behavior commonly observed in financial return series. It applies these models to markets such as WTI crude oil, Henry Hub natural gas, and the S&P 500 Index, enabling both cross-asset comparison and practical risk analysis.



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
