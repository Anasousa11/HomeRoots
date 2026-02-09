
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
- Add, edit, delete student profiles
- Upload profile pictures
- See a dashboard of all students

### 📘 Lesson Planner
- Create lessons with subjects, levels, objectives
- Set duration and materials needed
- Assign lessons to students
- Edit or delete lessons

### 📊 Progress Tracking
- Mark lessons as completed
- Record grades (0-100 scale)
- See overall grade automatically calculated
- View progress as a chart

### 📨 Contact
- Simple contact form on the site
- Messages show up in the console (for now)

### 🎨 User Interface
- Soft green visual theme  
- Rounded cards and modern layout  
- Fully responsive  
- Clean typography  

---

# 🛠 Tech Stack

- **Python 3 & Django** - the main framework
- **SQLite** locally, **PostgreSQL** on Heroku
- **HTML, CSS, Bootstrap 5** - for the frontend
- **Chart.js** - to draw the progress charts
- **Heroku** - where the app is deployed
- **Git & GitHub** - version control

# 🗃 Database Schema

My app uses three main tables to organize everything:

## How the Data Connects

**Students** → each student can take many lessons  
**Lessons** → each lesson can be assigned to many students  
**LessonProgress** → this tracks which lessons each student has completed and their grades

The `LessonProgress` table is the bridge between Students and Lessons - it keeps a record of every lesson a student has done, whether they completed it, and what grade they got.

## The Three Models

### Student
- student ID, first name, last name, date of birth, gender
- notes, profile image, created date

### Lesson
- lesson ID, title, subject, level (Elementary/Middle/High)
- description, learning objectives, materials needed
- duration, scheduled date, created/updated dates

### LessonProgress
- progress ID, student ID, lesson ID
- completed (yes/no), grade (0-100), completion date
- ensures each student can only have one record per lesson

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

All testing was carried out manually to verify that the application functions as expected across all core features.

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

- While several minor layout and configuration issues were discovered during testing, no major functional bugs remain in the deployed version.

---

# 📱 Responsive Testing

All responsive testing was completed using **Chrome Browser Developer Tools** to simulate real-world screen sizes and devices.

The following viewports were tested:

- Mobile (iPhone SE / iPhone 12)
- Tablet (iPad)
- Desktop (1080p and above)
- Landscape and portrait orientations

---

## 📸 Responsive Testing Screenshots (Browser DevTools)



- Homepage – Mobile View  
- Students Dashboard – Tablet View  
- Lessons Dashboard – Mobile View  
- Progress Chart – Small Screen Landscape  




### 🔍 Validator Testing
#### HTML Validation

Tested using W3C HTML Validator

✔ No major structural errors
✔ Minor warnings ignored (Bootstrap-related)

#### CSS Validation

Tested using W3C CSS Jigsaw

✔ Pass – no invalid rules

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

HomeRoots was deployed using **Heroku** to demonstrate a complete real-world development workflow from local development to live cloud hosting. This ensured the project met the requirement for deploying a full-stack web application to a production environment and verifying that it matched the development version.

The deployment process helped me understand real production workflows used in industry including environment configuration, version control, and secure handling of sensitive settings.

---

## ✅ Pre-Deployment Setup

Before deployment, the following production configurations were completed:

- `DEBUG` set to `False`
- `ALLOWED_HOSTS` updated to include the Heroku app domain  
- Static file handling configured using **WhiteNoise**  
- **Gunicorn** added as the production web server  
- `requirements.txt`, `Procfile`, and `runtime.txt` created  
- Environment variables used to protect sensitive settings  
- Final code reviewed to ensure:  
  - No commented-out production code  
  - No broken internal links  
  - No secret keys pushed to GitHub  

---

## ✅ Step-by-Step Deployment Process (Heroku)

1. **Login to Heroku**

- heroku login

2. **Create the Heroku Application**


- heroku create homeroot

3. **Set Python Buildpack**

- heroku buildpacks:set heroku/python

4. **Push the Project to Heroku**


- git add .
- git commit -m "Initial production deployment"
- git push heroku main

5. **Apply Database Migrations**

- heroku run python manage.py migrate

6. **Collect Static Files**


- heroku run python manage.py collectstatic

7. **Create Superuser (Admin Access)**


- heroku run python manage.py createsuperuser
---
After these steps, the application was successfully deployed and rendered live on the Heroku cloud platform.
---
## 🌍 Live Deployment Link
The deployed version of HomeRoots is available here:

🔗 https://homeroot-e8a349dd181e.herokuapp.com/

The deployed site was tested to ensure it matched the development environment in both functionality and design.

---

# 🔒 Security

This time around, I made sure to handle sensitive information properly:

## Secret Keys & Environment Variables

I learned the hard way that putting secret keys in code is a security risk. Now:
- The `DJANGO_SECRET_KEY` is read from environment variables only - never stored in the code
- I created a `.env.example` file so anyone cloning the project knows what variables to set up
- The `.env` file is in `.gitignore` so it never gets pushed to GitHub
- On Heroku, I set the secret key in the Config Vars dashboard

## Protected Database Credentials

- Database URL and credentials are loaded from environment variables
- They're never hardcoded or committed to the repository
- Locally uses SQLite for development; production uses PostgreSQL on Heroku with encrypted credentials

## User Authentication

I added login/logout functionality so:
- Only authenticated users can create, edit, or delete students and lessons
- Users have to register and log in to use the app
- All password-sensitive operations use Django's built-in password hashing

## What's Working

- DEBUG is set to False in production (prevents sensitive error details from showing)
- CSRF token protection on all forms
- Strong password validation for new accounts
- Session-based authentication

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

This project helped me fully understand how a full-stack web application works — from database modelling and CRUD logic to templates, deployment, and debugging live errors. Some issues initially felt impossible to solve, but working through them built my confidence and strengthened my problem-solving skills.

HomeRoots represents both my technical growth and a real solution to a real need in my own life. The skills I’ve gained from this project will strongly influence how I approach future development work.




# 👩‍💻 Author

Ana Samanda Dicha De Sousa
Web Application Development – Level 5 Diploma
GitHub: https://github.com/Anasousa11



