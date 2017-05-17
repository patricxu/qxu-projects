# -*- coding: utf-8 -*-
import os
import json
import logging
import tempfile
import webbrowser
from option import *
#from option import Axis, Legend, Series, Tooltip, Toolbox, VisualMap
from datastructure import *
from IPython.display import HTML
from IPython.core.display import display, HTML

import pandas as pd

__version__ = '0'
__release__ = '0'
__author__ = ''

divid = 0

class Echart(Base):
    def __init__(self, title, description=None, axis=False, align='center', **kwargs):
        self.title = {
            'text': title,
            'subtext': description,
            'x': align,
        }

        self.axis = axis
        if self.axis:
            self.x_axis = []
            self.y_axis = []

        self.series = []
        self.kwargs = kwargs

        self.logger = logging.getLogger(__name__)

    def use(self, obj):
        if isinstance(obj, Axis):
            if obj.position in ('bottom', 'top'):
                self.x_axis.append(obj)
            else:
                self.y_axis.append(obj)
            return self

        if isinstance(obj, Legend):
            self.legend = obj
        elif isinstance(obj, Tooltip):
            self.tooltip = obj
        elif isinstance(obj, Series):
            self.series.append(obj)
        elif isinstance(obj, Toolbox):
            self.toolbox = obj
        elif isinstance(obj, VisualMap):
            self.visualMap = obj
        elif isinstance(obj, DataZoom):
            self.dataZoom = obj
        elif isinstance(obj, Polar):
            self.polar = obj
        elif isinstance(obj, AngleAxis):
            self.angleAxis = obj
        elif isinstance(obj, RadiusAxis):
            self.radiusAxis = obj
        elif isinstance(obj, Grid):
            self.grid = obj
        elif isinstance(obj, RadarCoord):
            self.radarCoord = obj
        elif isinstance(obj, BackgroundColor):
            self.backgroundColor = obj

        return self

    @property
    def data(self):
        return self.series

    @property
    def json(self):
        """JSON format data."""
#        print("1111111111111")
        json = {
            'title': self.title,
            'series': list(map(dict, self.series)),
        }
#        print("2222222222222222")
#        print(type(self.series))

        if self.axis:
            json['xAxis'] = list(map(dict, self.x_axis)) or [{}]
            json['yAxis'] = list(map(dict, self.y_axis)) or [{}]

        if hasattr(self, 'legend'):
            json['legend'] = self.legend.json
        if hasattr(self, 'tooltip'):
            json['tooltip'] = self.tooltip.json
        if hasattr(self, 'toolbox'):
            json['toolbox'] = self.toolbox.json
        if hasattr(self, 'visualMap'):
            json['visualMap'] = self.visualMap.json
        if hasattr(self, 'dataZoom'):
            json['dataZoom'] = self.dataZoom.json
        if hasattr(self, 'polar'):
            json['polar'] = self.polar.json
        if hasattr(self, 'angleAxis'):
            json['angleAxis'] = self.angleAxis.json
        if hasattr(self, 'radiusAxis'):
            json['radiusAxis'] = self.radiusAxis.json
        if hasattr(self, 'grid'):
            json['grid'] = self.grid.json
        if hasattr(self, 'radarCoord'):
            json['radar'] = self.radarCoord.json
        if hasattr(self, 'backgroundColor'):
            json['backgroundColor'] = self.backgroundColor.json

        json.update(self.kwargs)
        return json

    def _html(self):
        with open(os.path.join(os.path.dirname(__file__), 'plot.js'), encoding='utf8') as f:
            template = f.read()
            global divid
            template = template.replace('{{ id }}', str(divid))
            divid = divid+1
            return template.replace('{{ opt }}', json.dumps(self.json, indent=4))

    def plot(self, persist=True, debug=False):
        """
        Plot into html file

        :param persist: persist output html to disk
        """
        if debug:
            print(self._html())

        #display(HTML(self._html()))
        return HTML(self._html())

    def save(self, path, name):
        """
        Save html file into project dir
        :param path: project dir
        :param name: html file name
        """
        if not os.path.exists(path):
            os.makedirs(path)
        with open(path+str(name)+".html", "w") as html_file:
            html_file.write(self._html())

