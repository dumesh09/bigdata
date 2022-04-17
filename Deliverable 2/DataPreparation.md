**Geography\_industry:**

\#   Column            Non-Null Count   Dtype         

\---  ------            --------------   -----         

` `0   post\_date         394393 non-null  datetime 

` `1   state             387832 non-null  object        

` `2   industry          369742 non-null  object       

` `3   count\_id\_indexed  394392 non-null  float64 

- There are a total number of 394393 observations and the following variables have more than 94% of data. So, these variables cannot be removed.
- The variable Post\_date has 394393 records, and it does not have any missing values. So, we cannot remove the post\_date variable.
- The variable state has 6561 missing values, and it corresponds to 1.6 % of total data as missing and 1.6% is very less so we include the state variable.
- The variable industry has 24651 records as missing values, and it corresponds to 6.25% of total data as missing. However, we will try to consider this variable as it has less than 30% of its missing values.
- The variable count\_id\_indexed has 1 record as missing value and it corresponds to 0.0025% of total data as missing and it is a very  very less significant amount of data as missing so we cannot ignore this variable.
- Overall, all the variables have 98% amount of data.

**Industry:**

- Communication         24650
- Construction          24650
- Energy                24650
- Entertainment         24650
- Financial Services    24650
- Healthcare            24650
- Hospitality           24650
- Insurance             24649
- Manufacturing         24649
- Mining                24649
- Real Estate           24649
- Retail                24649
- Services              24649
- Transportation        24649
- Wholesale             24649

If we observe in industry variable Communication, Construction, Energy, Entertainment, Financial Services, Healthcare, Hospitality has equal amount of share contribution. Insurance, Manufacturing, Mining, Real Estate, Retail, Services, Transportation, Wholesale these sectors have equal number of shares in market and slightly less than above-mentioned sectors.

**States:**

AK    6560

KS    6560

AL    6560

NH    6560

NE    6560

`      `... 

Ko      16

MB      16

ZH      16

BS      16

LU      16

From above states we can observe that AK,KS,AL,NH,NE states have an equal number of industries that is 6560 while Ko,MB,ZH,BS,LU states have less number of industries that is 16.

**Job\_family\_role:**

RangeIndex: 619919 entries, 0 to 619918

Data columns (total 4 columns):

` `#   Column            Non-Null Count   Dtype         

\---  ------            --------------   -----         

` `0   post\_date         619919 non-null  datetime64[ns]

` `1   job\_family        619347 non-null  object        

` `2   role              619904 non-null  object        

` `3   count\_id\_indexed  619919 non-null  object

- There are a total number of 619919 observations and the following variables have more than 94% of data. So, these variables cannot be removed.
- The variable Post\_date has 619919 records, and it does not have any missing values. So, we cannot remove the post\_date variable.
- The variable job\_family has 572 missing values, and it corresponds to 0.09 % of total data as missing and 0.09% is very less so we include the job\_family  variable in our data.
- The variable role has 15 records as missing values, and it corresponds to 0.002% of total data as missing. However, we will try to consider this variable as it has less than 0.5% of its missing values.
- The variable count\_id\_indexed has 619919 records, and it does not have any missing values. So, we cannot remove the count\_id\_indexed variable.

**Job\_family:**

Healthcare                        114519

Finance/Insurance                  95932

Entertainment and Recreation       52661

Manufacturing/Operations Staff     48559

IT                                 44100

Hospitality Staff                  40234

Skilled Trades                     38169

Food & Beverage                    30458

Retail Staff                       27241

Marketing/Advertising              23357

Facilities/Constr                  21275

Human Resources                    20388

Supply Chain Staff                 19272

Unassigned                         18167

Sales                              12136

Security                            5640

Customer Service                    5004

Product Management                  2235

- From above we can observe that Healthcare jobs contribute more while Product management jobs contribute less than all jobs. However, Finance/Insurance jobs stand in second position and Entertainment and Recreation jobs stand in third position.

**Roles:**

EXCUDE                             563

Marketing Assistant                563

Safety Manager                     563

Brand Specialist                   563

Category Manager                   563

`                                  `... 

Organ Procurement Technician         2

HRSC Representative                  2

Groundskeeper/crew                   2

Management Reporting Specialist      2

Behavior Modification Therapist      1


From above roles we can see that Excude, marketing assistant, safety manager, brand specialist, category manager roles having equal number of employees that is 563. Whereas behavior modification therapist role is having less number of employees that is 1.
