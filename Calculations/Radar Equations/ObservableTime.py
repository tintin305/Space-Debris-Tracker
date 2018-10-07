# Observable time or Dwell Time

import math

speedOfLight = 3*10**8
minDistance = 160 * 10**3
maxDistance = 2000 * 10**3
earthRadius = 6378 * 10**3
centerFrequency = 610*10**6
gravitationalConstant = 6.67408 * 10 ** -11
earthMass = 5.972 * 10 ** 24

# Lambda
Lambda = speedOfLight / centerFrequency

# Tangential velocity
maxObjectSpeed = 7.795 * 10**6


# Maximum Angle (from zenith)
maxAngle = 60 * (math.pi / 180)

# minArcDistance = minDistance * angle
# maxArcDistance = maxDistance * angle

# minObjectObservableTime = minArcDistance / maxObjectSpeed
# maxObjectObservableTime = maxArcDistance / maxObjectSpeed

# Max doppler shift
dopplerFrequencyShift = 2*((maxObjectSpeed)/(speedOfLight))*centerFrequency 

elevation = (math.pi)/2 - maxAngle
targetDistance = earthRadius * (math.sqrt((((earthRadius + maxDistance)**2)/(earthRadius**2)) - (math.cos(elevation)**2 )) - math.sin(elevation))

# Path Loss of signal (one direction)
pathLoss = (Lambda/(4 * math.pi * targetDistance))


# Observable Time
observableTime = (((earthRadius + maxDistance)**(3.0/2.0))/(math.sqrt(gravitationalConstant * earthMass))) * (math.pi - 2 * elevation - 2 * math.asin((earthRadius)/(earthRadius + maxDistance) * math.cos(elevation)))


