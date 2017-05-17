# -*- coding: utf-8 -*-

"""
    echarts.option
    ~~~~~~~~~~~~~~

    Options for chart
"""

import json
import re

class JSObj(object):
    def __init__(self, objstr, key='', scope='local'):
        assert isinstance(objstr, str)
        if key:
            assert isinstance(key, str)
            self.key = key
        self.objstr = re.sub(r'\n|[^:]//.{0,}\n|/\*[\s\S]*\*/', '', objstr)
        #self.objstr = re.sub(r'\n|/\*[\s\S]*\*/', '', objstr)

        self.scope = scope

    @property
    def json(self):
        tmpstr = str('<jsobj>'+self.objstr+'</jsobj>')
        return tmpstr

class Base(object):
    def __str__(self):
        """JSON stringify format data."""
        return json.dumps(self.json)

    def __getitem__(self, key):
        return self.json.get(key)

    def keys(self):
        return self.json.keys()

    @property
    def json(self):
        raise NotImplementedError


class Axis(Base):
    """Axis data structure."""

    def __init__(self, type, position, name='', data=None, **kwargs):
        assert type in ('category', 'value', 'time', 'log')
        self.type = type
        assert position in ('bottom', 'top', 'left', 'right')
        self.position = position
        self.name = name
        self.data = data or []
        self._kwargs = kwargs

    def __repr__(self):
        return 'Axis<%s/%s>' % (self.type, self.position)

    @property
    def json(self):
        """JSON format data."""
        json = dict(
            type=self.type,
            position=self.position,
            data=self.data
        )
        if self.name:
            json['name'] = self.name

        if self._kwargs:
            json.update(self._kwargs)
        return json


class Legend(Base):
    """Legend section for Echart."""

    def __init__(self, data, orient='horizontal', position=None, **kwargs):
        self.data = data

        assert orient in ('horizontal', 'vertical')
        self.orient = orient
        if not position:
            position = ('center', 'top')
        self.position = position
        self._kwargs = kwargs

    @property
    def json(self):
        """JSON format data."""
        json = {
            'data': self.data,
            'orient': self.orient,
            'x': self.position[0],
            'y': self.position[1]
        }

        if self._kwargs:
            json.update(self._kwargs)
        return json


class Tooltip(Base):
    """A tooltip when hovering."""
    def __init__(self, trigger='axis', **kwargs):
        if trigger:
            self.trigger = trigger

        self._kwargs = kwargs

    @property
    def json(self):
        """JSON format data."""
        json = {}
        if hasattr(self, 'trigger'):
            json['trigger'] = self.trigger

        if self._kwargs:
            json.update(self._kwargs)
        return json


class Series(Base):
    """ Data series holding. """
    def __init__(self, type, name=None, data=None, **kwargs):
        types = (
            'bar', 'boxplot', 'candlestick', 'chord', 'effectScatter',
            'eventRiver', 'force', 'funnel', 'gauge', 'graph', 'heatmap',
            'k', 'line', 'lines', 'map', 'parallel', 'pie', 'radar',
            'sankey', 'scatter', 'tree', 'treemap', 'venn', 'wordCloud'
        )
        assert type in types
        self.type = type
        self.name = name
        self.data = data or []
        self._kwargs = kwargs

    @property
    def json(self):
        """JSON format data."""
        json = {
            'type': self.type,
            'data': self.data
        }
        if self.name:
            json['name'] = self.name
        if self._kwargs:
            json.update(self._kwargs)
        return json


class Toolbox(Base):
    """ A toolbox for visitor. """

    def __init__(self, orient='horizontal', position=None, **kwargs):
        assert orient in ('horizontal', 'vertical')
        self.orient = orient
        if not position:
            position = ('right', 'top')
        self.position = position
        self._kwargs = kwargs

    @property
    def json(self):
        """JSON format data."""
        json = {
            'orient': self.orient,
            'x': self.position[0],
            'y': self.position[1]
        }
        if self._kwargs:
            json.update(self._kwargs)
        return json

class DataZoom(Base):
    def __init__(self, objs):
        self.objs = objs

    @property
    def json(self):
        assert isinstance(self.objs, list)
        return self.objs

class Polar(Base):
    def __init__(self):
        pass

    @property
    def json(self):
        json = {}
        return json

class AngleAxis(Base):
    def __init__(self, type='value', startAngle=0, **kwargs):
        self.type = type
        self.startangle = startAngle
        self._kwargs = kwargs

    @property
    def json(self):
        json = {
            'type': self.type,
            'startAngle': self.startangle
        }
        if self._kwargs:
            json.update(self._kwargs)
        return  json

class Grid(Base):
    def __init__(self, **kwargs):
        self._kwargs = kwargs

    @property
    def json(self):
        json = {}
        if self._kwargs:
            json.update(self._kwargs)
        return  json

class RadarCoord(Base):
    def __init__(self, **kwargs):
        self._kwargs = kwargs

    @property
    def json(self):
        json = {}
        if self._kwargs:
            json.update(self._kwargs)
        return  json

class RadiusAxis(Base):
    def __init__(self):
        pass

    @property
    def json(self):
        json = {}
        return json

class BackgroundColor(Base):
    def __init__(self, color=None, **kwargs):
        self.color = color
        self._kwargs = kwargs
        pass

    @property
    def json(self):
        if isinstance(self.color, JSObj):
            return self.color.json
        elif isinstance(self.color, str):
            return self.color

        json = {}
        if self._kwargs:
            json.update(self._kwargs)
        return json

class Title(Base):
    def __init__(self, text='', subtext='', left='left', **kwargs):
        self.text = text
        self.subtext = subtext
        self.left = left
        self._kwargs = kwargs
        pass

    @property
    def json(self):
        json = {
            'text': self.text,
            'subtext': self.subtext,
            'left': self.left,
        }
        if self._kwargs:
            json.update(self._kwargs)
        return json

class VisualMap(Base):
    """maps data to visual channels"""

    def __init__(self, type, min, max,  **kwargs):
        assert type in ("continuous", "piecewise")
        self.type = type
        self.min = min
        self.max = max
        self._kwargs = kwargs

    @property
    def json(self):
        """JSON format data"""
        json = {
            "type": self.type,
            'min': self.min,
            'max': self.max
        }
        if self._kwargs:
            json.update(self._kwargs)
        return json

