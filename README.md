# Clinical Trials API

An API to access information relating to the active clinical trials (as of 6/18). 


All, apologies for delay and lapse in communication. 

The API now includes information pertaining to 81,666 clinical trials [about 4K as of now but background process running to finish]. 

https://clinical-trial-finder-api.herokuapp.com/api/v1/studies/all

I have limited results returned by any single query to 200.

The following attributes are available for each trial (some trials have missing attributes): 
- `nct_id`: A unique id assigned to each trial
- `start_date`: Start date of the trial (may be in the future)
- `completion_date`: Expected compeltion date of the trial
- `study_type`: The type of trial 
- `overall_status`: The current status of the trial (e.g., Recruiting)
- `brief_title`: The title of the trial
- `phase`: The step in the regulatory process that the trial is currently in
- `condition_name`: 
- `description`: A description of the trial
- `gender`: The gender of people potentially eligble for the trial
- `minimum_age`: The minimum age of people potentially eligble for the trial
- `maximum_age`: The maximum age of people potentially eligble for the trial
- `healthy_volunteers`: Indication of whether or not the trial is recruiting healthy volunteers 
- `sponsor_name`: The entity backing the clinical trial
- `name`: The primary point of contact's name
- `phone`: The primary point of contact's phone number
- `email`: The primary point of contact's email address
- `completion_prob`: [Currently A Placeholder] An estimated likelihood of the clinical trial reaching completion (as opposed to being withdrawn/suspended/terminated). The estimated likelihood derived from a predictive model trained on historical data.

Options: I am going to add options to filter results by a number of these parameters this afternoon.

Note: The date attributes are getting encoded oddly, am going to look into keeping them as plain text. 