# Clinical Trials API

An API to access information relating to the active clinical trials (as of 6/18). The API includes information pertaining to 81,666 clinical trials.

The base API endpoint is: 

https://clinical-trial-finder-api.herokuapp.com/api/v1/studies/all

Which fill shows 200 of the trials from the API. Note, by default the API returns a maximum of 200 results per query. 

**The following attributes are available for each trial (some trials have missing attributes):**

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
- `minimum_age`: The minimum age of people potentially eligble for the trial. Returned as a string
- `maximum_age`: The maximum age of people potentially eligble for the trial. Return as a string
- `healthy_volunteers`: Indication of whether or not the trial is recruiting healthy volunteers 
- `sponsor_name`: The entity backing the clinical trial
- `name`: The primary point of contact's name
- `phone`: The primary point of contact's phone number
- `email`: The primary point of contact's email address
- `completion_prob`: [Currently A Placeholder] An estimated likelihood of the clinical trial reaching completion (as opposed to being withdrawn/suspended/terminated). The estimated likelihood derived from a predictive model trained on historical data.
- `minimum_age_val`: The minimum age of people potentially eligble for the trial. Returned as a integer
- `maximum_age_val`: The minimum age of people potentially eligble for the trial. Returned as a integer

**Working With The API:**

The API provides a number of options for users to shape the results provided. For example, a view of interventionalist trials targeting men with prostate cancer can be found with the following request: 

`https://clinical-trial-finder-api.herokuapp.com/api/v1/studies/query?phase=phase%202&gender=male&studytype=interventional`

The API also offers a basic search functionality which seeks to identify clinical trials related to the provided argument. To search for trials related to prostate cancer, the following request could be submitted: 

`https://clinical-trial-finder-api.herokuapp.com/api/v1/studies/search?description=Prostate%20Cancer`

**Acceptable Request Arguments**

The following arguments can be passed in any combination to the `https://clinical-trial-finder-api.herokuapp.com/api/v1/studies/query?` endpoint:

- **phase:** Specify the phase with `phase=phase+1`. Common arguments are: 'Phase 1', 'Phase 2', 'Phase 3', and 'Phase 4'
- **gender:** Specify the target gender with `gender=female`. Common arguments are: 'All', 'Female', 'Male'
- **studytype:** Specify the study type with `studytype=interventional`. Common arguments are: 'Interventional', 'Observational', 'Observational [Patient Registry]', 'Expanded Access'
- **limit:** Defaults to 200. User customize the limit by passing an integer as an argument as follows: `limit=20`
- **status:** Specify the status of the trial with `status=recruiting`. Common arguments are: 'recruiting', 'active, not recruiting', 'not yet recruiting', 'available', 'approved for marketing'
- **healthy:** Specify whether the returned trials accept healthy volunteers with `healthy=yes`. Available arguments are: 'no', 'yes', 'not provided'
- **predprob:** Specify a minimum likelihood of a trial reaching completion. Acceptable arguments are floats between 0 and 1, the arguments can be specified as follows `predproba=0.7`
- **maxage:** Specify the maximum patient age that the trial accepts with `maxage=80`. Acceptable arguments are integers between 0 and 100
- **minage:** Specify the minimum patient age that the trial accepts with `minage=18`. Acceptable arguments are integers between 0 and 100

As described above, any string can be passed to the search (https://clinical-trial-finder-api.herokuapp.com/api/v1/studies/search?) endpoint as follows: 

- `https://clinical-trial-finder-api.herokuapp.com/api/v1/studies/search?description=malignant%20melanoma`
- `https://clinical-trial-finder-api.herokuapp.com/api/v1/studies/search?description=chronic+hypertension`
- `https://clinical-trial-finder-api.herokuapp.com/api/v1/studies/search?description=neurodegenerative`

**Additional Notes**

- Requests are case insensitive.
- Missing attributes have been filled with the string `Not Provided`
- Spaces in requests can be encoded as `+` or `%20`
- Please do not abuse this freely available API.
- All data provided via the API is from `ClinicalTrials.gov` 
- Please reach out if you are interested in contributing to the development and maintenance of the API