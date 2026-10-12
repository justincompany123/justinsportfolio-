
from flask import Flask, render_template

app = Flask(__name__)


# ==============================
# PERSONAL INFORMATION
# ==============================

PERSONAL_INFO = {
    "name": "Justin C. Ramos",
    "nickname": "Timmy",
    "course": "BS Information Technology",
    "school": "Fellowship Baptist College",
    "role": (
        "Student | Content Creator | Web Developer | "
        "Blockchain Technology Beginner"
    ),
    "location": "Kabankalan City, Negros Occidental, Philippines",
    "email": "ramos_justin@fbc.ph.education",
    "facebook": "https://www.facebook.com/",
    "introduction": (
        "I'm an Information Technology student passionate about "
        "web development, database management, programming, and "
        "creative digital projects. I enjoy exploring new technologies, "
        "developing practical solutions, and creating user-friendly "
        "websites and applications. I am continuously improving my "
        "technical skills and expanding my knowledge in the IT field. "
        "My goal is to become a skilled IT professional who can use "
        "technology and creativity to build meaningful and innovative "
        "digital solutions."
    ),
    "about": (
        "I am currently pursuing a Bachelor of Science in "
        "Information Technology at Fellowship Baptist College. "
        "I enjoy learning programming, developing websites, "
        "managing databases, and creating useful digital solutions."
    ),
    "goal": (
        "To improve my programming skills, gain practical experience, "
        "and create innovative projects that solve real-world problems."
    )
}


# ==============================
# TECHNICAL SKILLS
# ==============================

SKILLS = [
    "Python",
    "HTML & CSS",
    "JavaScript",
    "PHP",
    "MySQL",
    "SQLite",
    "Web Development",
    "Innovation",
    "Database Management",
    "Networking",
    "UI Design",
    "Blockchain Technology"
]


# ==============================
# PERSONAL PROJECTS
# ==============================

PROJECTS = [
    {
        "title": "MedKIT Clinic System",
        "category": "Web System",
        "description": (
            "A proposed clinic management system designed to organize "
            "patient records, appointments, and medical certificates "
            "while supporting secure and efficient clinic operations."
        ),
        "technologies": [
            "Python",
            "Web Development",
            "Database Management"
        ],
        "status": "Concept / Development"
    },
    {
        "title": "ACAD GRANT",
        "category": "Web System",
        "description": (
            "A proposed web-based scholarship management system "
            "for the Fellowship Baptist College scholarship office. "
            "It aims to organize academic scholarship information "
            "and student records efficiently."
        ),
        "technologies": [
            "HTML & CSS",
            "JavaScript",
            "PHP",
            "MySQL"
        ],
        "status": "Academic Project"
    },
    {
        "title": "Roblox Ticketing Website",
        "category": "Web Development",
        "description": (
            "A website project for managing user registrations "
            "and ticket-related information, featuring an "
            "administrator dashboard."
        ),
        "technologies": [
            "PHP",
            "MySQL",
            "HTML & CSS"
        ],
        "status": "Personal Project"
    }
]


# ==============================
# FLASK ROUTES
# ==============================

@app.route("/")
def home():
    """Display the portfolio homepage."""

    return render_template(
        "index.html",
        personal=PERSONAL_INFO,
        skills=SKILLS,
        projects=PROJECTS
    )


# ==============================
# ABOUT PAGE
# ==============================

@app.route("/about")
def about():
    """Display the about page."""

    return render_template(
        "about.html",
        personal=PERSONAL_INFO
    )


# ==============================
# RUN THE APPLICATION
# ==============================

if __name__ == "__main__":
    app.run(debug=True)
