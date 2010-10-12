#!/usr/bin/env python
import sys

ed = sys.argv[1]

bandw = ed[0:4]
modulation = ed[4]
signalmod = ed[5]
information = ed[6]

if bandw.count("K"):
	bandw = bandw.replace("K",".")
	bandw += " kHz"
if bandw.count("M"):
	bandw = bandw.replace("M",".")
	bandw += " MHz"
print "Bandwidth = " + bandw

modulation_t = {'A': 'Double-sideband (AM)', 'C': 'Vestigal sideband', 'B': 'Independent sidebands', 'D': 'Amplitude and angle modulation', 'G': 'Phase Modulation', 'F': 'Frequency Modulation (FM)', 'H': 'Single-sideband full carrier', 'K': 'Amplitude modulated pulses', 'J': 'Single-sideband suppressed carrier', 'M': 'Pulses modulated in position/phase', 'L': 'Pulses modulated in width/duration', 'N': 'Unmodulated', 'Q': 'Angle-modulated carrier during pulse', 'P': 'Unmodulated pulses', 'R': 'Single-sideband reduced or variable carrier', 'W': 'Not otherwise covered, multiple modes', 'V': 'Combination of modulations of a pulse', 'X': 'Other Modulation'}
print modulation_t[modulation]

signalmod_t = {'1': 'Single subchannel, digital, no subcarrier', '0': 'Unmodulated main carrier', '3': 'Single channel, analog', '2': 'Single subchannel, digital, subcarrier', '7': 'Two or more channels, digital', 'X': 'Other Subchannel Type', '9': 'Two or more channels, analog and digital', '8': 'Two or more channels, analog'}
print signalmod_t[signalmod]

information_t = {'A': 'Telegraphy for aural reception', 'C': 'Facsimile', 'B': 'Telegraphy for automatic reception', 'E': 'Telephony (including sound broadcasting)', 'D': 'Data transmission', 'F': 'Television (video)', 'N': 'No information transmitted', 'W': 'Combination of different data', 'X': 'Other information'}
print information_t[information]

if (len(ed) == 9):
	signaldetails = ed[7]
	multiplexingnature = ed[8]
	
	signaldetails_t = {'A': 'Two-condition code differing numbers/durations', 'C': 'Two-condition code same number duration with error correction', 'B': 'Two-condition code same number duration no error correction', 'E': 'Multi condition code representing signal element', 'D': 'Four condition code representing signal element', 'G': 'Sound of broadcast quality (mono)', 'F': 'Multi condition code representing characters', 'H': 'Sound of broadcast quality (stereo/quad)', 'K': 'Sound of commercial quality with use of frequency inversion / band splitting', 'J': 'Sound of commercial qualiy, unscrambled, no level control', 'M': 'Monochrome video', 'L': 'Sound of commercial quality with seperate FM signals controlling demodulated signal level', 'N': 'Color video', 'W': 'Combination of above', 'X': 'Other signal type'}
	print signaldetails_t[signaldetails]
	
	multiplexing_t = {'C': 'Code division multiplex', 'F': 'Frequency division multiplex', 'N': 'No multiplexing', 'T': 'Time division multiplex', 'W': 'Frequency and time division multiplex', 'X': 'Other types of multiplexing'}
	print multiplexing_t[multiplexingnature]