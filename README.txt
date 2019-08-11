data project pipeline template

sample data from https://www.americansocceranalysis.com/asa-xgoals/


source			process			artifact		description

source import	->				data.csv
requirements	->				README.yaml		documentation, eg data dictionary

data.csv	->	dtools.explore	->	explore.csv		basic info and stats
(or transf.csv)				->	explore<column>.csv	for object (str) datatypes
					->	corr.csv		correlation matrix

data.csv	->	clean.py	->	clean.csv
		->	dtools.dropped	->	dropped.json		archives columns dropped, with index

clean.csv	->	transf.py	->	transf.csv		feature engineering


