import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

data = pd.read_csv("/Users/lucasmazza/Desktop/CommonResearch/Data/Securities/MSFT_INCOME.csv")


quarters = data['fiscalDateEnding']
net_income = data['netIncome']
ebitda = data['ebitda']
# Create a DataFrame
df = pd.DataFrame({'Quarter': quarters, 'Net Income': net_income, 'ebitda': ebitda})

# Plot using Seaborn
sns.lineplot(data=df, x='Quarter', y='Net Income', marker='o', label='Net Income')
sns.lineplot(data=df, x='Quarter', y='ebitda', marker='s', label='ebitda')

# Add labels and title
plt.xlabel('Quarter')
plt.ylabel('Value')
plt.title('Progression by Quarter')

# Rotate x-axis labels
plt.xticks(rotation=45)

# Show legend
plt.legend()

# Display the plot
plt.tight_layout()
plt.show()

