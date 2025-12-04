
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

### **Models**
- Student  
- Lesson  
- LessonProgress  

### **Relationships**
- One student → many progress entries  
- One lesson → many progress entries  
- LessonProgress links Students and Lessons  

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

### Manual Testing:

- Student Management
- Add student → works
- Edit student → works
- Delete student → works
- Validate required fields → works
- Lesson Management
- Create lesson → correct redirect
- Edit/delete lessons → working
- Assigned lessons appear correctly
- Progress System
- Assign lesson → added to pending
- Mark lesson as completed → moves to “completed”
- Grade saved & displayed
- Chart updates with new data
- Contact Form
- Empty fields → shows error
- Valid form → success message
- Console displays email data
- Dashboard Navigation
- All navbar links tested
- Breadcrumbs tested
- No broken links found

### 📱 Responsive Testing

()



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

# 🎯 Assessment Criteria Coverage

✔ CRUD functionality (students & lessons)  
✔ Relational database with appropriate models  
✔ Django templates & front-end structure  
✔ Routing & URL configuration  
✔ Data visualisation using Chart.js  
✔ Contact form (Django messages)  
✔ UX considerations & responsive design  
✔ Complete README documentation  
✔ Wireframes & screenshots 

---

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

Building HomeRoots was both an academic challenge and a personal accomplishment.  
It helped me solve a real problem I faced as a homeschooling mother: staying organised while teaching children at different levels.

I learned how to structure a web application, build multiple interconnected models, design a theme, and debug problems I initially thought were impossible.

This project taught me confidence, perseverance, and practical skills I will use in real life.



👩‍💻 Author

Ana Samanda Dicha De Sousa
Web Application Development – Level 5 Diploma
GitHub: https://github.com/Anasousa11



