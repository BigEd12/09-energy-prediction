# Energy Predictor

## Background
This was a challenge set from a few months ago. It surrounds the renewable energy sector and the output predicts how much energy would be produced by a wind farm

## Input
A txt document split into two sections:

### Observaciones (Observations)
Contains four values separated by a space:
- Energy produced
- U component
- V component
- Temperature
### Predicciones (Predictions)
Contains five values separated by a space:
- Date
- Time
- U Component
- V Component
- Temperature
  
## Output
A txt document split into three sections:

### Regresions (Regressions)
This section contains the coefficient and the y-intercept for each sector, rounded to two decimal places
### Errores (Errors)
This section contains the MAE and the MSE for each section as percentages of the energy produced.
### Predicciones (Predictions)
This section contains the date and time followed by the predictions
