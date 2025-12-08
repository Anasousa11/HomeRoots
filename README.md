
# 🌿 HomeRoots – Homeschool Planner & Progress Tracker

HomeRoots is a full-stack Django web application designed to help homeschooling families manage lessons, track progress, organise students, and simplify daily planning.  
This project was created as part of my Backend Development Milestone, but it is also inspired by my personal experience homeschooling my children.

---

## 🌱 Personal Motivation

I am a mother of three — a 1-year-old boy, a 4-year-old girl, and a 5-year-old boy — and starting the homeschooling journey was overwhelming. I constantly searched for lesson templates, trackers, and organisational tools, but everything was scattered across multiple websites.

I created **HomeRoots** as a single place where parents can:

- Plan lessons  
- Track student progress  
- Organise multiple children at different levels  
- View overall grades and improvement  
- Keep everything structured and reliable  

In the future, I would like to expand HomeRoots to include printable worksheets and a complete homeschool resource package.

---

# ✨ Features

### 👧 Student Management
- Create, edit, delete student profiles  
- Upload profile images  
- View student dashboards  

### 📘 Lesson Planner
- Add, edit, delete lessons  
- View a lesson dashboard  
- Assign lessons to students  

### 📊 Progress Tracking
- Mark lessons as completed  
- Add grades (0–100)  
- Automatic overall grade calculation  
- Line chart visualising student progress  

### 📨 Contact Form
- Styled contact page  
- Form submits messages  
- Currently uses Django console backend  

### 🎨 User Interface
- Soft green visual theme  
- Rounded cards and modern layout  
- Fully responsive  
- Clean typography  

---

# 🛠 Technologies Used

- **Python 3 / Django 5**  
- **SQLite3**  
- **HTML / CSS / Bootstrap 5**  
- **Chart.js**  
- **Google Fonts**  
- **Django Messages Framework**  
- **Django Class-Based Views**  
- **AI-generated images from DeepAI**  

---

# 🗂 Information Architecture

---

# 🗃 Database Schema

HomeRoots uses a relational database to manage students, lessons, and progress records. The data model reflects homeschooling relationships in real life and supports full CRUD functionality.

---

## 📌 Student Model
Stores each students information.

**Fields:**
- first_name  
- last_name  
- date_of_birth  
- profile_image  
- created_at  

Each student can have multiple lessons linked to them to then show progress.

---

## 📌 Lesson Model
Stores lesson details.

**Fields:**
- title  
- subject  
- description  
- created_at  

Each lesson can be assigned to multiple students through the progress page.

---

## 📌 LessonProgress Model
Acts as a **junction table** between Students and Lessons.

**Fields:**
- student (ForeignKey)
- lesson (ForeignKey)
- status (Pending / Completed)
- grade (0–100)
- updated_at  

---

## 🔗 Relationships Summary

- One **Student** → Many **LessonProgress** records  
- One **Lesson** → Many **LessonProgress** records  
- **LessonProgress** links both Students and Lessons together  

This structure allows user to track lessons completed and grades for multiple students.

---

# 📸 Screenshots


