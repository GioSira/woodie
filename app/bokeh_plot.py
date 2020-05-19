from bokeh.embed import components
from bokeh.plotting import figure
from bokeh.resources import INLINE
import math


def plot_scores(datalist):

    data = sorted(datalist, key=lambda x: x["created_at"], reverse=False)

    x_labels = []
    y_values_open = []
    y_values_wb = []
    y_values_total = []
    x_range = []

    for i,d in enumerate(data):
        x_range.append(i)
        x_labels.append(d["created_at"])
        #y_values_open.append(d["open"])
        y_values_wb.append(d["wb"])
        #y_values_total.append(d["open"]+d["wb"])


    fig = figure(plot_width=800, plot_height=600,
                 x_axis_label="Date", y_axis_label='Score')

    fig.line(x_range, y_values_open, line_width=3, line_alpha=0.6, line_color="blue", legend="open data")
    fig.line(x_range, y_values_wb, line_width=3, line_alpha=0.6, line_color='red', legend='whisteblower')
    fig.line(x_range, y_values_total, line_width=3, line_alpha=0.6, line_color='#f46d43', legend="both")

    fig.circle(x_range, y_values_total, fill_color='#f46d43', line_color='#f46d43', size=8)
    fig.circle(x_range, y_values_wb, fill_color='red', line_color='red', size=8)
    fig.circle(x_range, y_values_open, fill_color='blue', line_color='blue', size=8)

    fig.xaxis.ticker = x_range
    fig.xaxis.major_label_overrides = {i:v for (i,v) in zip(x_range, x_labels)}
    fig.xaxis.major_label_orientation = math.pi / 4

    js_resources = INLINE.render_js()
    css_resources = INLINE.render_css()

    script, div = components(fig)

    return script, div, js_resources, css_resources

