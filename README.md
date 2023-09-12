# AutomatedApllicationFormFilling

## Abstract
The project aims to automate the process of filling out job application forms using web scraping and automation techniques. The application collects data from users and then uses Selenium libraries in Python to extract job data from a CSV file and fill out the job application forms on various job websites. The program can handle text inputs, radio buttons, dropdowns, and date fields. It also ensures that all mandatory fields are filled out before moving to the next page. The project provides a faster and efficient way to apply for multiple jobs without spending hours filling out the same information repeatedly.

## SYSTEM ARCHITECTURE

<img width="726" alt="Screen Shot 2023-05-15 at 11 36 35 AM" src="https://github.com/AthiraNirmal/AutomatedApllicationFormFilling/assets/63495996/d46b8ca5-18c3-4ec8-9a08-810cb258562c">

## DATA COLLECTION
The data collection for this project is done through a web UI form using Flask.

*To ensure that each user has a unique record, the system assigns a unique username and email to each application. If a user tries to enter the same username and email with the application details, the system will throw a warning page.*

For returning users, only the username and job URL are required to be entered, and the system will retrieve their previously entered data. This feature helps users to quickly apply for multiple jobs without having to re-enter their personal details every time. The data collection process is made efficient and user-friendly through the use of various Python libraries such as Selenium. These libraries enable the automation of the data entry process, making it faster and more accurate. Overall, the data collection process is streamlined and ensures that accurate and consistent data is collected for each job application.


<img width="1429" alt="Screen Shot 2023-05-13 at 11 54 04 AM" src="https://github.com/AthiraNirmal/AutomatedApllicationFormFilling/assets/63495996/31c22f54-b201-4ace-8480-f132411c9447">
