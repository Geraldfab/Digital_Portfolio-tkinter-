"""
Digital Portfolio Application using Tkinter
A modern, interactive portfolio with smooth animations and professional UI/UX
"""

import tkinter as tk
from tkinter import ttk
import time

# Color scheme - Modern dark theme with accent colors
COLORS = {
    'bg_primary': '#1a1a2e',
    'bg_secondary': '#16213e',
    'bg_tertiary': '#0f3460',
    'accent': '#e94560',
    'accent_secondary': '#533483',
    'text_primary': '#ffffff',
    'text_secondary': '#a0a0a0',
    'text_muted': '#6c6c6c',
    'card_bg': '#252542',
    'nav_hover': '#e94560',
}

# Personal Information
PERSONAL_INFO = {
    'name': 'Gerald Fabre',
    'email': 'geraldfabre282@gmail.com',
    'phone': '+63 915-149-1270',
    'location': 'Cabadiangan, Kadingilan, Bukidnon',
    'education': [
        {'school': 'Torres Capitol College Inc.', 'year': '2025-2029', 'description': 'Computer Science/IT'},
        {'school': 'San Andres National High School', 'year': '2023-2025', 'description': 'Secondary Education'},
    ],
    'interests': [
        'Open Source Development',
        'Machine Learning & AI',
        'Photography',
        'Travel & Exploration',
        'Reading & Learning',
        'Gaming',
    ],
    'skills': [
        {'name': 'Python', 'level': 90},
        {'name': 'JavaScript', 'level': 75},
        {'name': 'HTML/CSS', 'level': 85},
        {'name': 'Machine Learning', 'level': 70},
        {'name': 'Data Analysis', 'level': 75},
        {'name': 'Git/Version Control', 'level': 80},
        {'name': 'SQL/Databases', 'level': 70},
        {'name': 'Problem Solving', 'level': 85},
    ],
    'experience': [
        {'role': 'Freelance Developer', 'company': 'Self-employed', 'year': '2023-Present', 'description': 'Developing web applications and automation scripts for various clients.'},
        {'role': 'Open Source Contributor', 'company': 'GitHub Community', 'year': '2022-Present', 'description': 'Contributing to open source projects and maintaining repositories.'},
    ],
    'projects': [
        {'name': 'AI-powered Task Manager', 'description': 'Machine learning based task prioritization system', 'tech': 'Python, TensorFlow, Tkinter'},
        {'name': 'Portfolio Website', 'description': 'Responsive personal portfolio with modern design', 'tech': 'HTML, CSS, JavaScript'},
        {'name': 'Data Visualization Dashboard', 'description': 'Interactive data analysis and visualization tool', 'tech': 'Python, Pandas, Matplotlib'},
        {'name': 'Automation Scripts', 'description': 'Various automation tools for productivity', 'tech': 'Python, Selenium'},
    ],
    'services': [
        {'name': 'Web Development', 'description': 'Custom websites and web applications'},
        {'name': 'Machine Learning', 'description': 'AI solutions and data analysis'},
        {'name': 'Consulting', 'description': 'Technical advice and code reviews'},
        {'name': 'Tutoring', 'description': 'Programming lessons and mentorship'},
    ],
    'achievements': [
        {'title': 'Deans Lister', 'description': 'Academic Excellence Award', 'year': '2024'},
        {'title': 'Hackathon Winner', 'description': 'Tech Innovation Challenge', 'year': '2023'},
        {'title': 'Open Source Contributor', 'description': '100+ Contributions', 'year': '2023'},
    ],
}


