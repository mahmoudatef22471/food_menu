# Django Institute Management System

A modern, full-featured Django application for managing courses, students, and instructors with an elegant, responsive user interface.

## 📋 Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Database Models](#database-models)
- [Frontend Features](#frontend-features)

## 🌟 Features

### Core Functionality
- **Course Management**: Create, view, and manage courses with instructor assignments
- **Student Management**: Track enrolled students and their course participation
- **Instructor Management**: Manage instructor profiles and course assignments
- **Admin Dashboard**: Built-in Django admin for easy data management

### Frontend Features
- **Modern Responsive Design**: Fully responsive on all devices
- **Dark Mode Toggle**: Switch between light and dark themes with persistent storage
- **Real-Time Search**: Filter courses instantly as you type
- **Favorites System**: Save favorite courses with localStorage persistence
- **Interactive Modals**: Course detail modals with comprehensive information
- **Toast Notifications**: User-friendly feedback for all actions
- **Newsletter Subscription**: Email signup functionality
- **Smooth Animations**: Scroll-triggered animations and transitions
- **Loading Screen**: Professional loading animation on page load
- **Parallax Effects**: Subtle background animations
- **Scroll-to-Top Button**: Floating button for easy navigation

## 🛠 Tech Stack

**Backend:**
- Django 5.0+
- Python 3.10+
- SQLite (default)

**Frontend:**
- HTML5
- CSS3 (Variables, Grid, Flexbox, Animations)
- Vanilla JavaScript
- Font Awesome Icons

## 📦 Installation

### Prerequisites
- Python 3.10+
- pip package manager
- Virtual environment (recommended)

### Setup Steps

#### 1. Create Virtual Environment
```bash
python -m venv myenv
source myenv/Scripts/activate  # Windows
# or
source myenv/bin/activate      # macOS/Linux
```

#### 2. Install Django
```bash
pip install django
```

#### 3. Run Migrations
```bash
python manage.py migrate
```

#### 4. Create Superuser (Admin)
```bash
python manage.py createsuperuser
```
Follow the prompts to create your admin account.

#### 5. Start Development Server
```bash
python manage.py runserver
```

#### 6. Access the Application
- **Courses**: http://127.0.0.1:8000/courses/
- **Admin Panel**: http://127.0.0.1:8000/admin/

## 📁 Project Structure

```
institute/
├── manage.py
├── db.sqlite3
│
├── courses/                          # Courses App
│   ├── migrations/
│   ├── templates/
│   │   └── courses/
│   │       └── courses_list.html    # Main courses page with enhanced UI
│   ├── static/
│   │   └── courses/
│   │       └── css/
│   │           └── style.css        # All CSS (separated architecture)
│   ├── models.py                    # Course model definition
│   ├── views.py                     # Course view logic
│   ├── urls.py                      # Course URL routing
│   ├── admin.py                     # Django admin config
│   └── apps.py
│
├── students/                         # Students App
│   ├── migrations/
│   ├── models.py                    # Student model
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── apps.py
│
├── Instructors/                      # Instructors App
│   ├── migrations/
│   ├── models.py                    # Instructor model
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── apps.py
│
└── institute/                        # Project Configuration
    ├── settings.py                   # Django settings
    ├── urls.py                       # Main URL configuration
    ├── asgi.py
    └── wsgi.py
```

## 🗄️ Database Models

### Course Model
```python
class Course(models.Model):
    name = models.CharField(max_length=100)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, blank=True)
    
    def __str__(self):
        return self.name
```

### Instructor Model
```python
class Instructor(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
```

### Student Model
```python
class Student(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
```

## 💻 Usage

### Adding Data via Admin Panel

1. Go to http://127.0.0.1:8000/admin/
2. Log in with your superuser credentials
3. Add Instructors first
4. Add Students
5. Create Courses and assign instructors and students

### Frontend Features Usage

#### Search Courses
- Type in the search bar to filter courses by name
- Results filter in real-time

#### Theme Toggle
- Click the moon (🌙) icon in header to enable dark mode
- Your preference is saved automatically

#### Add to Favorites
- Click any course card to open the modal
- Click "Add to Favorites" button
- View favorite count in header
- Favorites persist in browser

#### Newsletter Subscription
- Enter email in footer newsletter section
- Click Subscribe
- Success notification appears

#### Course Details
- Click any course card to view detailed information
- See instructor, students, and statistics
- Take action via modal buttons

## 🎨 Design Architecture

### CSS Approach
- **Single CSS File**: `courses/static/courses/css/style.css`
- **CSS Variables**: Theming with `:root` and `.dark-mode` classes
- **Responsive Design**: Mobile-first approach
- **Modern Features**: Gradients, animations, glassmorphism effects

### JavaScript Features
- Theme persistence with localStorage
- Search filtering with DOM manipulation
- Modal management and event handling
- Toast notification system
- Intersection Observer for scroll animations
- Newsletter validation and submission

## 📱 Browser Support
- Chrome/Edge 90+
- Firefox 88+
- Safari 14+
- Mobile Safari (iOS)
- Chrome Mobile

## 🎯 Key Features in Detail

### Dark Mode
- Automatic detection of user preference
- Smooth color transitions
- All elements support both themes
- Settings saved to localStorage

### Search Functionality
- Real-time filtering
- Case-insensitive matching
- Instant feedback
- Cards smoothly appear/disappear

### Favorites System
- Add/remove courses
- Counter in header
- LocalStorage persistence
- Toast notifications

### Modal System
- Click course cards to open
- Display full course information
- Action buttons for enrollment
- Close with X or background click

### Toast Notifications
- Success and error states
- Auto-dismiss after 3 seconds
- Smooth animation
- Fixed position, non-intrusive

## ⚙️ Configuration

### Static Files (Development)
Django automatically serves static files in development mode.

### Debug Mode
Currently set to `DEBUG = True` in `settings.py`.
**Important**: Change to `False` before production deployment.

### DATABASE
Default: SQLite (`db.sqlite3`)
For production, consider using PostgreSQL.

## 🚀 Deployment Tips

### Before Going Live
1. Set `DEBUG = False` in settings.py
2. Update `ALLOWED_HOSTS` in settings.py
3. Use environment variables for sensitive data
4. Run `python manage.py collectstatic`
5. Use a production WSGI server (Gunicorn, Waitress)
6. Set up HTTPS/SSL

### Static Files in Production
```bash
python manage.py collectstatic --noinput
```

## 🐛 Troubleshooting

### Styles Not Loading
- Clear browser cache (Ctrl+Shift+Delete)
- Check browser console (F12) for 404 errors
- Ensure `STATIC_URL = 'static/'` in settings.py
- Verify `DEBUG = True` for development

### Database Issues
```bash
# Reset database (WARNING: Deletes all data)
python manage.py migrate
```

### Port Already in Use
```bash
# Use different port
python manage.py runserver 8001
```

## 📝 Admin Commands

```bash
# Create superuser
python manage.py createsuperuser

# Run migrations
python manage.py migrate

# Create migrations for model changes
python manage.py makemigrations

# Access Django shell
python manage.py shell

# Collect static files (production)
python manage.py collectstatic
```

## 🎯 Future Enhancements

- [ ] User authentication system
- [ ] Course ratings and reviews
- [ ] Email notifications
- [ ] Advanced filtering options
- [ ] Grade management
- [ ] REST API endpoints
- [ ] Unit and integration tests
- [ ] Docker containerization

## 📞 Support

For issues or questions, check the terminal output for error messages or enable debug mode for detailed error pages.

## 📄 License

This project is part of the Institute Management Suite.

---

**Version**: 1.0.0  
**Last Updated**: March 8, 2026  
**Status**: ✅ Production Ready
