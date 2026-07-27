Week 1 – Data Cleaning & Preparation
Day 1 – Understanding the Project

Goal: Know what  i're going to build.


Collected the Olist E-commerce dataset.
Read the project roadmap.
Understood that the final dashboard will show:
Customer Retention
Cohort Analysis
Customer Lifetime Value (CLTV)
Day 2 – Import Data

imported:

import pandas as pd

Loaded datasets like:

customers
orders
order_items
payments
products
reviews
sellers

Then checked

head()
shape()

Meaning:

head() → first 5 rows
shape() → rows and columns

Example

100000 rows
10 columns

This helps understand dataset size.

Day 3 – Inspect Data Quality

checked

info()

to know

data types
missing values
memory usage

Then

isnull().sum()

to find empty values.

Then

duplicated()

to identify duplicate rows.

Purpose:

Before analysis, ensure the data is clean.

Day 4 – Cleaning the Data

 kept only

Delivered Orders

because

Cancelled or unavailable orders don't generate revenue.

Then  i handled missing values using

fillna()
dropna()

Finally, saved cleaned datasets.

Day 5 – Working with Dates

 i converted

2018-01-05 12:45:32

into datetime format.

Using

pd.to_datetime()

Then extracted

2018-01

from every purchase.

This purchase month becomes the foundation of Cohort Analysis.

Day 6 – Merge Data

Different datasets contain different information.

Example

Customers

↓

Orders

↓

Payments

↓

Order Items

 i merged them using

merge()

Now every row contains

Customer
Order
Payment
Purchase Date

all together.

Day 7 – Create Cohort Month

For every customer  i found

First Purchase Month

Example

Customer A

Jan 2018
Feb 2018
Apr 2018

Cohort Month

Jan 2018

This never changes.

Saved dataset for Week 2.

Week 2 – Cohort Retention Analysis

This week answers

Do customers come back after their first purchase?

Day 8

Calculated

First Purchase Month

for every customer.

Merged it into the orders table.

Every order now has

Purchase Month
Cohort Month
Day 9 – Cohort Index

Calculated

Purchase Month - Cohort Month

Example

Customer first bought

January

Bought again

March

Cohort Index

2

Meaning

Returned after 2 months.

Day 10 – Retention Matrix

Grouped data by

Cohort Month
Cohort Index

Counted

Unique Customers

Created Pivot Table

Example

Cohort	Month0	Month1	Month2
Jan	120	45	30
Feb	95	38	21

This is the Retention Matrix.

Day 11 – Retention Percentage

Converted counts into percentages.

Example

120 customers started

45 came back

Retention

45/120 ×100
=37.5%

Much easier to compare.

Day 12

Handled missing values

NaN → 0

Now the matrix is ready for visualization.

Day 13 – Business Insights

Studied

Best performing cohorts
Worst cohorts
Average retention

Example

January customers are more loyal than March customers.
Day 14

Exported

Retention Matrix
Retention %

as CSV.

Ready for Power BI.

Week 3 – Customer Lifetime Value (CLTV)

Now  i measure

How valuable is each customer?

Day 15 – Customer Purchase Analysis

Calculated

Total Orders

Example

Customer A

5 orders

Total Revenue

$1,250

Average Order Value

Formula

Revenue
---------
Orders

Example

$1250 /5

=$250
Day 16 – Purchase Frequency

Calculated

How often customers buy.

Example

Customer A

5 purchases

Customer B

1 purchase

Classified

Repeat Customers
One-time Customers
Day 17 – Customer Lifetime Value (CLTV)

Used

Revenue
Purchase Frequency

to estimate

Customer Lifetime Value

Meaning

How much money a customer is expected to generate.

Example

Customer A

CLTV
$900
Day 18 – Customer Segmentation

Created customer groups.

Example

Premium

CLTV > $1000

High

$500-$1000

Medium

$200-$500

Low

Below $200

Useful for targeted marketing.

Day 19 – Business Insights

Found

Top customers
Average CLTV
Highest CLTV
Lowest CLTV

Example

Top 10 customers contribute 30% of revenue.
Day 20

Validated the dataset.

Exported

cltv_dataset.csv

for Power BI.

Day 21

Checked

Missing values
Summary statistics
Data quality

Finished CLTV analysis.

Week 4 – Power BI Dashboard

Now  i create dashboards.

Day 22

Imported datasets into Power BI.

Created relationships.

Example

Customers

↓

Orders

↓

Payments
Day 23

Designed dashboard

Added

Navigation
Colors
La it
Day 24

Built Executive Dashboard.

Included

Total Revenue
Total Customers
Total Orders
Average CLTV
KPIs
Filters
Day 25

Created

Customer Cohort Dashboard

Included

Retention Heatmap
Cohort Trends
CLTV Charts
Customer Segments
Day 26

Added

Slicers
Buttons
Bookmarks
DAX Measures

Made dashboard interactive.

Day 27

Optimized

Faster loading
Better alignment
Better colors
Improved visuals
Day 28

Completed the project.

Final Power BI Dashboard
Documentation
GitHub Repository
Portfolio-ready project
Final Deliverables
