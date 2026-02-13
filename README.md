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

## 🔗 Live Site

- https://homeroot-e8a349dd181e.herokuapp.com/

---

## ✨ Features

### 👧 Student Management
- Create, edit, delete student profiles  
- Upload profile images  
- View student dashboards  

### 📘 Lesson Planner
- Add, edit, delete lessons  
- View a lesson dashboard  
- Assign lessons to students  

### 📊 Progress Tracking
- Assign lessons to students  
- Mark lessons as completed  
- Add grades (0–100)  
- Automatic overall grade calculation  
- Line chart visualising student progress  

### 📨 Contact Form
- Styled contact page  
- Form submits messages  
- Uses Django console email backend (messages appear in the terminal during development)

### 🎨 User Interface
- Soft green visual theme  
- Rounded cards and modern layout  
- Fully responsive  
- Clean typography  

---

## 🔐 Authentication & Route Protection (Resubmission Update)

This project includes **Login, Logout, and Registration**.

To protect user data and improve UX, **data-changing routes are restricted to authenticated users**:

- Student: add / edit / delete (LoginRequiredMixin)
- Lesson: add / edit / delete (LoginRequiredMixin)
- Progress actions: assign lesson / mark completed (login_required)
- Success + info messages provide consistent user feedback after actions

If a user is not logged in and tries to access a protected page, they will be redirected to the login screen.

---

## 🛠 Technologies Used

- Python 3 / Django 5  
- SQLite3  
- HTML / CSS / Bootstrap 5  
- Chart.js  
- Google Fonts  
- Django Messages Framework  
- Django Class-Based Views  
- AI-generated images from DeepAI  

---

## 🗃 Database Schema

HomeRoots uses a relational database to manage students, lessons, and progress records.  
The schema below matches the actual Django models.

### 📌 Student Model
Stores each student’s information.

**Fields**
- id (BigAutoField)
- first_name (CharField)
- last_name (CharField)
- dob (DateField, optional)
- gender (CharField, optional)
- notes (TextField, optional)
- profile_image (ImageField, optional)
- created_at (DateTimeField)

### 📌 Lesson Model
Stores lesson details.

**Fields**
- id (BigAutoField)
- title (CharField)
- subject (CharField)
- level (CharField)
- objectives (TextField)
- description (TextField)
- materials (TextField, optional)
- duration_minutes (IntegerField)
- lesson_date (DateField, optional)
- created_at (DateTimeField)
- updated_at (DateTimeField, optional)

### 📌 LessonProgress Model
Junction table linking Students and Lessons (progress + grading).

**Fields**
- id (BigAutoField)
- student (ForeignKey → Student)
- lesson (ForeignKey → Lesson)
- completed (BooleanField)
- completed_at (DateTimeField, optional)
- grade (IntegerField, optional)

### 🔗 Relationships Summary
- One Student → Many LessonProgress records  
- One Lesson → Many LessonProgress records  
- LessonProgress links both Students and Lessons together  

---

## 🗄 Entity Relationship Diagram (ERD)

The diagram below shows the relationship between Student, Lesson and LessonProgress models.

<img src="https://raw.githubusercontent.com/Anasousa11/HomeRoots/main/docs/erd.png" width="850" alt="HomeRoots ERD">

---

## 📸 Screenshots

