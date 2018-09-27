import math

c = 3 * 10**8
minDistance = 160 * 10**3
maxDistance = 2000 * 10**3

minRoundTripTime = 2 * (minDistance/c)
maxRoundTripTime = 2 * (maxDistance/c)

# Minimum radar cross section of object
minRCS = 1 * 10**-3


powerReceived = (powerTransmitted * arrayGain * effectiveAperture * minRCS) / (16 * (math.pi)**2 * maxDistance**4)


