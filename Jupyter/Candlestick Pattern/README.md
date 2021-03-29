# Candlestick Analysis: Prediction of Hong Kong and Korean Stock Market Trend

## Course project, taken few weeks

> It is an attempt to find useful candlestick patterns in two markets.

### Candlestick pattern
- A candlestick shows open, high, low, and close (OHLC) price of certain period of time.
![candlestick_chart.png](/images/candlestic_chart.png)
- A candlestick pattern can be either bearish(price drop) or bullish(price rise)
- A candlestick pattern is determined by few consecutive candlesticks

### Data
- HSI 50 & KOSPI 50 daily OHLC prices
- csv format
- collected from yahoo finance, finance.com
- time range : recent 9 years, `2011-11-07` to `2020-11-06`

### Python Libraries
- basic data analysis libraries : pandas, matplotlib, numpy, etc.
- statistical libraries : qqplot, scipy stats, etc.
- candlestick library : mplfinance candlestick_ohlc

### Notebook available [here](https://github.com/fl-ada/Toy_programs/blob/master/Jupyter/Candlestick%20Pattern/STAT3609_project_group2.ipynb)
- extract OHLC data from csv daily 
- detect candlestick patterns from OHLC data
- Find bearish and bullish patterns for each market, in short term (5-day) and long term(250-day)
- Test statistical significance and evaluate