"""
Defines custom VizzuChart bokeh model to render Vizzu charts.
"""
from bokeh.core.properties import (
    Any, Dict, Instance, Int, List, String,
)
from bokeh.events import ModelEvent
from bokeh.models import LayoutDOM
from bokeh.models.sources import DataSource

from ..config import config


class VizzuEvent(ModelEvent):

    event_name = 'vizzu_event'

    def __init__(self, model, data=None):
        self.data = data
        super().__init__(model=model)


class VizzuChart(LayoutDOM):
    """
    A Bokeh model that wraps around an Vizzu chart and renders it
    inside a Bokeh.
    """

    __javascript_module_exports__ = ['Vizzu']

    __javascript_modules__ = [
        f"{config.npm_cdn}/vizzu@0.7.1/dist/vizzu.min.js"
    ]

    animation = Dict(String, Any)

    config = Dict(String, Any)

    columns = List(Dict(String, Any))

    source = Instance(DataSource, help="""
    Local data source to use when rendering glyphs on the plot.
    """)

    config = Dict(String, Any)

    duration = Int(500)

    style = Dict(String, Any)
