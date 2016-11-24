# from http://matplotlib.org/users/screenshots.html#slider-demo
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider, Button
from scipy.stats import norm
import prettyplotlib as ppl

fig, ax = plt.subplots(1)
plt.subplots_adjust(left=0.1, bottom=0.25)

# Default parameters of the distribution
params = norm.stats()

# Initial plot
x = np.linspace(-5, 5, 100)

line_pdf, = ppl.plot(ax, x, norm.pdf(x, *params),
                     lw=2, color='red', label="pdf")
line_cdf, = ppl.plot(ax, x, norm.cdf(x, *params),
                     lw=1, color='lightgrey', label="cdf")
ppl.legend(ax)
# plt.axis([-10, 10, 0, 1])

## Updated plot on event
axcolor = 'lightgoldenrodyellow'
ax_params =[]
slider_params = []
for i in range(len(params)):
    ax_param = plt.axes([0.25, 0.1+i*.5, 0.65, 0.03], axisbg=axcolor, frameon=False)
    ax_params.append(ax_param)

    slider_param = Slider(ax_params[i], 'param '+str(i+1), 0.0, 30.0, valinit=params[i])
    slider_params.append(slider_param)


def update(val):
    updated_params = [0]*len(params)
    for i in range(len(params)):
        updated_params[i] = slider_params[i].val
    line_pdf.set_ydata(norm.pdf(x, *updated_params))
    line_cdf.set_ydata(norm.cdf(x, *updated_params))
    fig.canvas.draw_idle()


for i in range(len(params)):
    slider_params[i].on_changed(update)

resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')


def reset(event):
    for i in range(len(params)):
        slider_params[i].reset()


button.on_clicked(reset)

plt.show()