class DigitalPortfolio:
    """Main Digital Portfolio Application"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Gerald Fabre - Digital Portfolio")
        self.root.geometry("1200x800")
        self.root.configure(bg=COLORS['bg_primary'])
        self.root.minsize(1000, 700)
        
        self.current_section = None
        
        # Create main container
        self.main_container = tk.Frame(self.root, bg=COLORS['bg_primary'])
        self.main_container.pack(fill='both', expand=True)
        
        # Navigation bar
        self.create_navigation()
        
        # Content area
        self.content_frame = tk.Frame(self.main_container, bg=COLORS['bg_primary'])
        self.content_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Floating contact button
        self.create_floating_contact()
        
        # Center window
        self.center_window()
        
        # Show home section
        self.show_section('home')
    
    def center_window(self):
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def create_navigation(self):
        nav_frame = tk.Frame(self.main_container, bg=COLORS['bg_secondary'], height=60)
        nav_frame.pack(fill='x')
        nav_frame.pack_propagate(False)
        
        logo_label = tk.Label(
            nav_frame,
            text='GF',
            bg=COLORS['bg_secondary'],
            fg=COLORS['accent'],
            font=('Segoe UI', 24, 'bold')
        )
        logo_label.pack(side='left', padx=20)
        
        nav_btn_frame = tk.Frame(nav_frame, bg=COLORS['bg_secondary'])
        nav_btn_frame.pack(side='right', padx=20)
        
        nav_items = ['Home', 'About', 'Skills', 'Experience', 'Projects', 'Services']
        
        for item in nav_items:
            btn = tk.Button(
                nav_btn_frame,
                text=item,
                command=lambda s=item.lower(): self.show_section(s),
                bg=COLORS['bg_secondary'],
                fg=COLORS['text_primary'],
                font=('Segoe UI', 11),
                relief='flat',
                bd=0,
                padx=15,
                pady=10,
                cursor='hand2',
                activebackground=COLORS['nav_hover'],
            )
            btn.pack(side='left')
            btn.bind('<Enter>', lambda e, b=btn: b.config(bg=COLORS['nav_hover']))
            btn.bind('<Leave>', lambda e, b=btn: b.config(bg=COLORS['bg_secondary']))
    
    def show_section(self, section_name):
        # Clear current content
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        self.current_section = section_name
        
        # Create section content
        if section_name == 'home':
            self.create_home()
        elif section_name == 'about':
            self.create_about()
        elif section_name == 'skills':
            self.create_skills()
        elif section_name == 'experience':
            self.create_experience()
        elif section_name == 'projects':
            self.create_projects()
        elif section_name == 'services':
            self.create_services()
    
    def create_home(self):
        # Main container with two columns
        main = tk.Frame(self.content_frame, bg=COLORS['bg_primary'])
        main.pack(fill='both', expand=True)
        
        # Left side - Text
        left = tk.Frame(main, bg=COLORS['bg_primary'])
        left.pack(side='left', fill='both', expand=True)
        
        tk.Label(
            left,
            text='Hello, I am',
            bg=COLORS['bg_primary'],
            fg=COLORS['text_secondary'],
            font=('Segoe UI', 18)
        ).pack(anchor='w', pady=(100, 0))
        
        tk.Label(
            left,
            text=PERSONAL_INFO['name'],
            bg=COLORS['bg_primary'],
            fg=COLORS['accent'],
            font=('Segoe UI', 48, 'bold')
        ).pack(anchor='w')
        
        tk.Label(
            left,
            text='Developer | ML Enthusiast | Problem Solver',
            bg=COLORS['bg_primary'],
            fg=COLORS['text_primary'],
            font=('Segoe UI', 20)
        ).pack(anchor='w', pady=(10, 30))
        
        tk.Label(
            left,
            text='Passionate about building innovative solutions through\ncode and machine learning. Turning ideas into reality.',
            bg=COLORS['bg_primary'],
            fg=COLORS['text_secondary'],
            font=('Segoe UI', 14),
            justify='left'
        ).pack(anchor='w', pady=(0, 30))
        
        # Buttons
        btn_frame = tk.Frame(left, bg=COLORS['bg_primary'])
        btn_frame.pack(anchor='w')
        
        self.create_button(btn_frame, 'View My Work', lambda: self.show_section('projects')).pack(side='left', padx=(0, 15))
        self.create_button(btn_frame, 'Contact Me', self.toggle_contact).pack(side='left')
        
        # Right side - Profile placeholder
        right = tk.Frame(main, bg=COLORS['bg_primary'])
        right.pack(side='right', fill='both', expand=True, padx=50)
        
        # Profile image container
        profile_container = tk.Frame(right, bg=COLORS['bg_tertiary'], width=300, height=350)
        profile_container.pack(pady=(80, 0))
        profile_container.pack_propagate(False)
        
        tk.Label(
            profile_container,
            text='📷\n\n[Replace with\nYour Photo]',
            bg=COLORS['bg_tertiary'],
            fg=COLORS['text_secondary'],
            font=('Segoe UI', 16),
            justify='center'
        ).pack(fill='both', expand=True, padx=10, pady=10)
    
    def create_button(self, parent, text, command):
        btn = tk.Button(
            parent,
            text=text,
            command=command,
            bg=COLORS['accent'],
            fg=COLORS['text_primary'],
            font=('Segoe UI', 11, 'bold'),
            relief='flat',
            bd=0,
            padx=20,
            pady=10,
            cursor='hand2',
            activebackground=COLORS['accent_secondary'],
        )
        return btn
    
    def create_about(self):
        tk.Label(
            self.content_frame,
            text='About Me',
            bg=COLORS['bg_primary'],
            fg=COLORS['accent'],
            font=('Segoe UI', 36, 'bold')
        ).pack(anchor='w', pady=(30, 30))
        
        # Bio text
        bio = """Hi! I'm Gerald Fabre, a passionate developer and lifelong learner 
