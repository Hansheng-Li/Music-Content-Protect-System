
# Music Content Protection System (MCPS)

The Music Content Protection System (MCPS) is a comprehensive software solution designed to identify, monitor, and protect copyrighted music tracks from unauthorized access and distribution across the internet. MCPS employs the latest in audio fingerprinting technology, machine learning models, and web crawling techniques to safeguard the interests of artists and copyright holders.

## 1. Content Monitoring and Identification Module
- **Functionality**: Automatically monitors music content on the internet, utilizing audio fingerprinting technology to identify UMG copyrighted content.
- **Technology Stack**: Python3, Audio fingerprinting libraries (e.g., AcoustID), Web crawling technologies.

## 2. Data Management and Analysis Module
- **Functionality**: Stores information about identified unauthorized content, analyzes trends and origins of distribution, providing data support for subsequent legal actions.
- **Technology Stack**: PostgreSQL database, Python3 (Data analysis libraries such as Pandas and NumPy).

## 3. Automated Copyright Infringement Handling Module
- **Functionality**: Automatically sends copyright notices, interfaces with major platforms to facilitate the rapid takedown of infringing content.
- **Technology Stack**: Python3, RESTful API development and integration.

## 4. Security and Encryption Module
- **Functionality**: Protects the MCPS system from cyber attacks and encrypts sensitive data to ensure safety.
- **Technology Stack**: Security frameworks (e.g., OWASP recommended practices), SSL encryption.

## 5. User Interface
- **Functionality**: Provides an operational interface for UMG internal users to view reports, analyze results, and manage copyright notices.
- **Technology Stack**: Front-end development with React or Vue, Rapid prototyping with Retool.

## Detailed Process
- **Audio Fingerprinting**: Utilizing cutting-edge algorithms, this technology identifies copyrighted music tracks with high precision, even when they have been modified or quality-compromised. Prominent platforms like Soundhound, Shazam, ACRCloud, and AudD excel in this domain. ACRCloud and AudD stand out for their extensive audio fingerprint libraries, such as AcoustID, enabling efficient music recognition across varied alterations. This innovation is crucial for ensuring copyright compliance and accurate music identification in digital content management.

- **Content Monitoring**: The system regularly uses web crawling technologies to traverse music publishing platforms and social media on the internet, automatically identifying UMG's copyrighted music through audio fingerprinting technology.
- **Data Collection and Analysis**: Identified infringement information is stored in the database. The system automatically analyzes the distribution paths, hotspot regions, and high-risk platforms of the infringing content.
- **Automated Processing**: Based on the analysis results, the system automatically generates copyright infringement notices and interfaces with the infringing content publishing platforms via API to request the takedown of the content.
- **Legal Support**: For complex cases that are difficult to handle automatically, the system provides detailed data reports and analysis results to assist the legal team in taking further action.
- **System Security**: Employs the latest security technologies and encryption methods to protect system data, conducts regular security audits to ensure the system is protected from external attacks.
- **User Interaction**: Internal users can access the system through a user-friendly interface to view real-time data, reports, and operate various functions provided by the system. 

## Tiktok Project Overview 

This project is a web application that can scrape video data from TikTok based on specific keywords and display this data on a frontend page. Users can input a keyword (e.g., "Taylor Swift") into an input box on the frontend page to search for videos on TikTok. The application will then display information such as the video title, description, publication date, uploader username, and the number of comments. This data will be stored in a local PostgreSQL database for future use.

## Tech Stack

- Frontend: React + Bootstrap (including JavaScript, HTML5, CSS3)
- Backend: Django (including Python3, PostgreSQL)
- Data Transfer: RESTful API

## Environment Setup

1. Install Node.js and npm.
2. Install Python3.
3. Install PostgreSQL.

## Project Setup

### Database Setup

First, ensure that your local PostgreSQL database is running correctly and create a new database for this project.

### Backend Setup

1. Clone the repository to your local machine.

2. Navigate to the project directory, create a virtual environment, and activate it:

   ```bash
   python -m venv vsvenv
   source vsvenv/Scripts/activate  # On Windows
   source vsvenv/bin/activate  # On macOS/Linux
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Perform database migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. (Optional) If you wish to access the Django admin panel, you can create a superuser account:

   ```bash
   python manage.py createsuperuser
   ```

6. Start the Django server:

   ```bash
   python manage.py runserver
   ```

### Frontend Setup

1. Navigate to the frontend project directory.

2. Install dependencies:

   ```bash
   npm install
   ```

3. Start the frontend project:

   ```bash
   npm start
   ```

At this point, your frontend application should be running in your browser and be able to communicate with the backend.

## Instructions for Use

- Input a keyword (e.g., "Taylor Swift") into the input box on the frontend page and submit the search request.
- A table will be displayed below, listing the data for the top twelve videos from the TikTok search results, including the video's title, description, publication date, uploader username, and the number of comments.
- This data will be automatically stored in the PostgreSQL database.

## Notes

- Ensure that all necessary dependencies are installed in your environment and the database is correctly set up.
- Make sure the backend service is running before starting the frontend service.

Enjoy using the application!


## Contributing

Contributions to MCPS are welcome! Please read our [Contributing Guide](CONTRIBUTING.md) for more information on how to get involved.

## License

MCPS is licensed under the [Apache License 2.0](LICENSE). See the LICENSE file for more details.

## Contact

For any inquiries or support, please contact us.

## Acknowledgments

- Special thanks to the artists and content creators who inspire our work.
- Our partners and collaborators in the fight against copyright infringement.

## Study Materials
Udemy Video Course [Intro To PostgreSQL](https://iqbusiness.udemy.com/course/intro-to-postgresql-databases-with-pgadmin/learn/lecture/12154526#reviews) 

Educative Reading Course [Mastering PostgreSQL Databases: From Basics to Advanced](https://www.educative.io/courses/mastering-postgre-sql-databases-from-basics-to-advanced) 

Udemy Video Course [Web Scraping in Python Selenium, Scrapy + ChatGPT Prize 2024](https://iqbusiness.udemy.com/course/web-scraping-course-in-python-bs4-selenium-and-scrapy/learn/lecture/27782682#overview)

Educative Reading Course(CICD, Docker, Kubernetes, Jenkis, AWS) [DevOps for Developers](https://www.educative.io/path/devops-for-developers)

[Retool Doc](https://docs.retool.com/)

[Jira Project](https://lihansheng.atlassian.net/jira/software/projects/KAN/boards/1)

[OWASP Top 10](https://www.cloudflare.com/learning/security/threats/owasp-top-10/)

### Data Structures & Algorithms
[Problem rodemap](https://neetcode.io/roadmap)

[Problem Doc](https://programmercarl.com/%E6%95%B0%E7%BB%84%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%80.html)

Educative Reading Course [Grokking Modern System Design](https://www.educative.io/courses/grokking-modern-system-design-interview-for-engineers-managers)






