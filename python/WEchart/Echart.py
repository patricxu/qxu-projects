# -*- coding: utf-8 -*-
import os
import logging
from option import *
from datastructure import *
from IPython.core.display import display, HTML

__version__ = '0'
__release__ = '0'
__author__ = ''

divid = 0

class Echart(Base):
    def __init__(self, title=None, description=None, align='center', **kwargs):
        if title:
            self.title = Title(text=title, subtext=description, left=align)

        self.x_axis = []
        self.y_axis = []
        self.series = []
        self.kwargs = kwargs
        self.jsobjs = []
        self.g_jsobjs = []
        self.grid = []

        self.logger = logging.getLogger(__name__)

    def use(self, obj):
        if isinstance(obj, JSObj):
            if obj.scope == 'local':
                self.jsobjs.append(obj)
            elif obj.scope == 'global':
                self.g_jsobjs.append(obj)

        if isinstance(obj, Title):
            self.title = obj

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
            self.grid.append(obj)
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
        json = {}

        if hasattr(self, 'title'):
            json['title'] = self.title.json

        if len(self.series) > 0:
            json['series'] = list(map(dict, self.series))

        if len(self.x_axis):
            json['xAxis'] = list(map(dict, self.x_axis)) or [{}]

        if len(self.y_axis):
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
        if hasattr(self, 'radarCoord'):
            json['radar'] = self.radarCoord.json
        if hasattr(self, 'backgroundColor'):
            json['backgroundColor'] = self.backgroundColor.json

        for obj in self.jsobjs:
            json[obj.key] = obj.json

        if len(self.grid) > 0:
            json['grid'] = list(map(dict, self.grid))

        json.update(self.kwargs)
        return json

    def _html(self):
        with open(os.path.join(os.path.dirname(__file__), 'plot.js'), encoding='utf8') as f:
            template = f.read()
            global divid
            template = template.replace('{{ id }}', str(divid))
            divid = divid+1
            if self.json == {}:
                template = template.replace('{{ opt }}', 'option')
            else:
                template = template.replace('{{ opt }}', json.dumps(self.json, indent=4))

            if len(self.g_jsobjs) > 0:
                tmp = ''
                for obj in self.g_jsobjs:
                    tmp += obj.json
                tmp = tmp.replace('<jsobj>', '')
                tmp = tmp.replace('</jsobj>', '')
                template = template.replace('{{ globaljsobj }}', tmp)
            else:
                template = template.replace('{{ globaljsobj }}', '')

            template = template.replace('"<jsobj>', '')
            template = template.replace('</jsobj>"', '')

            return template

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

