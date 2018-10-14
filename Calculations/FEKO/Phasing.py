import math
import numpy
import matplotlib.pyplot as plt
import itertools


speedOfLight = 3*10**8
minDistance = 160 * 10**3
maxDistance = 2000 * 10**3
earthRadius = 6378 * 10**3
centerFrequency = 610*10**6
gravitationalConstant = 6.67408 * 10 ** -11
earthMass = 5.972 * 10 ** 24
boltzmannsConstant = 1.38064852e-23

# Lambda
Lambda = speedOfLight / centerFrequency

beta = (2 * math.pi)/(Lambda)


dx = Lambda/2
dy = Lambda/2

theta = 10
psi = 10

maxAmplitude = 1
minAmplitude = 0.5

w,h = 32,32
phaseMatrix = [[0 for x in range(w)] for y in range(h)]

f = open("phase.txt", "w+")
newline = ""
for x in range(0,32):
    thetaSteer = x * (360 * dx * math.sin(math.radians(theta)))/(Lambda)
    for y in range(0,32):
        psiSteer = y * (360 * dy * math.sin(math.radians(psi)))/(Lambda)
        totalSteer = thetaSteer + psiSteer
        phaseMatrix[x][y] = totalSteer
        outLine = newline + "1.0," + str(totalSteer)
        newline = "\n"
        f.write(outLine)

fig = plt.figure(figsize=(6, 3.2))

ax = fig.add_subplot(111)
ax.set_title('colorMap')
plt.imshow(phaseMatrix)
ax.set_aspect('equal')

cax = fig.add_axes([0.12, 0.1, 0.78, 0.8])
cax.get_xaxis().set_visible(False)
cax.get_yaxis().set_visible(False)
cax.patch.set_alpha(0)
cax.set_frame_on(False)
plt.colorbar(orientation='vertical')
plt.show()


#Amplitude
w,h = 32,32
amplitudeMatrix = [[0 for x in range(w)] for y in range(h)]

delta = numpy.linspace(0.5, 1.0, 16)
deltaReverse = numpy.linspace(1.0, 0.5, 16)
comb = numpy.concatenate((delta,deltaReverse))


for x in range(0,32):
    first = comb[x]
    for y in range(0,32):
        second = comb[y]
        amplitudeMatrix[x][y] = (first + second)/2

print(amplitudeMatrix)

fig = plt.figure(figsize=(6, 3.2))

ax = fig.add_subplot(111)
ax.set_title('colorMap')
plt.imshow(amplitudeMatrix)
ax.set_aspect('equal')

cax = fig.add_axes([0.12, 0.1, 0.78, 0.8])
cax.get_xaxis().set_visible(False)
cax.get_yaxis().set_visible(False)
cax.patch.set_alpha(0)
cax.set_frame_on(False)
plt.colorbar(orientation='vertical')
plt.show()

flattenedPhase = []
for x in phaseMatrix:
    for y in x:
        flattenedPhase.append(y)

flattenedAmplitude = []
for x in amplitudeMatrix:
    for y in x:
        flattenedAmplitude.append(y)

newline = ""
f = open("Amplitude.txt", "w+")
for x in range(0,1024):
    outLine = newline + str(flattenedAmplitude[x])  + ",0.0"
    newline = "\n"
    f.write(outLine)

newline = ""
f = open("AmplitudePhase.txt", "w+")
for x in range(0,1024):
    outLine = newline + str(flattenedAmplitude[x]) + "," + str(flattenedPhase[x])
    newline = "\n"
    f.write(outLine)