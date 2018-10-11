# Observable time or Dwell Time

import math

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

# Tangential velocity
minObjectPeriod = 5280 # Seconds
maxObjectPeriod = 7620 # Seconds
maxObjectSpeed = (2 * math.pi * (earthRadius+minDistance))/(minObjectPeriod)
test = math.sqrt((gravitationalConstant * earthMass)/(earthRadius+minDistance))

# Maximum Angle (from zenith)
maxAngle = 60 * (math.pi / 180)

# Max doppler shift
dopplerFrequencyShift = 2*((maxObjectSpeed)/(speedOfLight))*centerFrequency 

elevation = (math.pi)/2 - maxAngle
targetDistance = earthRadius * (math.sqrt((((earthRadius + maxDistance)**2)/(earthRadius**2)) - (math.cos(elevation)**2 )) - math.sin(elevation))
maxTargetDistance = earthRadius * (math.sqrt((((earthRadius + maxDistance)**2)/(earthRadius**2)) - (math.cos((math.pi/2 )-(math.pi/3))**2 )) - math.sin((math.pi/2 )-(math.pi/3)))
# Path Loss of signal (one direction)
pathLoss = (Lambda/(4 * math.pi * targetDistance))


# Observable Time
observableTime = (((earthRadius + maxDistance)**(3.0/2.0))/(math.sqrt(gravitationalConstant * earthMass))) * (math.pi - 2 * elevation - 2 * math.asin((earthRadius)/(earthRadius + maxDistance) * math.cos(elevation)))

# Minimum radar cross section of object (min diameter of 10 cm)
minObjectRadius = 10 * 10**-2
minRCS = math.pi * minObjectRadius**2

# Signal Round trip times
minRoundTripTime = 2 * (minDistance/speedOfLight)
maxRoundTripTime = 2 * (maxTargetDistance/speedOfLight)

# Pulse Width and Range Resolution Limits
maxBandwidth = 4 * 10**6
pulseWidthMin = 1/maxBandwidth
rangeResolutionMin = (speedOfLight * pulseWidthMin)/(2)



# rangeResolution = 1
# pulseWidth = (2*rangeResolution)/(speedOfLight)


print(rangeResolutionMin)

# Thermal Noise
noiseFigure = 7.94 # This should be calculated
bandwidth = 1/pulseWidthMin
thermalNoise = boltzmannsConstant * 290 * noiseFigure * bandwidth
print(thermalNoise)
# print(bandwidth/(1000000))




