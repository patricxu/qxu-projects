from Echart import *
import pandas as pd

def WECandlestick(title, subtitle=None, data=pd.DataFrame(), ma=[5,10,30]):
    def CalculateMA(period, data=[]):
        result = []
        for i in range(len(data)):
            if i < period:
                result.append('-')
                continue
            sum = 0
            for j in range(period):
                sum += data[i - j]
            result.append(sum / period)
        return result

    if isinstance(data, pd.DataFrame):
        colname = list(data.columns)
        expectedcol = ['date', 'open', 'close', 'high', 'low']
        try:
            assert len(list(filter(lambda x: x in expectedcol, colname))) == len(expectedcol)
        except AssertionError:
            print("The columns should contain 'date', 'open', 'lose', 'high', 'low'")
            return None

        date = list(data['date'])
        closes = list(data['close'])

        values = []
        for i in range(data.shape[0]):
            values.append([data['open'][i], data['close'][i], data['low'][i], data['high'][i]])
    else:
        print("The 'data' argument should be an instance of DataFrame")
        return None

    legendData = list(map(lambda x: 'MA'+str(x), ma))
    chart = Echart(title, subtitle, axis=True, align='left')
    chart.use(Candlestick(name="日k线", data=values))
    chart.use(Axis('category', 'bottom', data=date, scale=True, min=';dataMin', max='dataMax', splitNumber=20))
    chart.use(Axis('value', 'left', data=date, scale=True, splitArea={'show': 'true'}))
    chart.use(Tooltip(trigger='axis', axisPointer={'type': 'cross'}))
    chart.use(DataZoom([{'type': 'inside', 'start': 0, 'end': 100},
                        {'show': 'true', 'type': 'slider', 'y': '90%', 'start': 0, 'end': 100}]))
    chart.use(Legend(data=legendData))

    for i in ma:
        mavalue = CalculateMA(i, data=closes)
        chart.use(Line(name='MA'+str(i), data=mavalue, smooth=True, lineStyle={'normal': {'opacity': 0.5}}))

    return chart

def WEPie(title, subtitle, data=pd.DataFrame()):
    if isinstance(data, pd.DataFrame):
        colname = list(data.columns)
        expectedcol = ['value', 'name']
        try:
            assert len(list(filter(lambda x: x in expectedcol, colname))) == len(expectedcol)
        except AssertionError:
            print("The columns should contain 'value' and 'name'")
            return None

        values = []
        names = list(data['name'])
        for i in range(data.shape[0]):
            values.append({ 'name':data['name'][i], 'value':str(data['value'][i])})
    else:
        print("The 'data' argument should be an instance of DataFrame")
        return None

    chart = Echart(title, subtitle, align='center', axis=False)
    chart.use(Pie(name=None, radius='55%', center=['50%', '60%'], data=values, itemStyle={}))
    chart.use(Legend(orient='vertical', left='left', data=names))
    chart.use(Tooltip(trigger='item', formatter='{b} : {c} ({d}%)'))

    return chart

def WEBar(title=None, subtitle=None, data = pd.DataFrame(), stacks = [], category = []):
    if isinstance(data, pd.DataFrame):
        assert len(category) == data.shape[0]
        chart = Echart(title, subtitle)
        for i in range(data.shape[0]):
            tmp = list(map(lambda x: str(x), list(data.T[i])))
            chart.use(Series(type='bar', data=tmp, name=category[i], label={'normal':{'show':'true', 'position':'insideCenter'}}))

        chart.use(Axis('category', 'bottom', data=list(map(lambda x: str(x), list(data.columns)))))
        chart.use(Axis('value', 'left'))
        chart.use(Legend(left='center', data=category))
        chart.use(Tooltip(trigger=''))
    else:
        print("The 'data' argument should be an instance of DataFrame")
        return None
    return chart

def WERadar(title=None, subtitle=None, data = pd.DataFrame(), category = []):
    if isinstance(data, pd.DataFrame):
        assert len(category) == data.shape[0]
        chart = Echart(title, subtitle)

        seridata = []
        for i in range(data.shape[0]):
            tmp = list(map(lambda x: str(x), list(data.T[i])))
            seridata.append({'value': tmp, 'name': category[i]})

        chart.use(Series(type='radar', data=seridata))

        inds = []
        for name in data.columns:
            inds.append({'name': name, 'max': int(max(data[name] * 1.10))})

        chart.use(RadarCoord(indicator=inds))
        chart.use(Tooltip(trigger=''))
        chart.use(Legend(left='center', data=category))
    else:
        print("The 'data' argument should be an instance of DataFrame")
        return None
    return chart

def WELine(title=None, subtitle=None, data = pd.DataFrame(), category = []):
    if isinstance(data, pd.DataFrame):
        assert len(category) == data.shape[0]
        chart = Echart(title, subtitle)
        for i in range(data.shape[0]):
            tmp = list(map(lambda x: str(x), list(data.T[i])))
            chart.use(Series(type='line', data=tmp, name=category[i], smooth='True'))

        chart.use(Axis('category', 'bottom', data=list(map(lambda x: str(x), list(data.columns)))))
        chart.use(Axis('value', 'left'))
        chart.use(Legend(left='center', data=category))
        chart.use(Tooltip(trigger=''))
        chart.use(Toolbox(show='true', feature={'saveAsImage':{}}))
    else:
        print("The 'data' argument should be an instance of DataFrame")
        return None
    return chart