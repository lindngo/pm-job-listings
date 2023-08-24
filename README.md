# Product Management (PM) Job Listings Analysis

## Overview
Over the past few months, I've been searching for and applying to product positions. During this, I was curious on how I can better optimize my resume to fit the keywords, phrases, and qualifications that companies are looking for. I sifted through PM listings on LinkedIn to compile an Excel sheet of position names, job descriptions, and qualifications. I mainly focused on entry level PM roles. With Python, I used pandas and sklearn to perform k-means and agglomerative clustering to better understand what similarities are shared across these listings. 

## Dataset
https://github.com/lindngo/product-management/blob/main/jds.csv

## Dataset Variables
- Position Name: Title of the job
- Job Post Link: Job posting link on the company's career page
- Job Description: Overview of responsibilities and duties
- Qualifications/Desired Skills: Target skillset that the company is looking for in a qualified PM candidate

## Conclusions

![image](https://user-images.githubusercontent.com/63205351/233500344-34dbe17e-fa9f-41d6-86cf-ddbdf3ebee4d.png)

My first step was to examine the job descriptions. Choosing 6 clusters, I wrote a code to review each of the job descriptions and group similar terms together. After sorting from most similar to least similar in each cluster, I retrieved the top terms of each cluster, as pictured above. With this, I interpreted the following:

- Cluster 0: PMs are responsible for product development that meet existing market trend needs.
- Cluster 1: The PM must be able to understand and communicate clearly to their team, users, and stakeholders.
- Cluster 2: PMs are driven to develop fitting solutions to customer issues.
- Cluster 3: It is important that PMs do well in team environments that work with data and products.
- Cluster 4: Since this cluster seemed more company vision focused, I didn't focus much on this information.
- Cluster 5: A PM are well equipped to help the business drive their sales with their product solutions.

![image](https://user-images.githubusercontent.com/63205351/233500363-3bf8f102-d3da-4522-8a5f-4b54d3759f1a.png)

For the qualifications, I followed the same steps that I had executed for job descriptions. With the 6 clusters generated, I interpreted the following:
- Cluster 0: Companies value applicants with experience related to analytics.
- Cluster 1: Since this cluster talked mainly about relocation and not about specific qualifications, I didn't focus much on this information.
- Cluster 2: A strong applicant has strong interpersonal skills and business knowledge.
- Cluster 3: They also have product/project management and team collaboration experience.
- Cluster 4: Having experience in a start-up environment is a plus, especially if the candidate can demonstrate their product success.
- Cluster 5: This cluster focuses on students/recent graduates, hence the terms "majors" and "gpa".

For future steps, I plan to work on collecting more data for the jds.csv to create even more accurate clusters.
