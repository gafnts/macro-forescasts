# Predicting the next recession

Using **FRED (Federal Reserve Economic Data)**, **economic theory**, and **machine learning** to forecast future economic recessions.

## Overview

This project aims to provide a robust predictive model for identifying potential economic recessions. Combining data-driven insights with economic theory, the model leverages historical trends and key indicators to forecast recessionary periods.

## Economic theory behind initial feature selection

The initial feature set is grounded in macroeconomic theory, categorized into four broad areas:

1. **Real economy**
Gross Domestic Product (GDP)
Gross Domestic Income (GDI)
Unemployment Rate (UNRATE)
Employment-Population Ratio (EMRATIO)
All Employees, Total Nonfarm (PAYEMS)
All Employees, Goods-Producing (USGOOD)
All Employees, Service-Providing (SRVPRD)
Real Gross Private Domestic Investment (GPDIC1)
Gross saving as a percentage of gross national income (W206RC1Q156SBEA)

2. **Monetary indicators**
Federal Funds Effective Rate (DFF)
Personal Consumption Expenditures: Chain-type Price Index (PCEPI)
Sticky Price Consumer Price Index less Food and Energy (CORESTICKM159SFRBATL)
Monetary Base: Currency in Circulation (MBCURRCIR)
M1 (M1SL)
Velocity of M1 Money Stock (M1V)
M2 (M2SL)
Velocity of M2 Money Stock (M2V)
10-Year Treasury Constant Maturity Minus 3-Month Treasury Constant Maturity (T10Y3M)
10-Year Treasury Constant Maturity Minus 2-Year Treasury Constant Maturity (T10Y2Y)

3. **Fiscal policy**
Federal Debt: Total Public Debt as Percent of Gross Domestic Product (GFDEGDQ188S)
Federal Debt: Total Public Debt (GFDEBTN)

4. **Financial sector**
NASDAQ Composite Index (NASDAQCOM)
NASDAQ 100 Index (NASDAQ100)

## Analysis behind feature engineering

1. Moving averages
2. Differentiations
3. Decomposition