### **Homepage**
![home](https://github.com/user-attachments/assets/5fd9a5a4-bbf3-43c8-98af-e4b85507d642)


### **Students Dashboard**
![students](https://github.com/user-attachments/assets/1799bb99-2b3c-4ff2-95b9-4df4d1c987dc)


### **Lessons Dashboard**
![lessons](https://github.com/user-attachments/assets/5e11da6b-9a03-478a-abd3-613518b2b6d0)


### **Progress Tracker**
![progress](https://github.com/user-attachments/assets/9d3e302c-d052-41e9-9763-9fd2af693d63)


### **Contact Page**
![contact](https://github.com/user-attachments/assets/2182afa3-d0c6-43cd-a100-957d5504dec6)


---

# 🧪 Testing

All testing was carried out manually to verify that the applications features functions as expected.

---

## ✅ Student Management

| Test | Result |
|------|--------|
| Add student | Pass |
| Edit student | Pass |
| Delete student | Pass |
| Required field validation | Pass |
| Profile image upload | Pass |
| Dashboard display | Pass |

---

## ✅ Lesson Management

| Test | Result |
|------|--------|
| Create lesson | Pass |
| Edit lesson | Pass |
| Delete lesson | Pass |
| Assign lesson to student | Pass |
| Lesson dashboard view | Pass |

---

## ✅ Progress Tracking System

| Test | Result |
|------|--------|
| Assign lesson to student | Pass |
| Mark lesson as completed | Pass |
| Save grade (0–100) | Pass |
| Grade displayed correctly | Pass |
| Chart updates dynamically | Pass |

---

## ✅ Contact Form

| Test | Result |
|------|--------|
| Empty fields validation | Pass |
| Valid submission | Pass |
| Success message displayed | Pass |
| Console receives message | Pass |

---

## ✅ Navigation & UI

| Test | Result |
|------|--------|
| Navbar links | Pass |
| Breadcrumb navigation | Pass |
| No broken links | Pass |
| Clean page transitions | Pass |

- Although several minor design and configuration issues were discovered during testing, no major bugs remain in the deployed version.

### ✅ Lighthouse Testing

Lighthouse testing was done using Chrome DevTools on the deployed Heroku site.

#### Results:
- **Performance:** Not fully calculated(Performance limitations were due to large hero image loading and live server response time on Heroku.)
- **Accessibility:** 88
- **Best Practices:** 100
- **SEO:** 90

Screenshots of these results are included below as evidence.<img width="1920" height="1080" alt="lighthouse-results-homeroots" src="https://github.com/user-attachments/assets/e6db2c23-4b4c-4e0a-b234-12629f9a90e7" />

---
### ✅ Bugs & Fixes

During development, a number of issues were found and resolved, including:

- Static files not loading correctly on Heroku  
- Missing database tables due to migration issues  
- Broken links between pages  
- Image upload issues  

All bugs were fixed before final deployment.

# 📱 Responsive Testing

Due to Iframe embedding protection being enabled, all responsive testing was completed using **Chrome Browser Developer Tools** to simulate real-world screen sizes and devices.

The following viewports were tested:

- Mobile (iPhone SE / iPhone 12)
- Tablet (iPad)
- Desktop (1080p and above)
- Landscape and portrait orientations

---
## 📸 Responsive Testing Screenshots (Browser DevTools)

- Homepage – Mobile View  
<img width="300" alt="home_mobile" src="https://github.com/user-attachments/assets/30618e72-a97e-48aa-bd4d-cf7f3894b77c" />

- Students Dashboard – Tablet View  
<img width="420" alt="student_tablet" src="https://github.com/user-attachments/assets/369b4b14-1685-4f23-a56f-1177bbc8c3c9" />

- Lessons Dashboard – Mobile View  
<img width="300" alt="lesson_mobile" src="https://github.com/user-attachments/assets/457349b6-2624-4e4c-95ed-7b0f14c790b6" />

- Progress Chart – Small Screen Landscape  
<img width="500" alt="progress_ss" src="https://github.com/user-attachments/assets/19e54ee8-2413-4c28-87fa-1882ec568119" />




### 🔍 Validator Testing
#### HTML Validation

Tested using W3C HTML Validator
![html_validator](https://github.com/user-attachments/assets/79f5492e-bc92-45c4-bc48-a40b7b2276a4)

✔ No major structural errors


#### CSS Validation

Tested using W3C CSS Jigsaw
![css_validator](https://github.com/user-attachments/assets/59d77a19-2885-4413-a967-cde1183c3e23)

✔ Pass – no invalid rules

#### ✅ Python (PEP8) Validation

All custom Python files in this project were checked using `pycodestyle` to make sure the code follows PEP8 standards.

The following command was used to run the initial test:

python -m pycodestyle .

To ensure only the project’s own files were checked this command was then used:

python -m pycodestyle . --exclude=.venv

Results showed that most of the warnings were related to formatting only, such as:

- Lines being slightly longer than the recommended 79 characters  
- Spacing between functions and classes  
- Import placement in the settings file  
- Minor whitespace formatting  

These are all **styling issues only** and do **not affect how the project works**.  
All main features of the application were tested and confirmed to work as expected.

Overall, the Python code has been validated and is functioning correctly.

---
# 📁 Folder Pathway

<img width="216" height="400" alt="directory" src="https://github.com/user-attachments/assets/43b794e4-e641-4074-87af-bb9e620f2b22" />



# 📝 Project Planning
Wireframes


# 🧭 User Stories

- As a homeschooling parent, I want to add my children so their learning can be organised individually.  
- As a parent, I want to plan and save lessons for future use.  
- As a parent, I want to assign lessons and track when they’re completed.  
- As a parent, I want to give grades and see improvement visually.  
- As a user, I want to contact the site owner easily through a simple form.  

---
---

# 🚀 Deployment

HomeRoots was deployed using Heroku so that it can be accessed live on the web.  
The live site can be found here:

🔗 Live Site: https://homeroot-e8a349dd181e.herokuapp.com/

---

### Running the Project Locally

To run this project on your own computer, follow the steps below:

1. Clone the repository:

git clone https://github.com/yourusername/your-repo-name.git

2. Navigate into the project folder:

cd your-repo-name

3. Create and activate a virtual environment:

python -m venv venv  

Windows:
venv\Scripts\activate  

Mac/Linux:
source venv/bin/activate  

4. Install the project dependencies:

pip install -r requirements.txt  

5. Create a `.env` file and add the following values:

SECRET_KEY=your_secret_key  
DEBUG=True  
DATABASE_URL=sqlite:///db.sqlite3  

6. Apply the database migrations:

python manage.py migrate  

7. Create a superuser for the admin panel:

python manage.py createsuperuser  

8. Run the development server:

python manage.py runserver  

9. Open the project in your browser:

http://127.0.0.1:8000/

---

### Heroku Deployment

The following steps were used to deploy the project to Heroku:

1. A new Heroku app was created.
2. The following Config Vars were added:
   - SECRET_KEY  
   - DATABASE_URL  
3. Production dependencies were installed:
   - gunicorn  
   - dj-database-url  
   - psycopg2-binary  
   - whitenoise  
4. A `Procfile` was created to run the application.
5. Static files were collected using:

python manage.py collectstatic  

6. The project was pushed to Heroku using Git.
7. Database migrations were run on Heroku.

Once completed, the site became fully accessible online.

---

# 📝 Assessment Criteria Alignment

✔ Full CRUD functionality  
✔ Relational database design  
✔ Secure cloud deployment  
✔ Django framework conventions  
✔ Responsive front-end  
✔ Manual testing documentation  
✔ Version control using GitHub  
✔ Security practices applied  
✔ Professional documentation  

# 📚 Credits & Sources

### Documentation
- Django Documentation – https://docs.djangoproject.com/  
- Bootstrap Documentation – https://getbootstrap.com/  
- Chart.js Documentation – https://www.chartjs.org/docs/latest/  

### Other Resources
- Google Fonts – https://fonts.google.com  
- Bootstrap Icons – https://icons.getbootstrap.com  

### Image Sources
- AI-generated illustrations using DeepAI
- AI-generated support image used on Contact Page  

### Technical Support
- StackOverflow (debugging reference) – https://stackoverflow.com/  


---

# 🌟 Future Improvements

I hope to extend this app with:

- Printable worksheets for homeschool subjects  
- A weekly planner PDF generator  
- Student login system  
- Parent dashboard  
- Drag-and-drop lesson scheduler  
- Cloud storage for worksheets  
- Curriculum templates for different ages  

---


# 💬 Reflection

Building HomeRoots was one of the most challenging but rewarding projects I have worked on so far. Balancing this project alongside parenting three young children made time management extremely difficult, but it also reinforced why this project mattered so much to me personally.

During development, I faced several serious delays and was granted an official extension to complete the project. One of the biggest obstacles was ongoing technical issues with my original laptop, which significantly slowed my progress. After researching the most suitable laptop for programming and development, I made the decision to purchase a new one on the official submission date so that I could finally complete, deploy, and submit the project properly.

Although these challenges caused unavoidable delays, I remained committed to finishing HomeRoots to the best of my ability. Completing this project under such difficult circumstances has made the achievement even more meaningful to me.

This project helped me fully understand how a full-stack web application works — from database modelling and CRUD logic to templates, deployment, and debugging live errors. Some issues took forever to solve, but working through them built my confidence and embedded knowledge that will help me in my web development career.

HomeRoots represents both my technical growth and a real solution to a real need in my own life. The skills I’ve gained from this project will strongly influence how I approach development work in the future.




# 👩‍💻 Author

Ana Samanda Dicha De Sousa
Web Application Development – Level 5 Diploma
GitHub: https://github.com/Anasousa11








