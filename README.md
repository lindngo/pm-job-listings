# Product Management (PM) Job Listings Analysis

## Overview
As I have been job searching for product positions, I was curious how I can better optimize my resume to fit the keywords, phrases, and qualifications that companies are looking for. I began parsing through PM listings on LinkedIn to compile an Excel sheet of position names, job descriptions, and qualifications. I mainly focused on entry level PM roles based in Seattle, WA. With Python, I used pandas and sklearn to perform K-Means and Agglomerative Clustering to better understand what common similarities stretch across these listings. 

## Dataset
https://github.com/lindngo/product-management/blob/main/jds.csv

## Dataset Factors
- Position Name: Title of the job
- Job Post Link: Direct job posting link on the company's career page
- Job Description: Overview of responsibilities and duties that the incoming PM will take on
- Qualifications/Desired Skills: Target skillset that the company is looking for in a qualified PM candidate

## Conclusions

![image](https://user-images.githubusercontent.com/63205351/233500344-34dbe17e-fa9f-41d6-86cf-ddbdf3ebee4d.png)

My first line of action was to tackle the job descriptions. Choosing 6 clusters for my data, I generated code that parsed each of the job descriptions and group similar terms together. After sorting it from descending similarity in each cluster, I retrieved the top 5 terms of each cluster, as pictured above. With this, I interpreted the following:

- Cluster 0: PMs are responsible for product development that meets existing market trend needs.
- Cluster 1: The PM must be able to understand and communicate clearly to their team, users, and stakeholders.
- Cluster 2: PMs should have a drive to develop solutions to customer issues.
- Cluster 3: It is important that PMs do well in team environments that work with data and products.
- Cluster 4: For this cluster, it seemed to be more company vision focused, which I chose to move forward as it was not a direct relation to the PM responsibilties.
- Cluster 5: A PM should be able to help the business drive their sales with their product solutions.

![image](https://user-images.githubusercontent.com/63205351/233500363-3bf8f102-d3da-4522-8a5f-4b54d3759f1a.png)

For the qualifications, I followed the same steps that I had executed for job descriptions. With the 6 clusters generated, I interpreted the following:
- Cluster 0: Companies value applicants with experience related to analytics.
- Cluster 1: Because this cluster was speaking about company location/relocation, I chose to move forward.
- Cluster 2: A strong applicant should have strong interpersonal skills and business knowledge.
- Cluster 3: They should also have product/project management experience, as well as working on a team.
- Cluster 4: Having experience working in a start-up environment is a plus, especially if the candidate can demonstrate their product success.
- Cluster 5: I believe this cluster is focusing on students/recent graduates, hence the terms "majors" and "gpa".


For next steps, I plan to work on collecting more data for the jds.csv, as the file only contains 10 listings currently.
