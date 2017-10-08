README #
Components
	1. generate_instring_chanles - query tag names, and competitors names, calculate the most intresting accounts by tag pupularity.
	2. Get followers_of_instresting_chanels
	3. Filter_users_by_weight - configure what gives the weight by age, sex, keywords, followers count.
	4. Trafic execution - like, comment, follow.
	

Stages
	1. user + password, show basic info
	2. get tag and collect x most populer acounts in that tag 
	3 .multitherded 
	4. get follwers in multithreded way - thred per user.
	5. trafic exectiuon by limit multithreded.
	6. storge - mongodb?
	7. work on component #3 most of the logic. should considure desine and workflow on that part.
	
	
Dependencies
1. https://github.com/guilhermefarias/instagram-api ???? need to check of the api provides all of the necesery functions
2. https://github.com/huttarichard/instagram-private-api - no ned of access token, but need to run on VM with ARM process due to libstrings.so. see .signPayload() section.
