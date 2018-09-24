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