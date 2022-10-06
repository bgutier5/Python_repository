import matplotlib
matplotlib.use("TKAGG")
import matplotlib.pyplot as pyplot
import mpl_toolkits.mplot3d

figure = pyplot.figure()
figure.subplots_adjust(bottom=0.25, top=0.75)
axes = figure.gca(projection='3d')
xLabel = axes.set_xlabel('XXX xxxxxx xxxx x xx x')
yLabel = axes.set_ylabel('YY (y) yyyyyy')
zLabel = axes.set_zlabel('Z zzzz zzz (z)')
plot = axes.plot([1,2,3],[1,2,3])

pyplot.show()
