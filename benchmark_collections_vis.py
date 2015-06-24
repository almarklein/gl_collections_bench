""" Creating a visualization of the benchmarks. 
"""

import visvis as vv

measured_py_10m = {1:85, 10:85, 20:85, 30:85, 40:85, 50:55, 60:53, 70:41, 80:30, 90:24, 100:22, 200:5, 300:2.5, 400:1.3, 500:0.8}
measured_py_100k = {1:2200, 10:500, 20:250, 30:130, 40:80, 50:70, 60:53, 70:35, 80:28, 90:22, 100:20, 200:5, 300:2.5, 400:1.3, 500:0.8}
measured_js_10m_chrome = {1:60, 10:60, 20:55, 30:53, 40:40, 50:35, 60:30, 70:30, 80:28, 90:24, 100:22, 200:13, 300:11, 400:9, 500:7}
measured_js_100k_chrome = {1:60, 10:60, 20:60, 30:60, 40:60, 50:60, 60:55, 70:48, 80:42, 90:39, 100:35, 200:18, 300:12, 400:9, 500:7}
measured_js_10m_ff = {1:40, 10:40, 20:40, 30:40, 40:40, 50:35, 60:35, 70:32, 80:32, 90:32, 100:30, 200:30, 300:30, 400:30, 500:30}
measured_js_100k_ff = {1:60, 10:60, 20:60, 30:60, 40:60, 50:60, 60:60, 70:60, 80:60, 90:60, 100:60, 200:60, 300:60, 400:60, 500:60}

keys = list(sorted(measured_py_10m.keys()))

def samples(d):
    return [d[k] for k in keys]

f = vv.figure(1)
f.Clear()
a = vv.gca()

lw = 4
vv.plot(keys, samples(measured_py_10m), lw=lw, lc=(0.2, 0.4, 0.6), ls='-')
vv.plot(keys, samples(measured_py_100k), lw=lw, lc=(0.2, 0.4, 0.6), ls=':')

vv.plot(keys, samples(measured_js_10m_chrome), lw=lw, lc=(0.2, 0.6, 0.4), ls='-')
vv.plot(keys, samples(measured_js_100k_chrome), lw=lw, lc=(0.2, 0.6, 0.4), ls=':')

vv.plot(keys, samples(measured_js_10m_ff), lw=lw, lc=(0.8, 0.2, 0.0), ls='-')
vv.plot(keys, samples(measured_js_100k_ff), lw=lw, lc=(0.8, 0.2, 0.0), ls=':')

a.SetLimits((0, 500), (0, 99))
a.axis.showGrid = True
a.axis.xLabel = 'Number of GL programs'
a.axis.yLabel = 'FPS'
f.relativeFontSize = 1.3

vv.legend('Python 1M', 'Python 100k', 'Chrome 1M', 'Chrome 100k', 'Firefox 1M', 'Firefox 100k')