### Homepage
![home](https://github.com/user-attachments/assets/5fd9a5a4-bbf3-43c8-98af-e4b85507d642)

### Students Dashboard
![students](https://github.com/user-attachments/assets/1799bb99-2b3c-4ff2-95b9-4df4d1c987dc)

### Lessons Dashboard
![lessons](https://github.com/user-attachments/assets/5e11da6b-9a03-478a-abd3-613518b2b6d0)

### Progress Tracker
![progress](https://github.com/user-attachments/assets/9d3e302c-d052-41e9-9763-9fd2af693d63)

### Contact Page
![contact](https://github.com/user-attachments/assets/2182afa3-d0c6-43cd-a100-957d5504dec6)

---

## 🧪 Testing

All testing was carried out manually to verify that the application’s features work as expected.  
Most testing was done late at night after my children were asleep, which helped me properly focus on each feature.

### ✅ Student Management

| Test | Result |
|------|--------|
| Add student | Pass |
| Edit student | Pass |
| Delete student | Pass |
| Required field validation | Pass |
| Profile image upload | Pass |
| Dashboard display | Pass |

### ✅ Lesson Management

| Test | Result |
|------|--------|
| Create lesson | Pass |
| Edit lesson | Pass |
| Delete lesson | Pass |
| Assign lesson to student | Pass |
| Lesson dashboard view | Pass |

### ✅ Progress Tracking System

| Test | Result |
|------|--------|
| Assign lesson to student | Pass |
| Mark lesson as completed | Pass |
| Save grade (0–100) | Pass |
| Grade displayed correctly | Pass |
| Chart updates dynamically | Pass |

### ✅ Contact Form

| Test | Result |
|------|--------|
| Empty fields validation | Pass |
| Valid submission | Pass |
| Success message displayed | Pass |
| Console receives message | Pass |

### ✅ Navigation & UI

| Test | Result |
|------|--------|
| Navbar links | Pass |
| Breadcrumb navigation | Pass |
| No broken links | Pass |
| Clean page transitions | Pass |

---

## ✅ Lighthouse Testing

Lighthouse testing was performed using Chrome DevTools on the deployed Heroku application.

**Results**
- **Performance:** 69  
- **Accessibility:** 88  
- **Best Practices:** 100  
- **SEO:** 90  

<img src="https://raw.githubusercontent.com/Anasousa11/HomeRoots/main/core/static/core/screenshots/lighthouse-results-homeroots.png" width="850" alt="Lighthouse results">

**Notes**
- Performance is mainly impacted by Heroku cold starts and image loading.
- Accessibility is strong thanks to semantic structure + form labels.
- Best Practices is 100 due to secure deployment configuration and safe handling of environment variables.
- SEO confirms a clean structure and responsive layout.

---

## ✅ Bugs & Fixes (Traceable)

| Bug / Issue | What was happening | Fix applied | Result |
|---|---|---|---|
| Static files not loading on Heroku | CSS/JS missing in production | Configured static settings, enabled WhiteNoise, collected static files | Styling loads correctly |
| Missing tables after deploy | Pages erroring due to migrations not applied | Ran migrations and confirmed migration order | Data loads correctly |
| Broken links between pages | Some navigation routes were wrong | Updated URL patterns and templates | All internal links work |
| Image upload issues | Upload not saving/displaying reliably | Installed Pillow + corrected image handling | Images display correctly |

---

## 🧭 User Feedback & UX Improvements

To improve usability, the project includes / will continue improving:
- Clear success messages after create/edit/delete actions
- Clear inline form errors when something is missing or invalid
- Helpful guidance text so users know what went wrong and what to do next

---

## 📱 Responsive Testing

Due to iframe embedding protection being enabled, responsive testing was completed using Chrome Browser Developer Tools.

The following viewports were tested:
- Mobile (iPhone SE / iPhone 12)
- Tablet (iPad)
- Desktop (1080p and above)
- Landscape and portrait orientations

### 📸 Responsive Screenshots (Browser DevTools)

**Homepage – Mobile View**  
<img src="https://raw.githubusercontent.com/Anasousa11/HomeRoots/main/core/static/core/screenshots/home_mobile.png" width="320" alt="Homepage mobile view">

**Students Dashboard – Tablet View**  
<img src="https://raw.githubusercontent.com/Anasousa11/HomeRoots/main/core/static/core/screenshots/student_tablet.png" width="520" alt="Students dashboard tablet view">

**Lessons Dashboard – Mobile View**  
<img src="https://raw.githubusercontent.com/Anasousa11/HomeRoots/main/core/static/core/screenshots/lesson_mobile.png" width="320" alt="Lessons mobile view">

**Progress Chart – Small Screen Landscape**  
<img src="https://raw.githubusercontent.com/Anasousa11/HomeRoots/main/core/static/core/screenshots/progress_ss.png" width="520" alt="Progress chart landscape">

---

## 🔍 Validator Testing

### HTML Validation (W3C)
<img src="https://raw.githubusercontent.com/Anasousa11/HomeRoots/main/core/static/core/screenshots/html_validator.jpeg" width="850" alt="HTML Validator result">

✔ No major structural errors

### CSS Validation (W3C Jigsaw)
<img src="https://raw.githubusercontent.com/Anasousa11/HomeRoots/main/core/static/core/screenshots/css_validator.jpeg" width="850" alt="CSS Validator result">

✔ Pass – no invalid rules

---

## ✅ Python (PEP8) Validation

All custom Python files were checked using **pycodestyle**.

Commands used:

```
python -m pycodestyle .
python -m pycodestyle . --exclude=.venv
```

Most warnings were formatting only (line length, spacing, import placement).  
These do not affect functionality, and all main features were tested and confirmed working.

---

## ✅ JavaScript (JSHint) Validation

JSHint was used to check the JavaScript in this project.

Command used:

```
jshint core/static/
```

Most warnings came from an auto-generated Django admin vendor file and were safely ignored (not part of my code).

---

## 📁 Folder Pathway

<img src="https://raw.githubusercontent.com/Anasousa11/HomeRoots/main/core/static/core/screenshots/directory.png" width="850" alt="Project directory structure">

---

## 📝 Project Planning

### Wireframes

<img src="https://raw.githubusercontent.com/Anasousa11/HomeRoots/main/core/static/core/screenshots/wireframe.png" width="850" alt="Wireframes">

---

## 🧭 User Stories

- As a homeschooling parent, I want to add my children so their learning can be organised individually.
- As a parent, I want to plan and save lessons for future use.
- As a parent, I want to assign lessons and track when they’re completed.
- As a parent, I want to give grades and see improvement visually.
- As a user, I want to contact the site owner easily through a simple form.

---

## 🔒 Security

This project uses environment variables to protect sensitive values:
- Secret key is not stored in GitHub
- `.env` is ignored and `.env.example` is provided for safe setup
- DEBUG is disabled in production
- Config Vars are used on Heroku

---

## 🚀 Deployment

HomeRoots was deployed using Heroku.

### Running the Project Locally

1. Clone the repository:
```
git clone https://github.com/yourusername/your-repo-name.git
```

2. Navigate into the project folder:
```
cd your-repo-name
```

3. Create and activate a virtual environment:
```
python -m venv venv
```

Windows:
```
venv\Scripts\activate
```

Mac/Linux:
```
source venv/bin/activate
```

4. Install dependencies:
```
pip install -r requirements.txt
```

5. Create a `.env` file with:
```
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
```

6. Apply migrations:
```
python manage.py migrate
```

7. Create a superuser:
```
python manage.py createsuperuser
```

8. Run the server:
```
python manage.py runserver
```

9. Open in browser:
- http://127.0.0.1:8000/

### Heroku Deployment (Summary)

- Created a new Heroku app  
- Added Config Vars (SECRET_KEY, DATABASE_URL)  
- Installed production dependencies (gunicorn, dj-database-url, psycopg2-binary, whitenoise)  
- Added Procfile  
- Collected static files  
- Ran migrations on deploy  
- App is accessible live  

---

## 📝 Assessment Criteria Alignment

✔ Full CRUD functionality  
✔ Relational database design  
✔ Secure cloud deployment  
✔ Django framework conventions  
✔ Responsive front-end  
✔ Manual testing documentation  
✔ Version control using GitHub  
✔ Security practices applied  
✔ Professional documentation  

---

## 📚 Credits & Sources

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

## 🌟 Future Improvements

- Printable worksheets for homeschool subjects  
- Weekly planner PDF generator  
- Parent dashboard  
- Drag-and-drop lesson scheduler  
- Cloud storage for worksheets  
- Curriculum templates for different ages  

---

## 💬 Reflection

Building HomeRoots was one of the most challenging but rewarding projects I have worked on so far. Balancing this project alongside parenting three young children made time management extremely difficult, but it also reinforced why this project mattered so much to me personally.

During development, I faced several delays and was granted an official extension to complete the project. One of the biggest obstacles was ongoing technical issues with my original laptop, which significantly slowed my progress. After researching the most suitable laptop for programming and development, I made the decision to purchase a new one on the official submission date so that I could finally complete, deploy, and submit the project properly.

This project helped me fully understand how a full-stack web application works — from database modelling and CRUD logic to templates, deployment, and debugging live errors. Some issues took forever to solve, but working through them built my confidence and embedded knowledge that will help me in my web development career.

HomeRoots represents both my technical growth and a real solution to a real need in my own life.

---

## 👩‍💻 Author

Ana Samanda Dicha De Sousa  
Web Application Development – Level 5 Diploma  
GitHub: https://github.com/Anasousa11
