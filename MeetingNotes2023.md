# AMI Calibration Meeting Notes

## SLM notes Sep 25:  

Charge migration (CAL-NIS-026; APT 1516, but can include additional data)    
Goals:
1. Quantify ADU level at onset of charge migration. Use various thresholds for non-linearity effects, e.g., 0.5%, 1%, 2%, 3%?   
2. Test charge migration mitigation in pipeline. What contrast level can be achieved with and without charge migration mitigation?  
3. Identify ADU level for “effective saturation,” the limit at which we advise users to stay below when designing programs. Consider:    
	- At what level of charge migration does the pipeline fix not recover good enough PSF sampling to allow better contrast sampling? Should that be the limit? Or should we use a limit at which charge migration occurs?  

What’s the metric for completion?    
* Consider analysis program “complete” when the answers to the above are determined?   
* Or will further analysis to improve charge migration correction be part of this analysis program if the contrast levels aren’t deep enough?  

Other calibration programs/analysis needs to prioritize. What’s the next most important project to focus on in the coming quarter. Note that data for these calibration programs are already available:   
* Updates to ImPlaneIA algorithm  
* CAL-NIS-011 (APT 1504) NIRISS AMI Intra-pixel Response Calibration  
	o	Small offsets of star to different relative pixel positions to calibrate intra-pixel sensitivity of PSF.   
* APT 4478: Test AMI filter offsets to bring target at pixel center   
* APT 4480: AMI Calibrator Requirements    