#### Volatility Modeling for Commodities and Equity Indices
This project is a production‑grade implementation of advanced volatility models inspired by Saltık, Değirmen, and Ural (2016). It operationalizes the paper’s empirical framework into a modular Python application for forecasting, evaluating, and comparing conditional volatility across energy commodities and equity indices.

The system focuses on nonlinear dynamics, volatility clustering, asymmetry, and long‑memory effects—features that dominate real‑world financial return series but are often underrepresented in baseline models. Applications include risk forecasting, hedge ratio construction, and cross‑asset volatility analysis for markets such as WTI crude oil, Henry Hub natural gas, and the S&P 500 Index.

#### Key Capabilities
📈 Conditional Volatility Forecasting
Implements rolling out‑of‑sample forecasts using EGARCH and FIGARCH models to capture asymmetric responses to shocks and persistent volatility dynamics beyond standard GARCH assumptions.

📊 Model Evaluation via Loss Functions
Forecast accuracy is evaluated using Mean Squared Error (MSE) and Mean Absolute Error (MAE), directly mirroring the loss‑function framework used in the reference paper to identify minimum‑loss models.

🔍 Cross‑Asset Volatility Structure Analysis
Applies identical model specifications across commodities and equities, enabling direct comparison of volatility persistence, asymmetry, and memory across asset classes.

🛡️ Risk Management & Hedging Applications
Forecasted conditional variances can be used to derive optimal hedge ratios, supporting practical decision‑making for traders, portfolio managers, and risk analysts.

#### Methodology: Mapping Code to Econometric Models
This section explicitly links each code module to the mathematical formulations presented in the paper.

#### 1. Return Process
     All assets are modeled as log‑returns:
                                           𝑟𝑡 = 𝜇 + 𝜀𝑡,  𝜀𝑡 = 𝜎𝑡𝑧𝑡,  𝑧𝑡 ∼ 𝐷(0,1)

     ##### Code mapping

           - data/loader.py
               - Loads price data and computes log‑returns.

          - config/settings.py
               - Defines distributional assumptions (GED, Student‑t).

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
