# aiHackCovid
#### This is team 2 submission done by Rosella, Bharath Raj and Thanasis  for the [https://aihackcovid.aimedgroningen.com/](https://aihackcovid.aimedgroningen.com/) hackathon.


## Our Goals:
- Explore the policies adopted by the different European countries, trying to highlight similarities and patterns among them
- Find trends and projections of new_deaths_per_million population in the Global scenario,EU continent and the Netherlands.

Our datasets: 
[1] Oxford Covid-19 Government Response Tracker (OxCGRT) : [https://github.com/OxCGRT/covid-policy-tracker]
[2]COVID-19 Dataset by Our World in Data : [https://github.com/owid/covid-19-data]

To get started:
- install the packages from the requirements.txt

### Goal 1: Explore the policies adopted by the different European countries, trying to highlight similarities and patterns among them
>We use the OxCGRT dataset for this. 
Steps to run:
- Run the script...[commands needed]
- observe ...
- the images are saved in ....
- interpret

### Goal 2: Find trends and projections of new_deaths_per_million population in the Global scenario,EU continent and the Netherlands
> We use the OurWorldinData(OWID) dataset 
> We gather the dataset over the entire world, create a dataset of our own by selecting feature vectors : 
- Vaccination_ratio : It is given as a the ratio between the number of people who have been vaccinated(atleast 1 dose) and the total population (in 2020) before the pandemic
- Stringency_score : This is a score given by OWID based on the stringency measures taken in the location by closing of schools, public transport etc. This score is a measure between 0 to 100.
- positive rate : The share of COVID-19 tests that are positive given by OWID.
- current reproduction rate : This is the R_0 value, given by OWID.

Based on the above features we predict the new_deaths_per_million in our prediction models.
- We do the prediction models for Global scenario [Global_Projection Model.ipynb]
- We do the prediction models for Europe scenario [EU_Projection Model.ipynb]
- We do the prediction models for NL scenario [NL_Projection Model.ipynb]

<Things to do>  
- We create a synthetic dataset for forecasting the new_deaths_per_million using the above models on all the three regions [Creating_synthetic_dataForProjection.ipnyb]
- We visualize the projections until March 1st 2022 on all the three models and observe their behaviour [Visualisation_and_inference.ipnyb]
