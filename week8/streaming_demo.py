import hvplot.pandas
import hvplot.streamz
from streamz.dataframe import Random

# Create a demo streaming dataframe
df = Random(interval='1s', freq='50ms')

# Plot the data with a max of 100 rows
demoplot = df.hvplot(backlog=100)
hvplot.show(demoplot)