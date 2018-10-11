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

## Debris Speed

Max speed of objects in orbits are determined by their altitude and this means that their speeds are defined by those orbits. Each orbit has a specified period. Equations and notes can be found [here](https://www.quora.com/How-fast-does-an-object-move-in-outer-space), and [here](https://www.quora.com/How-fast-at-the-maximum-speed-can-you-orbit-in-LEO). 


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

Apply some form of taper for the amplitude over the area of the array.
In order to reduce the sidelobes, you must find a happy medium between gaussian distribution and a standard distribution.

Determine an acceptable dB level for the biggest sidelobes. Check for the power in the lobes and their direction (if they are pointing in dangerous areas or not). Another way to specify the first sidelobe level is to assume a maximum object size at the lowest altitude and then determine the gain for this sidelobe at which the signal is below acceptable levels.

Think about build up of static electricity within the system and consider how to protect circuitry from this (the receiver is commonly the most sensitive device)

It may make sense to apply a modulation to the signal as this can tell you if it is indeed your signal which you are detecting.


# Costing

Derek recommends going to see the Hartebeespoort array to ask about costings and stuff like that. 
He also recommends [this](https://www.minicircuits.com) site.
The other thing would be to ask Alaris folks about this and get quotes from Poynting.

In the Design document, they structure each element with a description, then they provide advantages and disadvantages followed by a cost estimate.



# Introduction

It will be pertinent to reference [this](https://www.reddit.com/r/space/comments/9h57ui/removedebris_satellite_performs_worlds_first/)

## System

The system can be illustrated with the use of the design slides. This illustrates the entirety of the system.
The elements which make up the system include:

    * Transmitter
    * T/R Device
    * Antenna
    * Receiver
    * Signal Processor

Each of these items will have their own section.
However, there will be sections which discuss other components/characteristics of the system.

Section on EM waves and how they are created, influenced, propagated, polarized, phase shifted, their spectrums, superpositioned, 
Introduce the simple kinds of polarization and then reference later parts in the report that the waves will be affected by the structure of the antenna and the array as well as the atmosphere.

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

It will be useful to take some info from [here](https://elib.dlr.de/110661/1/Initial%20Detection%20and%20Tracking%20of%20Objects%20in%20Low%20Earth%20Orbit.pdf), on page 9 and before it talks about the right frequency windows that allow for transmission of EM waves.

Info from [here](http://www.met.nps.edu/~psguest/EMEO_online/module3/module_3_2b.html)

There are limits to the frequencies that can be transmitted through the atmosphere+ionosphere. Below 5 MHz the radio waves are not transmitted because they are reflected by the ionosphere; above 30 GHz, the electromagnetic waves are absorbed by water vapour and carbon dioxide in the atmosphere.
[This](http://www.sws.bom.gov.au/Category/Educational/Other%20Topics/Radio%20Communication/Intro%20to%20HF%20Radio.pdf) document goes through a number of calculations and information providing about the ionosphere and how the different frequencies are affected by it.
Speak about critical frequencies.
Docs: http://www.rfwireless-world.com/Terminology/Critical-Frequency-and-Maximum-Usable-Frequency.html
http://www.sws.bom.gov.au/Category/Educational/Other%20Topics/Radio%20Communication/Intro%20to%20HF%20Radio.pdf
https://radiojove.gsfc.nasa.gov/education/educ/radio/tran-rec/exerc/iono.htm

Lower frequencies (< 1GHz) result in reduced atmospheric losses, this is a major reason to choose this. Based on the textbook (Mark A. Richards, James A. Scheer, William A. Holm - Principles of Modern Radar_ Basic Principles, page 124, and 15), it is apparent that frequencies below the 1 GHz mark will have less than 10^-2 dB of attenuation per kilometer.

It is also stated that attenuation will decrease with an increasing elevation angle, and can also be neglected when the angle of elevation exceeds 10 degrees (textbook: Radar Essentials: A concise handbook for Radar Design and Performance Analysis G. Richard Curry, https://m.eet.com/media/1121840/912radar_essentials_pt1.pdf). 
The book also has some useful graphs which indicate the two way attenuation for 425 MHz at differing angles.
At the 10 degrees line, the two way attenuation does not exceed 0.25 dB depending on the range.

## ICASA

It appears as if the last frequency allocation happened in 2013.
The next one is up for approval and is in draft stage. There are a number of bands which appear to be moving and this can affect things.

[Thils](https://www.icasa.org.za/legislation-and-regulations/national-radio-frequency-plan-2013) appears to contain the 2013 allocation.

Frequency allocation by [SKA](https://www.ska.ac.za/about/astronomy-geographic-advantage-act/)

The chosen frequency at this point is: 610 MHz.
The frequency on either side of the band is 4 MHz.
Wavelength: 0.4918 m
3/4 wavelength: 0.3689 m
1/2 wavelength: 0.2459 m
1/4 wavelength: 0.12295 m

## Astronomy Geographic Advantage Act

The minister has the ability to declare any area or part of an area in the Province of the Northern Cape as an astronomy advantage area. This implies that an area, which is technically advantagous to the functioning of the system can be demarkated by this act.
A number of proccesses are required to take place for these areas to be allocated to the system. These include a number of considerations for: local businesses, affected agricultural participants, environmental impacts, nearby electrical and radio interference.

The act allows for specific frequencies to be used (regardless of the current frequency allocation by ICASA) as long as it is assessed by the procedures required by the SKA. Permits can be issued by the act and they are then allowed to operate within the permitted areas. These permits include exemptions for the frequency spectrum that is allowed to be used and the permitted transmission characteristics.

The current situation with ICASA is such that there is a 50 mW maximum allowable broadcast power. However, with the use of the AGA, the TV transmission services are limited in the Northern Cape.

The band chosen is currently allocated ot the radion astronomy service on a primary basis.


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

[This](https://www.icasa.org.za/legislation-and-regulations/protection-of-karoo-central-astronomy-advantage-areas-regulations-2017) will be useful for talking about how the area will be protected.
Land can be given by the [SKA](https://www.ska.ac.za/about/astronomy-geographic-advantage-act/). One can argue that the system will not be used all the time, as such, the SKA may be able to make use of the system for research purposes.
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

Lightning?

Nearby electromagnetic interference?
Can this interference be removed? Must it be quantified and then subtracted from the overall signal? Is this sufficient?

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


# Construction

How things fit together, how the cables are placed
What kind of cables
What communications medium is used between modules


# Orbits

Orbits: use [this](https://www.iadc-online.org/Documents/IADC-2012-06,%20IADC%20Annual%20Report%20for%202011.pdf) to define some info about the orbits.

# Modelling the Debris

The specification needs to be able to determine if there are multiple objects in the view, or are you going to bundle them together. This has to do with the resolution of the system.

There are a number of equations that allow for exact modelling of the space debris. This has to do with the electron density, ion composition, electron drift velocity, and a number of other parameters which allows for in depth analysis of space debris. However, in order to simplify the calculation, a number of simplifying assumptions are made about the space debris. There are hard and soft radar target, and they each react differently to the electromagnetic wave they they encounter. This assumes that the target is a solid piece of matter (eg. your standard space debris that is assumed to be in the ionosphere). The soft radar targets are not covered in this paper as this is commonly highly distrubuted material which is distinctly more diffiult to determine and falls out of scope of this project.

Once the debris has been modelled, one can make use of the radar equations in order to determine a number of required parameters, these are found in section ***

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

The factor T_0 F_n can be replaced with T_s, the system noise temperature.

## Space debris distribution

[Lots](https://elib.dlr.de/110661/1/Initial%20Detection%20and%20Tracking%20of%20Objects%20in%20Low%20Earth%20Orbit.pdf) of info on space debris and how it is defined

## Debris Speeds

Objects in LEO normally have angular velocities of at least 0.5 degrees per second when viewed from the ground.[This](http://www.castor2.ca/08_Papers/Zenith_Ranging.pdf) shows the entire calculation for how the objects speed changes depending on altitude and how it is observed from the ground

Lower altitude objects exceed angular speeds of 1 degree per second relative to the ground observer, when it is viewed at high elevation angles (close to 90 degrees). However, when viewed at around 30 degrees elevation, the speed is observed to be around 0.25 degrees per second.

Figure 7 in [this](http://www.dtic.mil/dtic/tr/fulltext/u2/a531931.pdf) indicates how the angle of the object changes when it is viewed from different elevations. Fig 10 shows how the "detectability" increases with increasing elevation angle.

# Antenna

The radar equation forms the initial stage for the design process.

Primary functions:

    * Impedance transformation (free-space fields to guided waves)
    * Propagation-mode adapter (free-space to guided waves)
    * Spatial filter (radiation pattern - direction-dependent sensitivity)
    * Polariation filter (polarization-dependent sensitivity)

The antenna is used to fix the mismatch between free-space and the rest of the system.
Intrinsic impedance of free-space: n_0 = E/H
n_0 = sqrt(u_0 / e_0) = 120 * pi ~= 376.7 omega

Characteristic impedance of tx line, Z_0 = V/I (typically 50 omega)

## Polarization

Make use of [this](https://etd.ohiolink.edu/!etd.send_file?accession=ohiou1345227397&disposition=inline) to speak about the axial ratio and how polarization is done.

# Array Structure

## Monostatic versus Bistatic

There are two major radar configurations that are used. 

### Bistatic

The bistatic configuration makes use of a separate transmitter and receiver for the system. The two components are placed at differing locations and the separation between the components is required to be sufficiently large in terms of the angles or ranges that they present.
This implies that the two systems, in the case of Earth-to-Space transmission, are required to be geographically (in the order of kilometers) far apart \cite{bistaticNato}.
The transmitters in these systems generally transmit power in the range of kilowatts to megawatts, this is in order to increase the signal-to-noise (SNR) of the system as there is a significant amount of energy lost in the energy transfer process. The receiver on the other hand, works with milliwatts to nanowatts as it receives this greatly reduced power that is reflected from the objects in question. The bistatic system provides a concenient method of separating out the two systems such that it becomes increasingly difficult to damage the receivers equipment from the high power generated by the transmitter.

### Monostatic

The other, more commonly used system, is the monostatic configuration. This bundles the transmitter and receiver together on the same antenna/antenna array. In this case, a system is required such that the transmitted and received signals are isolated from eachother when they interact with the system. The isolation can be carried out in different ways, a circulator or a switch commonly achieves this. These components are discussed in a later section ***. In the monostatic configuration, the transmitter and receiver do not operate at the same time which greatly simplifies the switching apparatus.

### Comparison

The configuration implemented is the monostatic as it provides a lower cost alternative to the bistatic configuration. It has the added benefit of only requiring one piece of land for the system. The system cost is also reduced by the fact that only one set of antennas are required.
The bistatic configuration is easier to implement with regards to the protection systems for the receiver, however, this benefit does not out weigh the monostatic systems advantages. The bistatic systems also require a significant amount of communication between the two systems and this can increase the cost of implementation, most notably when the distance between the two systems is large and communication mediums can become prohibitively expensive.

## Continuous Wave and Pulsed Wave

The two commonly used transmission systems are the continuous wave and the pulsed wave, these two systems are also linked to the choice on the system configuration.
This implies that if the monostatic configuration is used, then the continuous wave transmission system is not available.

### Continuous Wave Transmission

The continuous wave transmission system, as the name indicates, has the transmitter functioning $100\%$ of the time, which implies that the receiver also functions all of the time. The continuous wave transmission system, as indicated above can only be used by the bistatic configuration. 
A unique characteristic of the continuous wave system is that it is unable to determine the electromagnetic (EM) waves round-trip time as there is no set begin and end time of transmission. This can be solved with the use of modulation on the wave, this implies that the receiver is required to know all of the characteristics of the transmitters waveforms ahead of time if it is to determine round trip times \cite[p.~20]{radarHandbook}.

### Pulsed Waveform Transmission

The second mehtod of EM wave transmission makes use of pulses, these occur periodically and their duration is commonly over a short period of time. This system is commonly used in tandem with a monostatic configuration and this provides the isolation between the transmitter and receiver circuitry, the circuitry to isolate these signals is still used.
Following the EM wave pulse, the receiver is set to record the resulting EM waves that are returned in the form of echoes after it has reflected from the objects in question. The determination of the pulse length and the period between pulses (the interpulse period (IPP))is discussed further in the report ***. The pulse repitition is also highly pertinent to the observable time window of debris, this will be discussed in section ***.

Need image here which describes how the pulses are placed with respect to time.

The pulse repetition frequency is related to the maximum distance that the system is able to detect objects, this is related to the observable area of the system and the furthest distance that the system can detect an object. This is discussed in section *** and section ***.

The following image represents a case where a pulse is sent outwards and is then followed by, a period of time later, a corresponding echo pulse.
The period between the pulse and the echo can be used to determine the altitude that the object has.
In order to detect the pulse, the time between each sample should be no less than the pulse width of the transmitter (this should be elaborated on... get the info from: \cite[p.~21]{radarHandbook})

Think about echoes that come back after the next pulse is fired, this can be from targets that are past the 2000 km range. These need to be dealt with. One way is to define a SNR that will rule out these cases. Another case is to throw out any echoes that happen before one is expected to have returned (based on the minimum altitude required to be detected). 
This issue is known as a range ambituite (\cite[p~.22]{radarHandbook})

*** Include calculation of the pulse width and the corresponding bandwidth if requires. Stuffies for this can be found on page 65

## Threshold Detection

In order to detect a signal, the received signals' power is required to be above a specific threshold. This threshold is defined as the level at which all sources of noise are incorporated. When an object is detected, the signal level is required to rise above this threshold and this is then considered a successful detection.

There are cases, based on the fact that noise is inherently a random variable, that the noise level can exceed the threshold set by the system. This is observed as a false alarm.
This implies that there are cases where the targets echo in addition to the noise are capable of being below the threshold, this is when the noise in the system is low, so the addition of the echo is not large enough for the system to detect the object.
These two cases are highly unlikely, however, cannot be ignored as they are based on the probabilities of the entire system.

These probabilities are given as two variables: the probability of detection (P_{D}), and the probability of false alarm (P_{FA}). The probability of detection is the probability that an object-plus-noise exceeds the threshold applied to the system. The probability of false alarm is the probability that the noise (from all components of the system) will exceed the threshold.
The best case scenario for these two variables are: 
P_{D} = 1
and
P_{FA} = 0

These values are idealistic and so the correct threshold value is required to be set such that the system can operate as close to these values as possible.
When the threshold is increased the probability of false alarm will decrease, however, so will the probability of detection. When the threshold is decreased, the probabilities of both variables increase. A trade-off is required here to determine the optimum threshold level.

There is one way in which to increase the probability of detection while lowering the probability of false alarm, this is achieved by increasing the targets signal power (it should be noted that the signal power should be increased relative to the noise power). 
<!-- If the noise power increases in ratio with the overall power, then this will not work -->

The importance of Doppler should not be underestimated. Doppler shift is important as it can be used to reduce the effects of clutter in the viewing area, it is also able to perform measurements to detect if there is more than one object in the viewing area (in the same range). The removal of clutter from view of the system is achieved with Doppler by the fact that clutter is not moving and thus will have a no frequency shift.

## Resolution

The resolution of the system has three components: the ability to distinguish between objects that are different distances away from the system, have differing angles with respecto the the system, and have differing Doppler frequencies.

The first of these, the range resolution, determines if you are able to discren two objects that are in eachothers vacinity.
The range resolution is defined by:
\delta R = \frac{c \tau}{2}

This implies that if the pulse width of the signal is 1us, then the range resolution of the system is 150 m. This implies that if the pulse width is decreased, then the range resolution increases.
It must be noted that, if the pulse width is decreased, then the energy that is transmitted will decrease, and therefore it becomes increasingly difficult to detect an object.

<!-- The doppler resolution is determined by:
3 dB width = \frac{0.89}{dwell time} -->

## Radar Functions

### Search/Detect

### Track

### Image

# SNR

The resulting SNR of the calculation performed is the targets signal power divided by the sum of the noises in the system, this includes the receiver thermal noise and jammer noise.

The set of equations that are used to determine a number of these parameters are known as the radar range equations (RRE), these equations allow for the determination of the received power from the systems EM waves' reflections and also to determine the levels of the interfering power within the system, this allows for the calculation of the SNR.

This section begins with introducing the RRE and how it is applied to the system and how to determine the simplistic performance of the system. This first step estimates the performance of the systems power density at a distance R away. This is followed by estimating the thermal noise present in the receiver of the system, this then allows for the first estimate of the SNR. 

## Power Density

The first equation defines the power that is incident on the target, this is given by equation ***

P_{inc} = P_t * \frac{G_{t}}{4 * pi * R^2} [W/m^2]

Where:
P_{inc} is the power incident on the target
P_t is the power transmitted from the system
G_t is the gain of the system
R is the distance from the system to the target

This equation assumes the use of a directional antenna (not isotropic) which has a corresponding gain. This allows for the concentration of the beam in a specific direction.

The next stage is to determine the magnitude of energy that is reflected by the target, as assumed in section ***, the radar cross section of the target is defined and known. 
In depth analysis of the targets is provided in section ***.
Equation *** indicates the magnitude of power reflected by this object.

P_{refl} = \frac{P_{t} G_{t} \sigma}{4 pi R^2}

Where:
P_{refl} is the reflected power from the target
\sigma is the radar cross section (RCS) of the target measured in square meters (m^2)

This reflected power from the target is then received by the system and this is defined by equation ***

P_{r} = \frac{P_{t} G_{t} G_{r} \lambda^2 \sigma}{(4 pi )^3 R^4}

Where:
P_{r} is the received power at the system
A_{e} is the effective aperture of the system
\lambda is the wavelength of the system
G_{r} is the gain of the receive antenna

It is assumed that the gain is determined with equation ***.

G = \frac{4 pi n_{a} A}{\lambda^2} = \frac{4 pi A_{e}}{\lambda^2}

Where:
n_{a} is the efficiency of the antenna created (this is commonly between 0.5 and 0.8 \cite[p.~64]{radarHandbook})

In the case of the monostatic antenna array, the transmitting and receiving gain are the same as it is the same array. This implies that for bistatic systems, it is possible to have two different ranges for receiving and transmitting.


## Receiver Noise

### Thermal Noise

The noise from the environment is mostly made up by solar effects. This case deals specifically with the noise generated by the sun. This can contribute to large amounts of noise within the signal if the antenna array is pointed in the direction of the sun, however, great care should be taken to avoid pointing the antenna array directly at the sun. There will still be a small contribution of the suns noise from the sidelobes of the antenna array, however, this is greatly reduced.

The second source of noise, the largest component within the system, is that generated by the receiver electronics.
Thermal noise power, being uniform over the frequency spectrum contributes to the noise power over the bandwidth of the system. This implies that the thermal noise power is directly proportional to the receivers bandwidth. This power is determined with the use of equation ***.

P_{n} = k T_{s} B = k T_{0} F B

Where:
k is Boltzmann's constant (1.38 * 10^{-23} watt-sec/K)
T_{0} is the standard temperature (normally 290 K)
T_{s} is the system noise temperature (T_{s} = T{0} F)
B is the receivers bandwidth (Hz)
F is the noise figure of the receiver subsystem.

The noise figure defined here should be given in real amplitude (convert from dB as this is what it is usually specified in).
The bandwidth defined here is a calculated value and is dependent on two factors of the system.
The first of these can be defined with the use of the largest doppler frequency shift detectable by the system. This is defined in *** with the introduction of the debris' characteristics.
The second of these is defined by the minimum pulse width of the signal. This is calculated in section ***. 
This second case is highly important because if the bandwidth of the receiver is made smaller than the bandwidth required for the pulse width, then the power on the target will be reduced and this will cause inconsistencies and will reduce the range resolution of the system \cite[p.~65]{radarHandbook}. If the bandwidth of the receiver is created to be larger than the reciprocal of the pulse width, then the SNR of the system will decrease. This implies that the bandwidth of the receiver can occupy a small frequency band which is set by the pulse width. This implies that if the pulse width of the system is set to 1us, then the bandwidth of the system is 1 MHz.
The approximation of using 1/\tau is often used in monostatic systems \cite[p.~65]{radarHandbook}.

## SNR and the RRE

At this point it is possible to evaluate the SNR of the system with the use of the noise figure that is attained above.
The SNR is defined by equation ***.

SNR = \frac{P_{t} G_{t} G_{r} \lambda^2 \sigma}{(4 pi)^3 R^4 k T_0 F B}

This equation applies to discreet targets, which applies to this circumstance.

## Multi-Pulsing

Need to talk about how the SNR can be improved with the use of multiple pulses.

# Directions

Discuss how the system cannot determine the direction of the object, it can only determine if the object is moving towards the antenna's boresight or away (with an increased doppler freq or a decreased doppler freq)


## Standard Parameters

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

## Transmitting Technique

When using the bistatic system, with continuous wave (CW), it is possible to perform ranging of the object, however, the transmission signal must be modulated with pulse compression waveforms, and the tx and rx must be synchronized and the signal processing systems should account for this. [Ref](https://core.ac.uk/download/pdf/30784809.pdf)

## Simple Array Explanation

A phased array is a group of antennas whose effective (summed) radiation pattern can be altered by phasing the signals of the individual elements.

By varying the phasing of the different elements, the radiation pattern can be modified to be maximized/suppressed in given directions, within limits determined by:
    * the radiation pattern of the elements
    * the size of the array, and
    * the configuration of the array

## Array Direction of Pointing

[This](https://core.ac.uk/download/pdf/11141258.pdf) paper describes the fact that if the array is perpindicular to earth, there is a reduced observable beam area, this reducing detection probability. However, when the angle is no longer 90 degrees, then there is increased signal attenuation due to free space even though the detecting area is increased. These two should be considered.

### Maximum scanning directions

The maximum scanning angles that antenna arrays can achieve is -60 degrees to 60 degrees, this is referenced [here](https://arxiv.org/ftp/arxiv/papers/1408/1408.0977.pdf)

# Why ISR?

According to the theory of incoherent scattering first presented by Gordon in 1958 ([Incoherent Scattering of Radio Waves by Free Electrons with Applications to Space Exploration by Radar](https://ieeexplore.ieee.org/document/4065300)).
ISR is the only equipment which has such ability. The measured area can be covered from 60 to 2000 km, and ISR has become the most powerful ground-based tool currently for the study of ionospheric structures and kinetic processes[ref](https://agupubs.onlinelibrary.wiley.com/doi/epdf/10.1029/2007JA012250)

The system is capable of measuring space debris ([Space Debris Measurements using the Advanced Modular Incoherent Scatter Radar](https://amostech.com/TechnicalPapers/2015/Poster/Nicolls.pdf))


# Electronics

RoHS standards
lead free components

# Detection Systems

[This](https://core.ac.uk/download/pdf/30784809.pdf), [this](http://epubs.surrey.ac.uk/813039/1/Orbit%20determination%20of%20space%20debris%20using%20a%20Bi%20static%20radar%20configuration%20with%20a%20multiple%20beam%20receiver.pdf) implementation makes use of Tailored Orbit Determination (OD) algorithms. 

Transmit uniformally. Then, receive the signal, and using signal processing, combine the signals to create the "phasing"

A typical radar system will operate with a detection probability of 0.9 and a probability of false alarm of 10^-6. The required signal to noise ratio can then be read directly off the graph as 13.2 dB. Note that this is for a single pulse of a steady sinusoidal signal in Gaussian noise with no detection losses.

## Multiple Pulses

