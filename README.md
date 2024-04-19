# Computational-Method-for-Identification-of-Potential-G-Quadruplex-
Computational Method for Identification of Potential G-Quadruplex Structures and  Stability Prediction in Coronaviridae Family
G-quadruplex identification and secondary structure stability prediction tool

G4Boost requires python3.

Prediction models was constructed using the sklearn module. Prebuilt regression and classification models are available through GitHub.

Locate regression and classification models (G4Boost_regressor.json and G4Boost_classifier.json) into the same directory with G4Boost.py
required python packages:
	pandas==1.4.3
	xgboost==1.4.2


Options:
--version             show program's version number and exit  
-h, --help            show this help message and exit
-f FASTA_FILE, --fasta FASTA_FILE
		      Query sequences in fasta format
--classifier JSON_FILE
		      Classification model in .json format [optional]
--regressor JSON_FILE
		      Regression model in .json format [optional]
-N MAX_LOOP_LENGTH, --maxloop MAX_LOOP_LENGTH
		      The maximum number of bases allowed within a loop region [default=12]
-n MIN_LOOP_LENGTH, --minloop MIN_LOOP_LENGTH
		      The minimum number of bases allowed within a loop region [default=1]
-G MAX_G_BASES, --maxG MAX_G_BASES
		      The maximum number of consecutive guanine bases allowed within a G-stem [default=7]
-g MIN_G_BASES, --minG MIN_G_BASES
		      The minimum number of consecutive guanine bases allowed within a G-stem [default=1]
-l NUMBER_OF_LOOPS, --loops NUMBER_OF_LOOPS
		      The maximum number of fleaxible loops separating the G-stems [default=11]
--noreverse
		      Do not search the reverse complement of the input fasta.
-q, --quiet
		      Do not print progress report (i.e. sequence names as they are scanned).
