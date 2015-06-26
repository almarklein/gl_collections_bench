""" Creating a visualization of the benchmarks. 
"""

import visvis as vv
from collections import OrderedDict

measurements_100k = OrderedDict()
measurements_100k['Python Linux (Nvidia)'] = {1:2700, 10:760, 20:337, 40:121, 60:61, 80:38, 100:26, 200:7, 300:3.4, 400:1.9, 500:1.2}
measurements_100k['Python Windows (Nvidia)'] = {1:1500, 10:712, 20:470, 40:248, 60:170, 80:125, 100:95, 200:41, 300:23, 400:15, 500:11}
measurements_100k['Python Windows (Intel)'] = {1:930, 10:365, 20:220, 40:116, 60:77, 80:56, 100:44, 200:19, 300:11, 400:7, 500:5}
measurements_100k['Firefox Linux (Nvidia)'] = {1:60, 10:60, 20:60, 30:60, 40:60, 50:60, 60:60, 70:60, 80:60, 90:60, 100:60, 200:60, 300:60, 400:60, 500:60}
measurements_100k['Firefox Windows (Nvidia)'] = {1:60, 10:60, 20:60, 30:60, 40:60, 50:60, 60:60, 70:60, 80:60, 90:60, 100:60, 200:60, 300:60, 400:60, 500:60}
measurements_100k['Firefox Windows (Intel)'] = {1:60, 10:60, 20:60, 30:60, 40:60, 50:60, 60:60, 70:60, 80:60, 90:60, 100:60, 200:60, 300:60, 400:60, 500:60}
#measurements_100k['Chrome Linux (Nvidia)'] = {1:60, 10:60, 20:60, 30:60, 40:60, 50:60, 60:55, 70:48, 80:42, 90:39, 100:35, 200:18, 300:12, 400:9, 500:7}
measurements_100k['Chrome Linux (Nvidia)'] = {1:60, 10:60, 20:60, 40:60, 60:60, 80:60, 100:57, 200:29, 300:20, 400:16, 500:12}
measurements_100k['Chrome Windows (Nvidia)'] = {1:60, 10:60, 20:60, 40:60, 60:60, 80:60, 100:55, 200:32, 300:21, 400:17, 500:14}
measurements_100k['Chrome Windows (Intel)'] = {1:60, 10:60, 20:60, 40:60, 60:60, 80:60, 100:53, 200:29, 300:20, 400:15, 500:12}

measurements_10m = OrderedDict()
measurements_10m['Python Linux (Nvidia)'] = {1:85, 10:85, 20:85, 30:85, 40:85, 50:55, 60:53, 70:41, 80:30, 90:24, 100:22, 200:5, 300:2.5, 400:1.3, 500:0.8}
measurements_10m['Firefox Linux (NVidia)'] = {1:40, 10:40, 20:40, 30:40, 40:40, 50:35, 60:35, 70:32, 80:32, 90:32, 100:30, 200:30, 300:30, 400:30, 500:30}
measurements_10m['Chrome Linux (Nvidia)'] = {1:60, 10:60, 20:55, 30:53, 40:40, 50:35, 60:30, 70:30, 80:28, 90:24, 100:22, 200:13, 300:11, 400:9, 500:7}

measurements_100k_buffer = OrderedDict()
measurements_100k_buffer['Python Linux (Nvidia)'] = {1:2700, 10:780, 20:372, 40:150, 60:80, 80:50, 100:34, 200:11, 300:5, 400:2.8, 500:1.8}
measurements_100k_buffer['Python Windows (Nvidia)'] = {1:1550, 10:678, 20:424, 40:244, 60:165, 80:125, 100:100, 200:44, 300:27, 400:18, 500:14}
measurements_100k_buffer['Python Windows (Intel)'] = {1:1570, 10:660, 20:440, 40:244, 60:162, 80:125, 100:99, 200:46, 300:27, 400:19, 500:14}
measurements_100k_buffer['Chrome Linux (Nvidia)'] = {1:60, 10:60, 20:60, 40:60, 60:60, 80:60, 100:58, 200:30, 300:20, 400:16, 500:13}
measurements_100k_buffer['Chrome Windows (Nvidia)'] = {1:60, 10:60, 20:60, 40:60, 60:60, 80:60, 100:60, 200:32, 300:22, 400:17, 500:14}
measurements_100k_buffer['Chrome Windows (Intel)'] = {1:60, 10:60, 20:60, 40:60, 60:60, 80:60, 100:60, 200:33, 300:22, 400:16, 500:13}


def plot(title, data, colors, linestyles):
    f = vv.figure()
    f.Clear()
    a = vv.gca()
    vv.title(title)
    
    lw = 4
    
    
    i = -1
    for key, d in data.items():
        i +=1 
        mm = list(sorted(d))
        vv.plot(mm, [d[k] for k in mm], lw=lw, lc=colors[i], ls=linestyles[i])
    
    a.SetLimits((0, 500), (0, 99))
    a.axis.showGrid = True
    a.axis.xLabel = 'Number of GL programs'
    a.axis.yLabel = 'FPS'
    f.relativeFontSize = 1.2
    
    vv.legend(*data.keys())

# Draw 100K
colors = [(0.2, 0.4, 0.6), (0.2, 0.4, 0.6), (0.2, 0.4, 0.6),  (0.8, 0.4, 0.0), (0.8, 0.4, 0.0), (0.8, 0.4, 0.0), (0.2, 0.6, 0.4), (0.2, 0.6, 0.4), (0.2, 0.6, 0.4)]
linestyles = '-', '--', ':', '-', '--', ':', '-', '--', ':'
plot('100K vertices', measurements_100k, colors, linestyles)


# Draw 10M
colors = [(0.2, 0.4, 0.6), (0.8, 0.4, 0.0), (0.2, 0.6, 0.4),]
linestyles = '-', '--', ':'
plot('10M vertices', measurements_10m, colors, linestyles)


# Draw buffers
colors = [(0.2, 0.4, 0.6), (0.2, 0.4, 0.6), (0.2, 0.4, 0.6), (0.2, 0.6, 0.4), (0.2, 0.6, 0.4), (0.2, 0.6, 0.4),]
linestyles = '-', '--', ':', '-', '--', ':'
plot('multi-buffer (100K vertices)', measurements_100k_buffer, colors, linestyles)

# Draw ghosts
colors = [(0, 0, 1), (0, 0, 1), (0, 0, 1), (0, 1, 0), (0, 1, 0), (0, 1, 0)]
i = -1
for key, d in measurements_100k.items():
    if 'Firefox' in key:
        continue
    i +=1 
    mm = list(sorted(d))
    vv.plot(mm, [d[k] for k in mm], lw=4, lc=colors[i], ls=linestyles[i], alpha=0.15, axesAdjust=False)
vv.xlabel('Number of GL buffers')

# vv.screenshot('benchmark_collections_resultX.jpg', bg='w')