based in Bukidnon, Philippines.

I have a strong interest in open source development, machine learning, 
and creating impactful solutions through technology. When I'm not coding, 
you can find me exploring new places through photography, playing games, 
or diving into a good book.

I'm currently studying at Torres Capitol College Inc. and continuously 
working on improving my skills in various areas of technology."""
        
        tk.Label(
            self.content_frame,
            text=bio,
            bg=COLORS['bg_primary'],
            fg=COLORS['text_secondary'],
            font=('Segoe UI', 14),
            justify='left',
            wraplength=600
        ).pack(anchor='w')
        
        # Info cards
        info_frame = tk.Frame(self.content_frame, bg=COLORS['bg_primary'])
        info_frame.pack(fill='x', pady=30)
        
        # Education card
        self.create_info_card(info_frame, '🎓 Education', 
            [f"{e['school']} ({e['year']})" for e in PERSONAL_INFO['education']]
        ).pack(side='left', fill='both', expand=True, padx=(0, 15))
        
        # Interests card
        self.create_info_card(info_frame, '💡 Interests', 
            PERSONAL_INFO['interests']
        ).pack(side='left', fill='both', expand=True, padx=(0, 15))
        
        # Achievements card
        self.create_info_card(info_frame, '🏆 Achievements', 
            [f"{a['title']} - {a['year']}" for a in PERSONAL_INFO['achievements']]
        ).pack(side='left', fill='both', expand=True)
    
    def create_info_card(self, parent, title, items):
        card = tk.Frame(parent, bg=COLORS['card_bg'], padx=20, pady=20)
        
        tk.Label(
            card,
            text=title,
            bg=COLORS['card_bg'],
            fg=COLORS['text_primary'],
            font=('Segoe UI', 14, 'bold')
        ).pack(anchor='w', pady=(0, 15))
        
        for item in items:
            tk.Label(
                card,
                text=f'• {item}',
                bg=COLORS['card_bg'],
                fg=COLORS['text_secondary'],
                font=('Segoe UI', 11)
            ).pack(anchor='w', pady=(0, 5))
        
        return card
    
    def create_skills(self):
        tk.Label(
            self.content_frame,
            text='My Skills',
            bg=COLORS['bg_primary'],
            fg=COLORS['accent'],
            font=('Segoe UI', 36, 'bold')
        ).pack(anchor='w', pady=(30, 30))
        
        # Skills container
        skills_frame = tk.Frame(self.content_frame, bg=COLORS['bg_primary'])
        skills_frame.pack(fill='both', expand=True)
        
        # Split skills into two columns
        mid = len(PERSONAL_INFO['skills']) // 2
        left_skills = PERSONAL_INFO['skills'][:mid]
        right_skills = PERSONAL_INFO['skills'][mid:]
        
        # Left column
        left = tk.Frame(skills_frame, bg=COLORS['bg_primary'])
        left.pack(side='left', fill='both', expand=True)
        
        # Right column
        right = tk.Frame(skills_frame, bg=COLORS['bg_primary'])
        right.pack(side='right', fill='both', expand=True)
        
        for skill in left_skills:
            self.create_skill_item(left, skill['name'], skill['level'])
        
        for skill in right_skills:
            self.create_skill_item(right, skill['name'], skill['level'])
    
    def create_skill_item(self, parent, name, level):
        container = tk.Frame(parent, bg=COLORS['bg_primary'], pady=10)
        container.pack(fill='x')
        
        tk.Label(
            container,
            text=name,
            bg=COLORS['bg_primary'],
            fg=COLORS['text_primary'],
            font=('Segoe UI', 12, 'bold')
        ).pack(anchor='w')
        
        # Progress bar background
        progress_bg = tk.Frame(container, bg=COLORS['bg_tertiary'], height=10)
        progress_bg.pack(fill='x', pady=(5, 0))
        
        # Progress bar fill
        progress_fill = tk.Frame(progress_bg, bg=COLORS['accent'], width=1)
        progress_fill.pack(side='left', fill='y')
        
        # Animate the progress bar
        container.after(100, lambda: self.animate_progress(progress_fill, progress_bg, level))
        
        tk.Label(
            container,
            text=f'{level}%',
            bg=COLORS['bg_primary'],
            fg=COLORS['text_secondary'],
            font=('Segoe UI', 10)
        ).pack(anchor='e', pady=(5, 0))
    
    def animate_progress(self, fill, bg, target):
        bg.update_idletasks()
        max_width = bg.winfo_width()
        if max_width > 1:
            target_width = max_width * (target / 100)
            for i in range(20):
                fill.config(width=int(target_width * (i + 1) / 20))
                bg.update()
                time.sleep(0.02)
    
    def create_experience(self):
        tk.Label(
            self.content_frame,
            text='Experience',
            bg=COLORS['bg_primary'],
            fg=COLORS['accent'],
            font=('Segoe UI', 36, 'bold')
        ).pack(anchor='w', pady=(30, 30))
        
        for exp in PERSONAL_INFO['experience']:
            self.create_experience_card(exp).pack(fill='x', pady=(0, 20))
    
    def create_experience_card(self, exp):
        card = tk.Frame(self.content_frame, bg=COLORS['card_bg'], padx=30, pady=25)
        
        tk.Label(
            card,
            text=exp['year'],
            bg=COLORS['accent'],
            fg=COLORS['text_primary'],
            font=('Segoe UI', 10, 'bold'),
            padx=10,
            pady=5
        ).pack(anchor='w')
        
        tk.Label(
            card,
            text=exp['role'],
            bg=COLORS['card_bg'],
            fg=COLORS['text_primary'],
            font=('Segoe UI', 18, 'bold'),
            pady=(10, 5)
        ).pack(anchor='w')
        
        tk.Label(
            card,
            text=exp['company'],
            bg=COLORS['card_bg'],
            fg=COLORS['accent'],
            font=('Segoe UI', 14)
        ).pack(anchor='w')
        
        tk.Label(
            card,
            text=exp['description'],
            bg=COLORS['card_bg'],
            fg=COLORS['text_secondary'],
            font=('Segoe UI', 12),
            wraplength=600,
            justify='left',
            pady=(10, 0)
        ).pack(anchor='w')
        
        return card
    
    def create_projects(self):
        tk.Label(
            self.content_frame,
            text='My Projects',
            bg=COLORS['bg_primary'],
            fg=COLORS['accent'],
            font=('Segoe UI', 36, 'bold')
        ).pack(anchor='w', pady=(30, 30))
        
        # Projects in a simple vertical stack
        for project in PERSONAL_INFO['projects']:
            self.create_project_card(project).pack(fill='x', pady=(0, 15))
    
    def create_project_card(self, project):
        card = tk.Frame(self.content_frame, bg=COLORS['card_bg'], padx=20, pady=20)
        
        tk.Label(
            card,
            text='💻',
            bg=COLORS['card_bg'],
            fg=COLORS['accent'],
            font=('Segoe UI', 24)
        ).pack()
        
        tk.Label(
            card,
            text=project['name'],
            bg=COLORS['card_bg'],
            fg=COLORS['text_primary'],
            font=('Segoe UI', 16, 'bold'),
            pady=(10, 5)
        ).pack()
        
        tk.Label(
            card,
            text=project['description'],
            bg=COLORS['card_bg'],
            fg=COLORS['text_secondary'],
            font=('Segoe UI', 12)
        ).pack()
        
        tk.Label(
            card,
            text=f"Tech: {project['tech']}",
            bg=COLORS['card_bg'],
            fg=COLORS['accent'],
            font=('Segoe UI', 10),
            pady=(10, 0)
        ).pack()
        
        return card
    
    def create_services(self):
        tk.Label(
            self.content_frame,
            text='Services',
            bg=COLORS['bg_primary'],
            fg=COLORS['accent'],
            font=('Segoe UI', 36, 'bold')
        ).pack(anchor='w', pady=(30, 30))
        
        # Services in a simple vertical stack
        for service in PERSONAL_INFO['services']:
            self.create_service_card(service).pack(fill='x', pady=(0, 15))
    
    def create_service_card(self, service):
        card = tk.Frame(self.content_frame, bg=COLORS['card_bg'], padx=30, pady=25)
        
        icons = {'Web Development': '🌐', 'Machine Learning': '🤖', 'Consulting': '📊', 'Tutoring': '📚'}
        icon = icons.get(service['name'], '💡')
        
        tk.Label(
            card,
            text=icon,
            bg=COLORS['card_bg'],
            fg=COLORS['accent'],
            font=('Segoe UI', 24)
        ).pack()
        
        tk.Label(
            card,
            text=service['name'],
            bg=COLORS['card_bg'],
            fg=COLORS['text_primary'],
            font=('Segoe UI', 16, 'bold'),
            pady=(10, 5)
        ).pack()
        
        tk.Label(
            card,
            text=service['description'],
            bg=COLORS['card_bg'],
            fg=COLORS['text_secondary'],
            font=('Segoe UI', 12)
        ).pack()
        
        return card
    
    def create_floating_contact(self):
        # Floating button at bottom right
        self.float_btn = tk.Button(
            self.root,
            text='📞 Contact',
            command=self.toggle_contact,
            bg=COLORS['accent'],
            fg=COLORS['text_primary'],
            font=('Segoe UI', 12, 'bold'),
            relief='raised',
            bd=2,
            padx=20,
            pady=12,
            cursor='hand2',
            activebackground=COLORS['accent_secondary'],
        )
        self.float_btn.place(relx=0.98, rely=0.95, anchor='se')
        
        # Contact popup (initially hidden)
        self.contact_popup = tk.Frame(self.root, bg=COLORS['card_bg'], padx=20, pady=20)
        
        tk.Label(
            self.contact_popup,
            text='📧 Email',
            bg=COLORS['card_bg'],
            fg=COLORS['text_secondary'],
            font=('Segoe UI', 10)
        ).pack(anchor='w')
        
        tk.Label(
            self.contact_popup,
            text=PERSONAL_INFO['email'],
            bg=COLORS['card_bg'],
            fg=COLORS['text_primary'],
            font=('Segoe UI', 11)
        ).pack(anchor='w', pady=(0, 10))
        
        tk.Label(
            self.contact_popup,
            text='📱 Phone',
            bg=COLORS['card_bg'],
            fg=COLORS['text_secondary'],
            font=('Segoe UI', 10)
        ).pack(anchor='w')
        
        tk.Label(
            self.contact_popup,
            text=PERSONAL_INFO['phone'],
            bg=COLORS['card_bg'],
            fg=COLORS['text_primary'],
            font=('Segoe UI', 11)
        ).pack(anchor='w', pady=(0, 10))
        
        tk.Label(
            self.contact_popup,
            text='📍 Location',
            bg=COLORS['card_bg'],
            fg=COLORS['text_secondary'],
            font=('Segoe UI', 10)
        ).pack(anchor='w')
        
        tk.Label(
            self.contact_popup,
            text=PERSONAL_INFO['location'],
            bg=COLORS['card_bg'],
            fg=COLORS['text_primary'],
            font=('Segoe UI', 11)
        ).pack(anchor='w', pady=(0, 10))
        
        self.contact_popup_visible = False
    
    def toggle_contact(self):
        self.contact_popup_visible = not self.contact_popup_visible
        
        if self.contact_popup_visible:
            self.contact_popup.place(relx=0.98, rely=0.85, anchor='se')
            self.float_btn.config(text='✖ Close')
        else:
            self.contact_popup.place_forget()
            self.float_btn.config(text='📞 Contact')


def main():
    root = tk.Tk()
    app = DigitalPortfolio(root)
    root.mainloop()


if __name__ == '__main__':
    main()