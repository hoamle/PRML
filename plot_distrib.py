# from http://matplotlib.org/users/screenshots.html#slider-demo
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider, Button
import scipy.stats
import prettyplotlib as ppl


def prepare_params(distrib_method_name):
    if distrib_method_name is 'norm':
        params = [0, 1]
        rangexy = [-5, 5, 0, 1]
    elif distrib_method_name is 'beta':
        params = [1, 1]
        rangexy = [0, 1, 0, 3]
    else: # take 'norm'-related values
        params = [0, 1]
        rangexy = [-5, 5, 0, 1]

    return params, rangexy


def plot_distrib(distrib_method_name):
    fig, ax = plt.subplots(1)
    ax.set_title(distrib_method_name + " distribution")
    plt.subplots_adjust(left=0.1, bottom=0.25)

    # Default parameters of the distribution
    params, rangexy = prepare_params(distrib_method_name)
    distrib = getattr(scipy.stats, distrib_method_name)  # call method norm() from string 'norm'

    # Initial plot
    x = np.linspace(rangexy[0], rangexy[1], 100)
    line_pdf, = ppl.plot(ax, x, distrib.pdf(x, *params),
                         lw=2, color='red', label="pdf")
    line_cdf, = ppl.plot(ax, x, distrib.cdf(x, *params),
                         lw=1, color='lightgrey', label="cdf")
    plt.axis(rangexy)
    ppl.legend(ax)

    ## Updated plot on event
    axcolor = 'lightgoldenrodyellow'
    ax_params = []
    slider_params = []
    for i in range(len(params)):
        ax_param = plt.axes([0.25, 0.15 - i * .05, 0.65, 0.03], axisbg=axcolor, frameon=False)
        ax_params.append(ax_param)

        slider_param = Slider(ax_params[i], 'param ' + str(i + 1), 0.1, 10.0, valinit=params[i])
        slider_params.append(slider_param)

    def update(val):
        updated_params = [0] * len(params)
        for i in range(len(params)):
            updated_params[i] = slider_params[i].val
        line_pdf.set_ydata(distrib.pdf(x, *updated_params))
        line_cdf.set_ydata(distrib.cdf(x, *updated_params))
        fig.canvas.draw_idle()

    for slider_param in slider_params:
        slider_param.on_changed(update)

    resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
    button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')

    def reset(event):
        for slider_param in slider_params:
            slider_param.reset()

    button.on_clicked(reset)  # NOT working when wrapped inside plot_distrib()

    plt.show()