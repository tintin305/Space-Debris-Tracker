---
title: Design Project Notes
---

# Brief

## Title: Antenna Array Design to map man made space "junk" in low earth orbit

With the increase in space travel, it is becoming more and more important to know where potentially fatal problems may arise due to man made space junk/debris.
The man made space junk is made of small objects travelling at high velocity, (usually metalic). This occurs due to bits and pieces breaking off from satellites, rockets, space stations, intentional satellite destruction by missiles etc.
This was highlighted in the movie “Gravity”
Startup companies such as LEOLABS (www.leolabs.space) have begun to address this problem.
Students will be required to do a theoretical design similar to LEOLABS phased array radars in order to track space debris, including the operational environment and costing of the system.
FEKO will be made available to the students in the DLAB to run simulations.
A visit factory visit to Alaris antennas will be organised to ask questions of engineers in industry. (week 3 or 4)



# Extra Notes

What if it can be placed in the sea?

The altitude that an ICBM reaches is in the order of [150 to 400 km](https://en.wikipedia.org/wiki/Intercontinental_ballistic_missile). This is part of the LEO to the GEO and so these can also be identified by this system.
The US has [created such an antenna array](https://www.airspacemag.com/how-things-work/how-things-work-phased-array-radar-10766910/) (floating), that can detect these missiles. It makes use of a phased array system.


# LEOLABS

On the LEOLABS site, they make use of phased array radars in order to track the space debris. This does not provide much information. The next piece of information that they provide is that of the company which designed and constructed the antenna array (SRI).
Based on an [article](https://www.dailymail.co.uk/sciencetech/article-4267014/Firm-raises-4-million-build-space-junk-radar-tracker.html), they say that the company created a site in Alaske that uses Advanced Modular Incoherent Scatter Radar (AMISR). Which is a "modular, transportable radar system which can observe small-scale and temporary phenomena. 
The system was originally designed to observe phenomena like the aurora and space weather storms. 


# Space Debris

Commonly, space craft make use of [Whipple shields](https://en.wikipedia.org/wiki/Whipple_shield) to shield craft from some of the objects in space.

The runaway chain reaction of the space debris is known as a [Kessler syndrome](https://en.wikipedia.org/wiki/Kessler_syndrome). 

The [Space Debris](https://en.wikipedia.org/wiki/Space_debris) wiki contains a lot of information relating to the detection of this space junk.

The maximum speed of objects that have currently been detected: [16 km/s](https://en.wikipedia.org/wiki/Space_debris). [Other site](https://www.nasa.gov/mission_pages/station/news/orbital_debris.html)

# AMISR

The current [website](http://amisr.com/amisr/about/amisr-overview/) holds a wealth of information on the one antenna used by LEOLABS. It appears that there are actually three different "faces" of the AMISR: "the first AMISR face was deployed in Poker Flat, Alaske in 2006 (the Poker Flas IST, or PFISR), and the remaining two faces were deployed in Resolute Bay, Nunavut, Canada (RISR-N and RISR-C). 
The [National Science Foundation](https://www.nsf.gov) in collaboration with SRI International undertook the construction and design of the system. 

## System Description

The AMISR [site](http://amisr.com/amisr/about/amisr-overview/amisr-system-description/) contains useful info for how the system is constructed:

   SRI International designed and constructed, and now operates and manages, the Poker Flat and Resolute Bay Advanced Modular Incoherent Scatter Radar (AMISR) facilities. The AMISR has significant advantages over other ISRs in operation, because of the pulse-to-pulse steering provided by the phased array antenna. This rapid steering capability allows scientists to resolve temporal/spatial ambiguities inherent in measurements from mechanically steered dish-based systems. An additional important feature enabled by the AMISR is that the facility can be readily relocated to new regions of scientific interest, resulting in much greater overall utility of the system. Major portions of the AMISR can, in fact, be separately located to provide broad geographic coverage. Many of the scientific issues addressable by the innovative AMISR design were articulated in the Re-locatable Atmospheric Observatory 7–8 April 1999, Workshop Report [NSF, 1999].

    Knowledge of the Earth’s upper atmosphere, ionosphere, and geospace environment advanced significantly during the second half of the twentieth century. A wealth of information was garnered from in situ probes and various remote-sensing techniques in combination with the development of models of the environment, both from first principles and via heuristic approaches. A detailed understanding of even the most basic processes remains somewhat vague, however, because such an understanding must encompass the strongly coupled systems of the Earth’s upper atmosphere, ionosphere, magnetosphere, and the solar wind. At various times and locations, important temporal scales can range from seconds to days, seasons, or even an entire solar cycle. Similarly, the relevant spatial scales range from sub-meters to thousands of kilometers. Thus, while substantial progress has been made, there remain significant gaps in our understanding of the system as a whole.

    One of the most powerful remote-sensing instruments available today for probing the ionospheric plasma is the incoherent scatter radar. ISRs measure many of the parameters needed to describe the state and energy balance of this plasma (e.g., electron number density, electron and ion temperatures, bulk ion motion, ion masses, ion-neutral collision frequency). Furthermore, they do this in a spatially resolved sense over regions extending hundreds of kilometers in the hemisphere centered on the radar, and can measure the variations in the ionospheric state continuously over timescales from hours to days, with time resolutions as short as a few seconds for one altitude profile, or a few minutes for measurements versus altitude and ground distance from the ISR.

    The AMISR concept entails the use of a large number of identical electronic subsystems, which yields a high degree of redundancy and a robust response to hardware failures. The systems as a whole have proven to be exceptionally reliable, as evidenced by the nearly continuous PFISR coverage since it began normal operations in 2007. The high-level of redundancy in an AMISR system is in so small part responsible for AMISR’s amenability to largely unattended remote operations. AMISR is the only system in the world with similar capabilities that can be operated with so little on-site staffing.

    ![](amisrbuildup.png)

    The AMISR systems are highly modular. The various subsystems operate synchronously via a combination of Ethernet/software constructs and specialized hardware signaling. The figure above shows the components that go into an AMISR system.

    The basic element of an AMISR system is the radar front-end Tx/Rx module, called an Antenna Element Unit (AEU).  The AEU includees a 500-Watt solid state power amplifier (SSPA), designed and manufactured by SRI International, as well as a cross dipole antenna. The design of the AEU is conducive to plug-and-play upgrades.  Each AEU consists of low-level RF circuitry for phase control on transmit and receive, a low noise amplifier that sets the overall system receive sensitivity, a Solid State Power Amplifier (SSPA) to generate the transmitter RF, a power supply, and digital control and communications electronics.
    32 AEUs are arranged on an AMISR panel that contains a Panel Control Unit (PCU) for AEU control and monitoring.  The PCUs each include a fully programmable computer running Linux so that the functionality of the array can be adjusted and upgraded over time. On a standard AMISR face, 128 identical AMISR panels are nominally arranged in a densely-packed and roughly square configuration.
    The prime power for the radar, on the other hand, is routed through two Utility Distribution Unit (UDU) vans. The radar runs off of aircraft-standard 400 Hz power, which is generated by eight JetPower units with four in each UDU van.  Each JetPower unit powers 16 panels.
    The overall control of the system is driven from an Operation and Control Center (OCC) that houses general-purpose computers as well as low-level RF signal conditioning modules. Physically, the OCC is an environmentally controlled shelter or building available for operator interaction with the system, though most interactions in fact occur over the internet whether the operator is in the OCC or not. The OCC also houses all of the data acquisition channels, and contains the source for the transmitted waveforms and (at PFISR) RF receive signals from 16 equally sized portions of the array (representing a 4x4 grid).



A number of other companies supported the project: Sanmina-SCI (manufactured the antenna element units(the basic building blocks of the radar panels)). Information found from [here](https://www.sri.com/newsroom/press-releases/sri-international-announces-findings-new-upper-atmospheric-radar-system-buil). 

VECO Alaska Inc. oversees the design and structural engineering of the radar, including the panels and support scaffolding
MIT Millstone Hill is a co-investigator on the project.
Universities involved: MIT Millstone Hill, Standord University, University of Alaska, University of Western Ontario.


# Explanation of ISR

https://www.haystack.mit.edu/atm/mho/instruments/isr/isTutorial.html

Commonly, these systems are used to measure characteristics of the ionosphere which ranges from approximately 100 km through to 1000 km, this is perfect for detecting the space junk which lies within this region.

# Detecting Space Debris with Antenna Arrays (a Google)

It was important to google this exact thing to have a look at other alternatives, even though the brief asked for a solution similar to what Leolabs uses. 



# Meeting with Derek

Radiation after the big bang (4 Kelvin). 
Noise floor. 

Specify a minimum size of objects: approx 10 cm (RCS (radio cross section))

Choose a receiver sensitivity: randomly: -120 dBm

The gain of the system needs to be determined as well as the transmitting power as you are required to receive at least -120 dBm of power back from an object of 10 cm

How narrow must your beam be in order to pick out individual elements floating around (this is a resolution issue)

Trade off between power and gain

Specify a frequency this can be because of monetary reasons as well as physical reasons.

Building an amp is a big mission. Lower frequency amps are easier to design/purchase.

Broadcast dipoles and how to make low VSWR versions

Degradation in the gain as you swing your major direction

Where will all of the side lobes go!?!?!? Will they affect other systems? Will they affect the readings and pick up objects that you dnot want?

Using the binomial you will reduce your sidelobes however you will reduce your overall gain.

What kind of beam sweep will you be looking for?

When it hits the object it will change polarization. We must check how many times if flips polarization and how it does this.

Maximum ratio combining (to do with the polarization things) This must be thought of, in how you combine these signals together. 

You need to provide time for "switches" to work, this is to give "dead time" for the system to set itself up.

How do you swap between the receiver and the transmitter.
This may be a case where a "[circulator](https://en.wikipedia.org/wiki/Circulator)" can be used.

Wilkinson splitter (for feeding the antenna)

The feeding network is different to how the antenna is connected together (Wilkinson splitter)

Hartebeespoort visit.

Where is the processing done? SHould the data be transmitted elsewhere and then processed? Then you won't need a server farm in the karoo and you can use the cloud.


Corporate feed

Determine the power that is present in the side lobes. 
I do not believe that it is worth using a binomial array, even though it reduces the side lobes, you still have to consider how the power system is structured. How do you distribute the amplifiers? Do you then have a case where you have a multitude of differently sized amplifiers in order to reduce the cost? 

# Costing

Derek recommends going to see the Hartebeespoort array to ask about costings and stuff like that. 
He also recommends [this](https://www.minicircuits.com) site.
The other thing would be to ask Alaris folks about this and get quotes from Poynting.

In the Design document, they structure each element with a description, then they provide advantages and disadvantages followed by a cost estimate.





# Design (Paper)



# Optimal Frequency

[This](http://www.met.nps.edu/~psguest/EMEO_online/module3/module_3_2b.html) seems useful

When determining the frequency, specify an opimal frequency, then provide optional operational frequency ranges (if possible). A discussion on how well the components work at these other frequencies and how the ionosphere handles these other frequencies, as well as the frequency bands that are available.
Speak about how the returned frequency will be different than the transmitted.

In choosing the frequency, it is highly advantageous to decide on a frequency where there is a decent amount of experience in the design and operation as well as it should be easy to find and purchase "off the shelf components". This implies that the frequency should lie near the EISCAT frequencies (224 and 931 MHz) or lie in the 400-500 MHz band which has been used by other incoherent scatter radars.

Higher frequency choices:

    * Lower system noise, this is highly dependent on the temperature above the site, these temperatures are different at different frequencies.
    * Smaller antenna size for a given beamwidth, apparently this makes it easier to achieve full steerability and a high scanning rate
    * Less clutter form coherent echoes which are mainly due to field-aligned irregulatities. The strength of these echoes will be about 12 times stronger at 430 MHz than at 931 MHz, and about 50 times stronger at 224 MHz.

Lower Frequency choices:

    * Smaller Debye ratio for a given electron concentraion so that measurements can be extended to greater heights
    * Greater cross-section for MST work

One final factor points to an intermediate frequency:

    * At higher frequencies the bandwidth of the scattered signal is greater. This widens the bandwidth over which noise is received and if the system noise temperature is approximately constant (i.e. for frequencies > 400 MHz) this increases the total noise power in proportion. However, with a broader bandwidth the maximum lag which must be measured in the autocorrelation function is reduced. This allows the envelope of the transmitted signal to be shorter and hence allows observations to begin at shorter range.

When using lower frequencies, the system noise limits the sensitivity massively, this also makes a narrow beamwidth which limits the E region (especially for observations near the zenith)

Another factor that affects the frequency band choice is that available by the systems regulator. A [document](https://www.icasa.org.za/uploads/files/ITU-Reference-Review-the-Radio-Frequency-Band-Plan-31264.pdf) provides the info for these bands.

ISM band (freely available, however everyone also is allowed to use it)

## Getting through the ionosphere

Info from [here](http://www.met.nps.edu/~psguest/EMEO_online/module3/module_3_2b.html)

There are limits to the frequencies that can be transmitted through the atmosphere+ionosphere. Below 5 MHz the radio waves are not transmitted because they are reflected by the ionosphere; above 30 GHz, the electromagnetic waves are absorbed by water vapour and carbon dioxide in the atmosphere.
[This](http://www.sws.bom.gov.au/Category/Educational/Other%20Topics/Radio%20Communication/Intro%20to%20HF%20Radio.pdf) document goes through a number of calculations and information providing about the ionosphere and how the different frequencies are affected by it.
Speak about critical frequencies.
Docs: http://www.rfwireless-world.com/Terminology/Critical-Frequency-and-Maximum-Usable-Frequency.html
http://www.sws.bom.gov.au/Category/Educational/Other%20Topics/Radio%20Communication/Intro%20to%20HF%20Radio.pdf
https://radiojove.gsfc.nasa.gov/education/educ/radio/tran-rec/exerc/iono.htm

# Environmental Considerations

## Weather Dependence

Maximum and minimum temperatures. Average temperatures, temperature swings and their gradients. 
Wind.
Fog
Sun angles

Light intensities

Air quality
Humidity
Icing of instruments
Snow


Light polution



## Land

The lay of the land
Mountains?
Flat land?
How difficult will it be to lay foundations
Shipping material
Construction side of things
Altitude? Height above sea level?
Nearby roads?
Quality of these roads? Will they need upgrading? 
Power distribution? 
Communications?
Water?
Sewage?
Disturbances of power lines and transformers to the system?
Frequency of the power?

Nearby electromagnetic interference? 

Possible impact from telecommunication in the area. Do radio links exist? 
One must look at the sidelobes and the distribution of power in the various harmonics

Air traffic interference?
Airports? planes overhead?
Mostly planes? Helicopters? They pose different interferences as they fly at different altitudes and use different communication systems.

In the design paper, they say that helicopters frequent the area, however, on days of good visibility they fly low and follow the valleys where they will be shielded against the radar beam.

It may be worth installing a separate small surveillance radar that is capable of detecting aircraft and then switch off the main radar (depending on the situation)

Is it worth contacting the air ports and the control towers for some of this? Get real time tracking of planes?

Beacons in the area?

Displacement of plants and animals?

Elevation of the horizon? Does it change in different directions? Does this affect the system?

# Orbits

Orbits: use [this](https://www.iadc-online.org/Documents/IADC-2012-06,%20IADC%20Annual%20Report%20for%202011.pdf) to define some info about the orbits.

# Modelling the Debris

The specification needs to be able to determine if there are multiple objects in the view, or are you going to bundle them together. This has to do with the resolution of the system.

There are a number of equations that allow for exact modelling of the space debris. This has to do with the electron density, ion composition, electron drift velocity, and a number of other parameters which allows for in depth analysis of space debris. However, in order to simplify the calculation, a number of simplifying assumptions are made about the space debris. There are hard and soft radar target, and they each react differently to the electromagnetic wave they they encounter. This assumes that the target is a solid piece of matter (eg. your standard space debris that is assumed to be in the ionosphere). The soft radar targets are not covered in this paper as this is commonly highly distrubuted material which is distinctly more diffiult to determine and falls out of scope of this project.

Once the debris has been modelled, one can make use of the radar equations in order to determine a number of required parameters:

P_{inc} = P_t * \frac{G_{t}}{4 * pi * R^2} [W/m^2] - Power incident on the target

P_{scat} = P_{inc} * sigma_{radar cross section} [W] - scattered power

P_{rec} = P_{scat} * \frac{A_{eff}}{4 * pi * R^2} [W] - Received power

P_{rec} = \frac{P_t * G_{t} * A_{eff} * sigma_{radar cross section}}{16 * pi^2 * R^4} [W] - radar equation

A_{eff} = \frac{lambda^2 * G}{4 * pi}

It is important to note that the minimum detectable power/signal should be defined, here it is denoted by S. When the received power is equal to this value, it is possible to define this range as the maximum range that can be detected. This is defined as R_{max}

Manipulating the P_{rec} equation above and combining the S parameter allows for the following equation to be defined:

R_{max}^4 = \frac{(P_t * A_{eff} * G_t * sigma_{radio cross section}}{(4 * pi)^2} * 1/S

Based on this equation, the peak power of the system, as well as the antenna aperture affect the range at which the system can detect objects. This implies that if the detecting range is required to be increased, then one or both of the parameters should be increased.

The size of these objects should be defined and the reasoning behind this decision originates from a number of sources. 
Firstly, the Whipple shield is deployed on satellites and space craft, this shield is used to protect the systems and crew from collision of the space debris, as well as micrometroroids.
Use [this](https://www.iadc-online.org/Documents/IADC-2012-06,%20IADC%20Annual%20Report%20for%202011.pdf) site to provide some explanation on the choice of the debris size. 

The equations determined thus far do not consider a number of other characteristics and this forms a rough calculation of the systems performance at a specified range. A number of the parameters in these equations are still unknown and are required to be determined.
The range in the above equation is optimistic as it does not include the losses within the radar, and it also does not consider the fact that the objects' cross section and minimum detectable signal are statistical variables.

The S parameter defined in the above equation is defined as the minimum detectable signal; it is important to note that this is a statistical quantity that means that it has the ability to provide a false alarm. 
In order to deal with this characteristic, it is assumed that in order to reliably detect a signal, it must be at least greater than noise (usually 10 - 20 dB) on the receivers side.
This minimum signal magnitude is expressed as a signal-to-noise ratio (S/N) required for reliable detection times the receiver noise.
SNR * Noise_{receiver} = S_{min}

The noise of the receiver is defined to be relative to the thermal noise produced by an idea receiver
The thermal noise is equal to kTB
The receiver noise is the thermal noise multiplied by the factor F_n, the receiver noise figure.
The receiver noise figure is measured relative to a reference temperature T_0 = 290 K (approx room temp), and the factor kT_0 becomes 4 * 1-^-21 W/Hz. 

S_{min} = kT_0 * B * F_n * \frac{S}{N}

The facto rT_0 F_n can be replaced with T_s, the system noise temperature.


# Antenna

The radar equation forms the initial stage for the design process.



# Array Structure

Create each antenna element independently, talk about IoT and how each element can be connected so that large feeding networks are not required.

Beamwidth
Gain (main lobe)
Sidelobes (near)
Sidelobes (far)

Beam directions

Noise temperature

Bandwidth (-1.5 dB): transmit and receive

Polarization:
    accuracy: < ? dB 
    transmit:
    receive: 

VSWR: 
    transmit:
    receive:

Power capability:
    peak:
    average:
    pulse lengths:

Highest operating frequency in receive mode

Antenna mechanical specifications

Feed system:
    elements:

Foc.len./diam:

Diameter of array (m):

Slewing velocity (deg/s):

Slewing range (deg):
    elevation:
    azimuth:

Surface accuracy (cm_(rms)):

Pointint/tracking accuracy (deg):

Windspeed (km/h):
    operational:
    survival:

Temperature (deg C):
    operational:
    survival:

Rotary joints:

Equipment on azimuth platform:
    weight (kg):
    volume (m^3):

Icing: 

Transmitter:
    Frequency:
        operation:
        optional:

        bandwidth (-1.5 dB)

    Transmitter modules: 

    Total Power:
        peak:
        average
        pulse length:

    interpulse period:

    VSWR:

    Duplexer:
        isolation:
        recovery:
        insertion loss:

        Operation:

Receiver:

    Input bandwidth:
    Baseband-width:

    Noise temperature:

    Dynamic range:

    Higher order inter modulation products:

    Phase noise of oscillators (incl. transmitter exciter with respect to the carrier frequency)

## Simple Array Explanation

A phased array is a group of antennas whose effective (summed) radiation pattern can be altered by phasing the signals of the individual elements.

By varying the phasing of the different elements, the radiation pattern can be modified to be maximized/suppressed in given directions, within limits determined by:
    * the radiation pattern of the elements
    * the size of the array, and
    * the configuration of the array

# Why ISR?

According to the theory of incoherent scattering first presented by Gordon in 1958 ([Incoherent Scattering of Radio Waves by Free Electrons with Applications to Space Exploration by Radar](https://ieeexplore.ieee.org/document/4065300)).
ISR is the only equipment which has such ability. The measured area can be covered from 60 to 2000 km, and ISR has become the most powerful ground-based tool currently for the study of ionospheric structures and kinetic processes[ref](https://agupubs.onlinelibrary.wiley.com/doi/epdf/10.1029/2007JA012250)

The system is capable of measuring space debris ([Space Debris Measurements using the Advanced Modular Incoherent Scatter Radar](https://amostech.com/TechnicalPapers/2015/Poster/Nicolls.pdf))


# Electronics

RoHS standards
lead free components