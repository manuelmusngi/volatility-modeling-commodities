## 🧪 Methodology

### 1. Data and volatility construction

We focus on Henry Hub natural gas prices at a daily frequency. Raw settlement prices are transformed into continuously compounded log‑returns. Basic data cleaning includes handling missing observations, aligning trading days, and filtering out obvious data errors. Where appropriate, realized volatility proxies (e.g., squared returns or rolling realized variance) are constructed to serve as targets or auxiliary variables in model estimation and evaluation.

Formally, let \( P_t \) denote the price at time \( t \). Returns are defined as


\[
r_t = 100 \times \left( \ln P_t - \ln P_{t-1} \right),
\]


and the conditional variance process \( \sigma_t^2 \) is modeled under different specifications described below.

### 2. GARCH‑family models

Baseline volatility dynamics are captured using standard GARCH‑type models. A simple GARCH(1,1) specification is given by


\[
r_t = \mu + \varepsilon_t, \quad \varepsilon_t = \sigma_t z_t, \quad z_t \sim \mathcal{D}(0,1),
\]




\[
\sigma_t^2 = \omega + \alpha \varepsilon_{t-1}^2 + \beta \sigma_{t-1}^2,
\]


where \( \mathcal{D} \) is a chosen standardized distribution (e.g., Gaussian or Student‑t). We extend this baseline to EGARCH and FIGARCH to accommodate asymmetry and long memory in volatility. Parameters are estimated via maximum likelihood, and models are compared using information criteria and out‑of‑sample forecast performance.

### 3. Regime‑switching volatility: HMM and MS‑GARCH

To capture distinct volatility regimes, we employ Hidden Markov Models (HMM) and Markov‑Switching GARCH (MS‑GARCH). In the HMM framework, returns (or volatility proxies) are assumed to be generated from a finite mixture of state‑dependent distributions, with the latent state following a first‑order Markov chain. Let \( S_t \in \{1, \dots, K\} \) denote the regime at time \( t \). Conditional on \( S_t = k \), the return distribution is


\[
r_t \mid S_t = k \sim \mathcal{N}(\mu_k, \sigma_k^2),
\]


and the transition probabilities are summarized by a \( K \times K \) matrix \( P \), where \( P_{ij} = \Pr(S_t = j \mid S_{t-1} = i) \).

In the MS‑GARCH specification, the conditional variance dynamics themselves are regime‑dependent:


\[
\sigma_t^2 = \omega_{S_t} + \alpha_{S_t} \varepsilon_{t-1}^2 + \beta_{S_t} \sigma_{t-1}^2,
\]


with the regime \( S_t \) again evolving according to a Markov chain. This allows both the level and persistence of volatility to differ across regimes, aligning with empirical evidence of calm vs turbulent periods in natural gas markets. Estimation proceeds via likelihood‑based methods, combining Hamilton filtering and smoothing for state inference.

### 4. Machine learning benchmarks

We construct machine learning benchmarks by modeling volatility (or squared returns) as a function of lagged features and, optionally, exogenous variables. Let \( y_t \) denote the volatility target and \( \mathbf{x}_t \) a feature vector including lagged returns, lagged volatility, and other engineered predictors. ML models such as Random Forests, gradient boosting (XGBoost), and optionally LSTM networks are trained to approximate


\[
y_t = f(\mathbf{x}_t) + \eta_t,
\]


where \( f(\cdot) \) is a nonlinear mapping learned from data. Hyperparameters are tuned via cross‑validation on a rolling or expanding window to respect the time‑series structure.

### 5. Hybrid GARCH‑residual‑ML models

Hybrid models are constructed by combining a parametric GARCH‑type model with a nonparametric ML correction. First, a baseline GARCH model is estimated and used to generate fitted conditional variances \( \hat{\sigma}_t^2 \) and residuals \( \hat{\varepsilon}_t \). The residual component is then modeled using ML:


\[
\hat{\varepsilon}_t = g(\mathbf{z}_t) + u_t,
\]


where \( \mathbf{z}_t \) includes lagged residuals and other features. The final hybrid volatility forecast is obtained by augmenting the GARCH forecast with the ML‑based correction, effectively capturing structure that the parametric model alone cannot explain.

### 6. Forecasting design and evaluation

All models are evaluated in a rolling out‑of‑sample forecasting framework. A fixed initial estimation window is used to fit each model, after which one‑step‑ahead volatility forecasts are generated. The window is then rolled forward, with periodic refitting according to a configurable refit frequency. For regime‑switching models, both filtered and smoothed state probabilities are computed, and regime‑conditioned forecasts are produced.

Forecast accuracy is assessed using standard loss functions such as mean squared error (MSE), mean absolute error (MAE), and the quasi‑likelihood (QLIKE) loss. Pairwise model comparisons are conducted using Diebold‑Mariano tests to assess whether differences in forecast performance are statistically significant. Results are summarized in tables and visualized through forecast comparison plots and regime probability diagrams, enabling a transparent benchmarking of GARCH, MS‑GARCH, HMM, ML, and hybrid specifications.

#### License
This project is licensed under the [MIT License](https://github.com/manuelmusngi/regime_switching_models/edit/main/LICENSE).  
