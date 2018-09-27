import math

minDistance = 160 * 10**3
maxDistance = 2000 * 10**3

maxObjectSpeed = 16 * 10**3

angle = 1 * (math.pi / 180)

minArcDistance = minDistance * angle
maxArcDistance = maxDistance * angle

minObjectObservableTime = minArcDistance / maxObjectSpeed
maxObjectObservableTime = maxArcDistance / maxObjectSpeed

