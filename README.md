# cal_ami

Author(s): Anand Sivaramakrishnan, Deepashri Thatte, Rachel Cooper

## Purpose

Repository for code used for calibration of AMI data.

#### Development guidelines:

- Design code at high level first and walk-through by one other AMI team member
- Keep repo up-to-date with code during development (even partially-written code!)
- Include design into code in docstring comment
- Encapsulate related sets of quantities (parameters for big processing steps, eg implaneia run, median filtering raw data, etc)?
- Plan data file manipulation/cleaning, develop in notebooks, then put into single (eg) calutil.py module and remove from notebooks.  Avoid repeated code blocks in different notebooks & scripts
- Use in-line function documentation, comments, PEP8 style as much as is reasonable
- Develop convenient mapping of data file names to descriptive names (as done in AMI COM) (RAC is working on this)

## Calibration Programs

#### Cycle 1 
| APT Number | Cal Number | Title | Description |
|---|---|---|---|
| 1504 | CAL-NIS-011 | Intra-pixel Response Calibration | A series of exposures of a single star with sub-pixel offsets will be used to characterize the variations in the AMI PSF with the position of the star within the pixel. |
| 1506 | CAL-NIS-013 | NRM Fractional Throughput Cal (Full Frame) | Observations will be made of a standard star in regular full frame imaging and then with the NRM in the beam to calibrate the fractional throughput of the mask for photometric calibration purposes |
| 1507 | CAL-NIS-014 | NRM Fractional Throughput Cal (Sub80) | Observations will be made of the single star HD 49306 in the SUB80 read-out in regular imaging and then with the NRM in the beam to measure the fractional througput of the mask for photometric calibration purposes. This measurement differs from the full frame measurement because there will be signal losses out of the small sub-array, hence the fractional throughput measured here will not be the same as measured with the full frame imaging. |
| 1508 | CAL-NIS-016 | NRM Phase Calibration | A high S/N observation of a single star will be taken in the three medium-band NIRISS AMI filters. These observations will be used to determine the AMI closure phases. |
| 1509 | CAL-NIS-017 | NRM Pixel Linearity Cal | NIRISS/AMI observations of three bright stars will be taken to characterize the linearity response of the peak pixels in the PSF to better precision than can be obtained in ground-based linearity measurements. The observations will be taken with dithering between the 4 primary positions, so this will also provide some persistence data for analysis. |
| 1516 | CAL-NIS-026 | AMI Charge Transfer Characterization | Observations of standard stars in NIRISS AMI mode with differing peak ramp counts and the same total exposure time are to be taken to assess the effects of charge migration on the interference pattern.  In this preliminary test, the F430M and F277W filters are used, and in the wide filter a smaller total number of photons is collected per ramp set-up. |

#### Cycle 2 
| APT Number | Cal Number | Title | Description |
|---|---|---|---|
| 4478 | CAL-NIS-212 | AMI Pixel Placement | Observations of two stars, selected to be single stars, will be made in the AMI mode with the three medium-band filters to test that the star can be positioned consistently at the centre of a pixel allowing for the filter-to-filter offsets that are observed in normal imaging. Having a consistent position for the observations in different filters is helpful in the analysis of the amplitudes and phases of the interference pattern observed through the mask, and should improve the AMI sensitivity |
| 4480 | CAL-NIS-214 | AMI Calibrator Requirements | Observations of four single stars as AMI mode calibration sources are requested. The first two have closely matched brightesses and the third star is of similar spectral type but is a factor of 1.5 fainter. The last star is the same brightness as the third star but of a somewhat different spectral type. Cross-calibrations of these stars with each other will give information to guide the requirements needed for selecting AMI phase calibration sources. |
| 4481 | CAL-NIS-216 | AMI Subpixel Contrast | A series of AMI mode observations with sub-pixel offsets are requested of the AB Dor binary system and a single star phase calibration target. This star was previously observed in commissioning. Analysis of these observations compared to the commissioning observations will provide information about the effect of small mis-matches in the calibration source and the science target on the the contrast that can be achieved in the data reduction. |

## Details
In-progress code design should be written in CodeDesign.md. Usage details of working code should be copied here. 

#### Class `Dataset`
[details here]


#### Class `Data`
[details here]