# Observable time or Dwell Time

import math
import numpy

speedOfLight = 3*10**8
minDistance = 160 * 10**3
maxDistance = 2000 * 10**3
earthRadius = 6378 * 10**3
centerFrequency = 610*10**6
gravitationalConstant = 6.67408 * 10 ** (-11)
earthMass = 5.972 * 10 ** (24)
boltzmannsConstant = 1.38064852*10**-(23)
standardTemp = 290
numElements = 4096

# Lambda
Lambda = speedOfLight / centerFrequency

# Tangential velocity
minObjectPeriod = 5280 # Seconds
maxObjectPeriod = 7620 # Seconds
# maxObjectSpeed = (2 * math.pi * (earthRadius+minDistance))/(minObjectPeriod)
maxObjectSpeed = math.sqrt((gravitationalConstant * earthMass)/(earthRadius+minDistance))
minObjectSpeed = math.sqrt((gravitationalConstant * earthMass)/(earthRadius+maxDistance))

# Maximum Angle (from zenith)
maxAngle = 30 * (math.pi / 180)



# Slant Distance
elevation = (math.pi)/2 - maxAngle
maxSlantDistance = earthRadius * (math.sqrt((((earthRadius + maxDistance)**2)/(earthRadius**2)) - (math.cos(elevation)**2 )) - math.sin(elevation)) # Taking in the max angle (from zenith) and max distance
minSlantDistance = earthRadius * (math.sqrt((((earthRadius + minDistance)**2)/(earthRadius**2)) - (math.cos(elevation)**2 )) - math.sin(elevation)) # Taking in the max angle (from zenith) and min distance

maxSlantDistanceFOV = earthRadius * (math.sqrt((((earthRadius + maxDistance)**2)/(earthRadius**2)) - (math.cos((math.pi/2 )-(math.pi/3))**2 )) - math.sin((math.pi/2 )-(math.pi/3))) # Assuming 120 degrees FOV

# Path Loss of signal (one direction)
pathLoss = (Lambda/(4 * math.pi * maxSlantDistance))


# Observable Time
maxObservableTime = (((earthRadius + maxDistance)**(3.0/2.0))/(math.sqrt(gravitationalConstant * earthMass)))*(math.pi - 2 * elevation - 2 * math.asin((earthRadius)/(earthRadius + maxDistance) * math.cos(elevation)))


# Angular Velocity
maxAngularVelocity = (maxObjectSpeed)/(minDistance)
minAngularVelocity = (minObjectSpeed)/(maxDistance)


# Apparent Angular Velocity
apparentAngularVelicity = (2 * maxAngle)/(maxObservableTime)

# Linear Velocity (measured from center of earth of from system)
minLinearVelocity = apparentAngularVelicity * minDistance
maxLinearVelocity = apparentAngularVelicity * maxDistance

# Max doppler shift
dopplerFrequencyShift = 2*((maxLinearVelocity)/(speedOfLight))*centerFrequency 


# Minimum radar cross section of object (min diameter of 10 cm)
minObjectRadius = 5 * 10**(-2)
minRCS = math.pi * minObjectRadius**(2)

# Signal Round trip times
minRoundTripTime = 2 * (minDistance/speedOfLight)
maxRoundTripTime = 2 * (maxSlantDistance/speedOfLight)
test = 2 * (maxDistance/speedOfLight)


# Pulse Width and Range Resolution Limits
maxBandwidth = 8 * 10**6
pulseWidthMin = 1/maxBandwidth
pulseWidthMax = minRoundTripTime
rangeResolutionMin = (speedOfLight * pulseWidthMin)/(2)

#Bandwidth max with minimum pulse width
bandwidthMax = 1/pulseWidthMin


# rangeResolution = 1
# pulseWidth = (2*rangeResolution)/(speedOfLight)

# Minimum Number of Pulses (based on HPBW of simulation)
HPBW = 1.30417 * (math.pi / 180)
elevationStationary = math.pi/2 - HPBW
maxObservableTimeStationary = (((earthRadius + minDistance)**(3.0/2.0))/(math.sqrt(gravitationalConstant * earthMass)))*(math.pi - 2 * elevationStationary - 2 * math.asin((earthRadius)/(earthRadius + minDistance) * math.cos(elevationStationary)))
maxNumPulses = maxObservableTimeStationary/maxRoundTripTime
# Safe estimate pulse number
numPulses = 50

# Thermal Noise
noiseFiguredB = 2.5 # Measured in dB
noiseFigure = 10**(noiseFiguredB/10)

pulseWidth = 1 * 10**(-6)
bandwidth = 1 / pulseWidth
SNRmindB = 10 #Measured in dB
SNRmin = 10**(SNRmindB/10)

gainPowerProduct = (SNRmin * (4 * (math.pi))**3 * maxSlantDistance**4 * boltzmannsConstant * standardTemp * noiseFigure * bandwidth)/(Lambda**2 * minRCS * numPulses)

arrayGain = 12656.7
# arrayGain = 15430

maxPowerRequired = gainPowerProduct / ((arrayGain)**2)
print("Maximum Power Requires: " + str(maxPowerRequired/1000000) + " MW")


dutyCycle = pulseWidth * maxRoundTripTime
averagePower = dutyCycle * maxPowerRequired
print("Average Power Required: " + str(averagePower) + " MW")

averagePowerPerElement = averagePower/numElements
maxPowerPerElement = maxPowerRequired/numElements

print("Average Power Per Element: " + str(averagePowerPerElement) + "W")
print("Maximum Power Per Element: " + str(maxPowerPerElement) + "W")


# Element Separation without Grating Lobes (assuming 30 degrees steering)
maxElementSpacing = (Lambda)/(1 + numpy.absolute(math.sin(maxAngle)))
print(maxElementSpacing)