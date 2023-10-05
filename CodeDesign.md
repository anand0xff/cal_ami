# Code Design

### General

"Tables" could be pandas (pd) tables - mixed types of columns, pd methods & attributes & flexible formatting come for free.  Some coder learnig overhead initially.  Stick with astropy tables?

Mapping human readable names to disk filenames: text? pandas? Use low-learning-overhead easy-to implement code.

Incoming data sets real/fake/grafted hdrs, ... but MAST format

Let's think about dataset needs:

	forddataset = Dataset(newdirfordata, (1260,'4346045ccd2c42d9b438b192cf412a32', 'uncal')
	fordataset.create_summary('dt_type_file.txt') # or make this a param in the __init__?
	# User creates the 'my_mapping.txt' file by looking at the dt_type_file.txt or other way(?)
	
	forddataset.create_mapping('my_mapping.txt', 'my_mapping.txt')
	# Now we have easily understood 'pointers;' in 'my_mapping.txt' file for further processing
	

≈        

		def __init__(self, datafrom, 
		                   filetypes=(),
		                   infodir = ,
		                   verbose=False):
		   """ Finds data on file or downloads with shell call to jwst_download.py """ 
		   ****************************************************
		   *  Is generalizing to get data two ways overkill?  *
		   *  Restrict to one filetype at a time?             *
		   ****************************************************
		   
			datafrom - location_on_disk or (aptid, token, datadir 
			             --- use jwst_download.py, put data in datadir)
			filetypes - use jwstdownload arg(s) syntax.
			infodir - where to log details of driver input, running, etc.
			
			creates
				self.rootlist = self.getdataset(dataset) # as many rootnames as exposures
				self.filetypes
				infodir
				
				
				Questions:
			         - how do we treat specifying 'level' of data calibration?
			         - writes rootlist items to disk file (format? .txt?) 
			         - stores directory where data reside in self.datadir
			self.summary =  create_summary(rootlist) 
			
			
		def create_summary(self, rootlist):
			creates and stores information table like Deepashri's table 
			    - get info by looking at headers only?
			    - read full headers into memory and just retrieve from them by keyword?

			
		def create_mapping(self, user_file, association_file):
			like Rachel's mapping for COM data: created from  self.rootlist and user_file
			maps  association_file (eg 'abdor_72ke') given by user to a mast(like) filename
			
		def info(self,...):
			write out dataset info in requested formats
				- Deepashri's big table output
				- associations between human-requested string ('abdor_obs1') and mast-like filename
			
### Class Data

	each exposure (eg mast file) is an instance of Data.
	methods to be developed as we ingest some com analyses and cal analyses tasks  


Let's think about data manipulation needs.  

Use mapped names that are relevant to the analysis/investigation, assuming the right stage of data (uncal, rate, ...) for the data analysis task. 

Tasks can be done: 

	def prep_data(self, {datasetname: ...):
		Examples: 
		data cleaning with rejecting 2, 3, or 4 std devs from a median   
		dicing for CM examination as in commissioning CM analysis8  
		fixing bad pixels with a certain set of parameters (rejection, max iterations)
		Includes putting extracted data into mast-like files for eg calibration using early vs late groups, 

	def pipe_data(self, ...):
		apply particular jwst pipeline steps or more atomic processing included in pipeline  
		
	def rearrange_data(self, ...):
	
### Org questions:

	Where do we store useful 'meta-information' if we want to easily reprocess with the same ref files and different algorithm (eg changed threshold or max iteration in bp_fix) E.g., CRDS_VER, CRDS_CTX,, jwst software branch info,... 
	
--
--

## Prototyping using CAL_1516 design

###Quantify CM in data

Top level driver - set-up allows for using multiple datasets later.:

	userhomedir = ...
	outputdir = ...
	analysisname = "CMquantification"
	dataset = Dataset(datafrom = userhomedir+ + "/niriss/cal_1516/pipeline_calibrated_data/",
                       filetypes = ("ramp"),
                       outputdir = ...,
                       verbose=True)
--


