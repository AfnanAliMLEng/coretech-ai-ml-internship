# Task 06: Unsupervised Learning — Client Segmentation Using Clustering

## Intern Information

**Name:** Afnan Ali
**Education:** 2nd Year Information Technology Student
**City:** Kazi Ahmed, Sindh, Pakistan



# Project Overview

This project applies **Unsupervised Machine Learning** techniques to perform intelligent client segmentation for CoreTech Innovation. The objective is to identify hidden patterns within client data and group organizations with similar business characteristics. Such segmentation enables data-driven decision-making, targeted business strategies, and improved customer relationship management.

A realistic client dataset was created containing operational and financial indicators including workforce size, annual revenue, project activity, customer satisfaction, and relationship duration.



# Objectives

* Perform client segmentation using clustering techniques.
* Identify high-value and growth-potential clients.
* Compare K-Means and Hierarchical Clustering approaches.
* Generate actionable business insights from discovered clusters.
* Visualize cluster structures and relationships.



# Methodology

### Data Preparation

* Dataset Creation
* Feature Selection
* Data Standardization using StandardScaler

### Clustering Techniques

* K-Means Clustering
* Elbow Method for Optimal K Selection
* Agglomerative Hierarchical Clustering
* Dendrogram Analysis

### Visualization

* Revenue Distribution Analysis
* Elbow Curve
* K-Means Cluster Visualization
* Hierarchical Cluster Visualization



# Dataset Features

| Feature               | Description                  |
| --------------------- | ---------------------------- |
| Client_ID             | Unique client identifier     |
| Employees             | Total workforce size         |
| Annual_Revenue        | Annual business revenue      |
| Projects_Completed    | Number of completed projects |
| Years_With_Company    | Client relationship duration |
| Customer_Satisfaction | Satisfaction score           |



# Business Insights

The clustering process successfully identified multiple client segments representing distinct business profiles:

### Emerging Clients

Small organizations with limited revenue and project activity that require growth-focused solutions.

### Growth-Oriented Clients

Medium-scale businesses demonstrating consistent performance and expansion potential.

### Enterprise Clients

Large organizations with substantial revenue contribution and strategic business importance.

### Premium Clients

High-value customers with strong engagement, long-term relationships, and significant business impact.

These insights can support personalized service offerings, customer retention strategies, and resource optimization.



# Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-Learn
* SciPy
* Google Colab
* GitHub



# Repository Structure

```text
Task_06_Clustering/
│
├── task_06_clustering.ipynb
├── coretech_clients_dataset.csv
├── clustered_clients.csv
├── elbow_method.png
├── kmeans_clusters.png
├── hierarchical_dendrogram.png
├── hierarchical_clusters.png
└── README.md
```



# Key Outcomes

* Developed a complete client segmentation pipeline.
* Applied multiple clustering algorithms on business data.
* Evaluated cluster quality using the Elbow Method.
* Generated professional visualizations for cluster analysis.
* Produced actionable business intelligence from unsupervised learning techniques.



# Conclusion

This project demonstrates the practical application of clustering algorithms for customer segmentation and business analytics. By leveraging K-Means and Hierarchical Clustering, meaningful client groups were identified, enabling deeper understanding of customer behavior and supporting strategic business decision-making through data-driven insights.

