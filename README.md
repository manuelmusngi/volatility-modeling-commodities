#### Volatility Modeling for Commodities and Equity Indices
This project is a production‑grade implementation of advanced volatility models inspired by Saltık, Değirmen, and Ural (2016). It operationalizes the paper’s empirical framework into a modular Python application for forecasting, evaluating, and comparing conditional volatility across energy commodities and equity indices.

The system focuses on nonlinear dynamics, volatility clustering, asymmetry, and long‑memory effects—features that dominate real‑world financial return series but are often underrepresented in baseline models. Applications include risk forecasting, hedge ratio construction, and cross‑asset volatility analysis for markets such as WTI crude oil, Henry Hub natural gas, and the S&P 500 Index.

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
