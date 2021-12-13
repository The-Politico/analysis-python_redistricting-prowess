download_data:
	aws s3 sync \
		"s3://staging.interactives.politico.com/data/redistricting-tracker/" \
		"raw_data/"

upload_data:
	aws s3 sync \
		"raw_data/" \
		"s3://staging.interactives.politico.com/data/redistricting-tracker/"
