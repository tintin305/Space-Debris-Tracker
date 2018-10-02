# Observable time or Dwell Time

import math

minDistance = 160 * 10**3
maxDistance = 2000 * 10**3

# Tangential velocity
maxObjectSpeed = 7.795 * 10**3



angle = 1 * (math.pi / 180)

minArcDistance = minDistance * angle
maxArcDistance = maxDistance * angle

minObjectObservableTime = minArcDistance / maxObjectSpeed
maxObjectObservableTime = maxArcDistance / maxObjectSpeed

# Max doppler shift