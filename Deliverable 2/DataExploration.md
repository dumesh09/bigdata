**Data Exploration**

**Data Set Info**

This dataset provides updates on the volume of US job listings filtered by geography industry job family and role; normalized to pre-covid levels. The data set is configured into 7 csv files comprising 9.2+MB data. There are 394393 observations and 6 columns among which 4 attributes are of categorical type and the remaining are numerical attribute and date attribute. Looking at the columns, the data set provides us information about total number of US job hiring listings in various states, industries (Real estate, Retail, Transportation etc.), job family (Customer Service, Entertainment, Finance etc.), role (Call Center Manager, Actor, CFO etc.) All the columns are not null data fields.

|**Data Columns**|**Data Type**|**Description**|
| :- | :- | :- |
|post\_date|date|Analysis date|
|industry|varchar|Industry name (note: low count industries excluded)|
|job\_family|varchar|Job family name (note: low count job families excluded)|
|state|varchar|State abbreviation (note: included Washington DC but excludes US territories)|
|role|varchar|Role name (note: low count roles excluded; titles normalized to common roles based on Greenwich.HR role taxonomy)|
|count\_id\_indexed|decimal|Count of the total number of unique listings for US jobs for a period of 7 days ending on post\_date, divided by the count of total number of unique listings for US jobs within the job family and role for the period Feb 24 2020-Mar 1 2020|

Below table shows the summary of numerical and categorical variables:

|**Job\_family**|**Count\_id\_indexed**|**Industry**|**Count\_id\_indexed**|**Role**|**Count\_id\_indexed**|**State**|**Count\_id\_indexed**|
| :- | :- | :- | :- | :- | :- | :- | :- |
|Customer Service|5004|Communication|567|.Net Specialist|96|AK|631.8484|
|Entertainment and Recreation|52661|Construction|567|Abstractor|408|AL|762.1853|
|Facilities/Constr|21275|Energy|567|Account Manager|563|AR|779.4816|
|Finance/Insurance|95932|Entertainment|567|Accountant|563|CA|600.252|
|Food & Beverage|30458|Financial Services|567|Accounting Manager|563|AZ|676.0278|
|Healthcare|114519|Healthcare|567|Accounting Specialist|563|CO|602.5249|
|Hospitality Staff|40234|Hospitality|567|Accounts Payable Specialist|561|CT|674.1802|
|Human Resources|20388|industry|1|Accounts Receivable Specialist|562|IL|667.3717|
|IT|44100|Insurance|567|Acquisition Specialist|309|DC|474.7179|
|Manufacturing/Operations Staff|48559|Manufacturing|567|Activity Coordinator|506|DE|737.5532|
|Marketing/Advertising|23357|Mining|567|Actor|447|IN|726.8867|
|Product Management|2235|Real Estate|567|Actuary|544|FL|655.6748|
|Retail Staff|27241|Retail|567|Acupuncturist|413|GA|702.454|
|Sales|12136|Services|567|Administrative Assistant|563|HI|552.828|
|Security|5640|Transportation|567|Administrator|562|IA|742.8861|
|Supply Chain Staff|19272|Wholesale|567|Admissions Coordinator|552|ID|760.8748|





