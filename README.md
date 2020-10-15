# CMP 459 - Introduction to Data Mining - Fall 2020, SFU
**Prof** - Martin Ester

**TAs** - Madana Krishnan V K, Rhea Rodrigues

This repository consists of the dataset to be used for the course project. The dataset revolves around the novel COVID-19 pandemic that has emerged and taken the world by storm. The first file contains the data for individual cases and the second file contains the number of cases based on location. The 2 files are obtained from an open-source repository (link below) and have been processed to make it easier to use. To ensure consistency, the dataset has been frozen to September 20th, 2020.

* https://github.com/beoutbreakprepared/nCoV2019
* https://github.com/CSSEGISandData/COVID-19

<h2>Project Structure</h2>
|-- covid-19<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-- ExploratoryDataAnalysis.ipynb<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-- ExploratoryFigures<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   |-- Active.png<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   |-- BoxPlotForEveryColumninLocation.png<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   |-- CombinedScatterPlot.png<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   |-- Confirmed.png<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   |-- DateConfirmed.png<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   |-- Deaths.png<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   |-- Fatality_Ratio.png<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   |-- FittedRegPlotActiveDeathRatio.png<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   |-- FittedRegPlotActiveFatilityRatio.png<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   |-- FittedRegPlotConfirmedActive.png<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   |-- FittedRegPlotConfirmedActive2.png<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   |-- FittedRegPlotConfirmedDeaths.png<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   |-- FittedRegPlotConfirmedDeaths2.png<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   |-- FittedRegPlotConfirmedRecovered.png<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   |-- FittedRegPlotConfirmedRecovered2.png<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   |-- Incidence_Rate.png<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   |-- IndividualBoxPlot.png<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   |-- IndividualDataHeatMap.png<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   |-- LocationDataHeatMap.png<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   |-- LowerIndividualDataHeatMap.png<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   |-- Recovered.png<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   |-- UpperIndividualDataHeatMap.png<br/>
|-- IndividualTransformation.py<br/>
|-- LocationDataImpute.ipynb<br/>
|-- LocationDataSetImputation<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   |-- ImputeLatLong.py<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   |-- ImputedIncidenceRate.csv<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   |-- ImputedLongLat.csv<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   |-- ImputedProvince.csv<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   |-- IncidenceRate.py<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   |-- LatLongMissing.csv<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   |-- MissingIncidenceRate.csv<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   |-- ProvinceImpute.py<br/>
|-- LocationTransformation.py<br/>
|-- Merge.py<br/>
|-- MergeData<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   |-- CombinedData.csv<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   |-- IndividualData.csv<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   |-- LocationData.csv<br/>
|-- Outliers.ipynb<br/>
|-- README.md<br/>
|-- dataset<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   |-- CleanedIndividualCases.csv<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   |-- CleanedLocations.csv<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   |-- OutlierIndex.csv<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   |-- RevisedIndividualData.csv<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   |-- RevisedLocationData.csv<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   |-- processed_individual_cases_Sep20th2020.csv<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   |-- processed_location_Sep20th2020.csv<br/>

<h2>Pre-req: Third-Party Libraries Install Guide</h2>

Please install the following libraries using:
```bash
pip3 install numpy
pip3 install pandas
pip3 install seaborn
pip3 install geopy
pip3 install seaborn
pip3 install -U scikit-learn
pip3 install matplotlib

```

<h2> Order to Run the Project </h2>

1. ExploratoryDataAnalysis.ipynb <br/>
2. DataCleaning.ipynb <br/>
    &nbsp;&nbsp;&nbsp;&nbsp; 2.1 - impute_province_state_date.ipynb <br/>
3. python3 LocationDataSetImputation/ProvinceImpute.py <br/>
    &nbsp;&nbsp;&nbsp;&nbsp; 3.1 - LocationDataImpute.ipynb <br/>
4. python3 LocationDataSetImputation/ImputeLatLong.py <br/>
    &nbsp;&nbsp;&nbsp;&nbsp; 4.1 - LocationDataImpute.ipynb <br/>
5. python3 LocationDataSetImputation/IncidenceRate.py <br/>
    &nbsp;&nbsp;&nbsp;&nbsp; 5.1 - LocationDataImpute.ipynb <br/>
6. Outliers.ipynb <br/>
7. python3 IndividualTransformation.py <br/>
8. python3 LocationTransformation.py<br/>
9. python3 Merge.py<br/>

<h2> Additional Information </h2>

1. After running ExploratoryDataAnalysis.ipynb, the figures are stored in ExploratoryFigures directory.</br>
2. Do not run all the cells of LocationDataImpute.ipynb at once. Please follow the guidelines in .ipynb file. Since, all the files are present, if you run all the cells, you will get no error.
3. Outliers.ipynb file contains information what the outliers are and how they are dealt.
4. IndividualTransformation.py file transforms the final version of processed_individual_cases_Sep20th2020.csv for merging.
5. LocationTransformation.py file transforms the final version of processed_location_Sep20th2020.csv for merging.
6. Merge.py file merges the two dataframe on province, country attribute. 



