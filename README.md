# Institute Management System

A modern, full-featured Django-based Institute Management System with an elegant, responsive UI for managing courses, students, and instructors.

![Django](https://img.shields.io/badge/Django-5.0+-green)
![Python](https://img.shields.io/badge/Python-3.10+-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 🌟 Features

### Core Functionality
- **Course Management**: Create, view, and manage courses with instructor assignments
- **Student Management**: Track enrolled students and their course participation
- **Instructor Management**: Manage instructor profiles and course assignments
- **Database Migrations**: Automated Django migrations for all models

### Frontend Features
- **Modern Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices
- **Dark Mode Toggle**: Switch between light and dark themes with persistent storage
- **Real-time Search**: Filter courses instantly as you type
- **Favorites System**: Save favorite courses with local storage persistence
- **Modal Dialogs**: Interactive course detail modals with rich information
- **Toast Notifications**: User-friendly notifications for actions and feedback
- **Newsletter Subscription**: Email signup with validation
- **Scroll Animations**: Smooth scroll-triggered animations using Intersection Observer
- **Parallax Background**: Subtle floating animation effects
- **Loading Screen**: Professional loading animation on page load

### UI/UX Enhancements
- Glassmorphism card design with backdrop blur effects
- Gradient backgrounds with custom color schemes
- Smooth transitions and hover animations
- Breadcrumb navigation
- Floating scroll-to-top button
- Professional footer with multiple sections
- Search icon with detailed search interface
- Responsive grid layout for course cards

## 📋 Tech Stack

**Backend:**
- Django 5.0+
- Python 3.10+
- SQLite (default) / PostgreSQL (recommended for production)

**Frontend:**
- HTML5
- CSS3 (with CSS Variables, Grid, Flexbox, Animations)
- JavaScript (Vanilla - no frameworks)
- Font Awesome Icons
- Google Fonts

## 📦 Installation

### Prerequisites
- Python 3.10 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Step 1: Clone the Repository
```bash
git clone https://github.com/mahmoudatef22471/food_menu.git
cd institute
```

### Step 2: Create Virtual Environment
```bash
python -m venv myenv
source myenv/Scripts/activate  # On Windows
# or
source myenv/bin/activate      # On macOS/Linux
```

### Step 3: Install Dependencies
```bash
pip install django
```

### Step 4: Run Migrations
```bash
python manage.py migrate
```

### Step 5: Create Superuser (Admin Account)
```bash
python manage.py createsuperuser
```

### Step 6: Run Development Server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/courses/` in your browser.

## 🚀 Usage

### Accessing the Application
- **Courses Page**: `http://127.0.0.1:8000/courses/`
- **Admin Panel**: `http://127.0.0.1:8000/admin/`

### Creating Data via Admin Panel
1. Log in to admin at `/admin/`
2. Navigate to Instructors and create instructor profiles
3. Create Students
4. Create Courses and assign instructors and students

### Frontend Features
- **Search**: Use the search bar to filter courses by name
- **Dark Mode**: Click the moon icon in the header to toggle theme
- **Favorites**: Click the heart icon in course modals to add to favorites
- **Newsletter**: Enter your email in the footer to subscribe
- **Modal**: Click any course card to view detailed information

## 📁 Project Structure

```
institute/
├── manage.py
├── db.sqlite3
├── courses/                          # Courses app
│   ├── migrations/
│   ├── templates/courses/
│   │   └── courses_list.html        # Main courses page (enhanced UI)
│   ├── static/courses/
│   │   └── css/
│   │       └── style.css            # All styling (separated from HTML)
│   ├── models.py                    # Course, Student, Instructor models
│   ├── views.py                     # View logic
│   ├── urls.py                      # URL routing
│   ├── admin.py                     # Django admin configuration
│   └── apps.py
│
├── students/                         # Students app
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── Instructors/                      # Instructors app
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
└── institute/                        # Project settings
    ├── settings.py                   # Django configuration
    ├── urls.py                       # Main URL configuration
    ├── asgi.py
    └── wsgi.py

```

## 🎨 Styling Architecture

### CSS Organization
- **Location**: `courses/static/courses/css/style.css`
- **Approach**: Separated from HTML using Django's `{% static %}` template tag
- **Features**:
  - CSS Variables for theming (`:root` for light, `.dark-mode` for dark)
  - Mobile-first responsive design
  - Animations and transitions
  - Grid and Flexbox layouts
  - Glassmorphism effects

### JavaScript Features
- Inline in template for dynamic functionality:
  - Theme toggle with localStorage persistence
  - Search functionality with real-time filtering
  - Modal management (open/close with click handlers)
  - Favorites system with JSON storage
  - Toast notifications for user feedback
  - Intersection Observer for scroll animations
  - Newsletter subscription handling

## 🗄️ Database Models

### Course
```python
- name: CharField(max_length=100)
- instructor: ForeignKey(Instructor)
- students: ManyToManyField(Student)
```

### Instructor
```python
- name: CharField(max_length=100)
```

### Student
```python
- name: CharField(max_length=100)
```

## 🔧 Configuration

### Static Files
Development mode automatically serves static files. For production:
```bash
python manage.py collectstatic
```

### Debug Mode
Currently set to `DEBUG = True` in `settings.py`. Change to `False` for production.

## 🌐 Browser Support
- Chrome/Edge 90+
- Firefox 88+
- Safari 14+
- Mobile browsers (iOS Safari, Chrome Mobile)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see LICENSE file for details.

## 👨‍💻 Author

**Mahmoud Atef**
- GitHub: [@mahmoudatef22471](https://github.com/mahmoudatef22471)
- Email: [Your Email]

## 🐛 Known Issues

None currently. Please report bugs via GitHub Issues.

## 📚 Additional Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [MDN Web Docs](https://developer.mozilla.org/)
- [CSS Variables Guide](https://developer.mozilla.org/en-US/docs/Web/CSS/--*)

## 🎯 Future Enhancements

- [ ] User authentication and permissions
- [ ] Course ratings and reviews
- [ ] Email notifications
- [ ] Advanced filtering and sorting
- [ ] Course enrollment workflow
- [ ] Grade management system
- [ ] API endpoints (REST framework)
- [ ] Unit tests
- [ ] Docker containerization
- [ ] Database export/import features

## 📞 Support

For support, open an issue on GitHub or contact the author.

---

**Last Updated**: March 8, 2026  
**Version**: 1.0.0
