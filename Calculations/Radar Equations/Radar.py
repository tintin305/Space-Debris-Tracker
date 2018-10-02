import math

c = 3 * 10**8
minDistance = 160 * 10**3
maxDistance = 2000 * 10**3

minRoundTripTime = 2 * (minDistance/c)
maxRoundTripTime = 2 * (maxDistance/c)

# Minimum radar cross section of object (min diameter of 10 cm)
minObjectRadius = 10 * 10**-2

minRCS = math.pi * minObjectRadius**2

kB = 1.38064852e-23


# Atmospheric Loss

# receiverTemp = 10
# antennaTemp = 10
# sysTemp = receiverTemp + antennaTemp
# bandwidth = 10

# noiseFloor = kB * sysTemp * bandwidth

# powerReceived = (powerTransmitted * arrayGain * effectiveAperture * minRCS) / (16 * (math.pi)**2 * maxDistance**4)


# SNR = powerReceived - noiseFloor