# from http://matplotlib.org/users/screenshots.html#slider-demo
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider, Button
from scipy.stats import norm
import prettyplotlib as ppl

fig, ax = plt.subplots(1)
plt.subplots_adjust(left=0.1, bottom=0.25)

# Default parameters of the distribution
mu, sigma, _, _ = norm.stats(moments='mvsk')

## Initial plot
x = np.linspace(-5, 5, 100)

line_pdf, = ppl.plot(ax, x, norm.pdf(x, mu, sigma),
                     lw=2, color='red', label="pdf")
line_cdf, = ppl.plot(ax, x, norm.cdf(x, mu, sigma),
                     lw=1, color='green', label="cdf")
ppl.legend(ax)
# plt.axis([-10, 10, 0, 1])

## Updated plot on event
axcolor = 'lightgoldenrodyellow'
ax_mu = plt.axes([0.25, 0.15, 0.65, 0.03], axisbg=axcolor, frameon=False)
ax_sigma = plt.axes([0.25, 0.1, 0.65, 0.03], axisbg=axcolor, frameon=False)

slider_mu = Slider(ax_mu, 'mu', 0.0, 30.0, valinit=mu)
slider_sigma = Slider(ax_sigma, 'sigma', 0.1, 10.0, valinit=sigma)


def update(val):
    updated_mu = slider_mu.val
    update_sigma = slider_sigma.val
    line_pdf.set_ydata(norm.pdf(x, updated_mu, update_sigma))
    line_cdf.set_ydata(norm.cdf(x, updated_mu, update_sigma))
    fig.canvas.draw_idle()


slider_mu.on_changed(update)
slider_sigma.on_changed(update)

resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')


def reset(event):
    slider_mu.reset()
    slider_sigma.reset()


button.on_clicked(reset)

plt.show()
