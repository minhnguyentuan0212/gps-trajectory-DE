# Analyzing User Interests Through GPS Stops

This project aims to analyze user interests by processing and visualizing GPS data. Utilizing a comprehensive dataset collected from the Geolife project by Microsoft Research Asia, we developed a system to extract meaningful insights about user behavior and movement patterns.

## Introduction

The core of our analysis revolves around GPS data, which represents users' trajectories over time. Through data engineering techniques, we process this data to identify significant locations (StayPoints), understand user movement patterns, and derive insights into the most frequented places and preferred modes of transportation.

## Dataset Overview

The dataset comprises GPS trajectories collected from 182 users over five years, containing over 17,621 trajectories spanning 1,292,951 kilometers. The trajectories are detailed, with data points including latitude, longitude, and altitude.

## Technologies Used

- **Apache Hadoop & HDFS**: For scalable storage and processing of large-scale GPS data.
- **Apache Spark**: Employed for efficient data processing and analysis.
- **MySQL**: Utilized for structured data storage after processing.
- **PowerBI**: For visualizing the GPS data and analytical results.

## Problem Solving Approach

1. **Data Storage System Construction**: Leveraging Hadoop for raw data storage and Spark for data transformation.
2. **User Data Statistics**: Analysis of user data to identify trends and patterns.
3. **Clustering GPS Locations**: Using the DBSCAN algorithm to cluster significant locations from GPS data.
4. **Data Visualization**: Employing PowerBI for visual representation of the data and insights.

## Installation & Usage

Explain how to install and run your project. This should include steps to set up the environment, install necessary dependencies, and run the application.

## Results & Conclusion

Briefly describe the findings of your analysis. Highlight interesting patterns, user behavior insights, and any conclusions drawn from the data visualization.

## Challenges

Discuss any significant challenges encountered during the project and how they were addressed. This could include issues with data size, tool selection, or approach to problem-solving.

## Project Significance

Summarize the importance of this project and its potential applications or implications for real-world problems.

## Contributing

Provide guidelines for how others can contribute to the project. This could include instructions for submitting issues, pull requests, and contact information for the project team.

## License

Specify the license under which your project is released.

## Acknowledgments

Mention any individuals, organizations, or resources that were instrumental in the success of your project.

---

This project was developed by students of the Ho Chi Minh City University of Technology, Faculty of Computer Science and Engineering, as part of a Data Engineering course.

**Instructors**: Dr. Phan Trong Nhan

**Contributors**: Trinh Duc Manh, Vo Duc Minh, Nguyen Tuan Minh
