# stuartplot - A simple wrapper for matplotlib

I frequently use the same matplotlib options in my visualisations. This is a simple wrapper which simplifies these options for me.
## Installation

```bash
pip install stuartplot
```

## Quickstart
Simple example:
```python 
from stuartplot import Figure

fig = Figure(
                figsize=(12, 5),
                title="Figure Title", 
                title_size=25,
                lay=(1, 2), 
                spacing=(.3, .5)
                )

fig.axes[0].plot(np.arange(10), np.arange(10)**2, label='Trace 1')
fig.axes[1].hist(np.random.randn(100), color='r')

fig.label(axis=0, labels=('Plot 1 Title', 'Plot 1 xlabel', 'Plot 1 ylabel'), sizes=(20, 15, 15))
fig.label(axis=1, labels=('Plot 2 Title', 'Plot 2 xlabel', 'Plot 2 ylabel'), sizes=(20, 15, 15))

fig.show()
```

