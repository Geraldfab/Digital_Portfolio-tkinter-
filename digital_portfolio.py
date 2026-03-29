"""
Digital Portfolio Application using Tkinter
A modern, interactive portfolio with smooth animations and professional UI/UX
"""

import tkinter as tk
from tkinter import ttk
import math
import time
from typing import Callable, Optional

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
    'gold': '#ffd700',
    'silver': '#c0c0c0',
    'bronze': '#cd7f32',
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


class AnimatedButton:
    """Animated button with hover effects"""
    
    def __init__(self, parent, text: str, command: Callable, **kwargs):
        self.command = command
        self.bg_color = kwargs.get('bg', COLORS['accent'])
        self.hover_color = kwargs.get('hover', COLORS['accent_secondary'])
        self.text_color = kwargs.get('text_color', COLORS['text_primary'])
        
        self.frame = tk.Frame(parent, bg=COLORS['bg_primary'])
        
        self.btn = tk.Button(
            self.frame,
            text=text,
            command=command,
            bg=self.bg_color,
            fg=self.text_color,
            font=('Segoe UI', 11, 'bold'),
            relief='flat',
            bd=0,
            padx=20,
            pady=10,
            cursor='hand2',
            activebackground=self.hover_color,
            activeforeground=self.text_color,
        )
        self.btn.pack()
        
        self.btn.bind('<Enter>', self.on_enter)
        self.btn.bind('<Leave>', self.on_leave)
        
        # Animation properties
        self.animation_progress = 0
        self.animation_direction = 0
        
    def on_enter(self, event):
        self.animate_hover(True)
        
    def on_leave(self, event):
        self.animate_hover(False)
        
    def animate_hover(self, enter: bool):
        """Animate button on hover"""
        def animate():
            steps = 10
            if enter:
                for i in range(steps):
                    alpha = i / steps
                    self.btn.config(bg=self.lerp_color(self.bg_color, self.hover_color, alpha))
                    self.frame.update()
                    time.sleep(0.01)
            else:
                for i in range(steps):
                    alpha = i / steps
                    self.btn.config(bg=self.lerp_color(self.hover_color, self.bg_color, alpha))
                    self.frame.update()
                    time.sleep(0.01)
        
        import threading
        thread = threading.Thread(target=animate, daemon=True)
        thread.start()
    
    def lerp_color(self, color1: str, color2: str, t: float) -> str:
        """Linear interpolation between two colors"""
        def hex_to_rgb(hex_color):
            hex_color = hex_color.lstrip('#')
            return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
        
        def rgb_to_hex(rgb):
            return '#{:02x}{:02x}{:02x}'.format(int(rgb[0]), int(rgb[1]), int(rgb[2]))
        
        c1 = hex_to_rgb(color1)
        c2 = hex_to_rgb(color2)
        result = tuple(c1[i] + (c2[i] - c1[i]) * t for i in range(3))
        return rgb_to_hex(result)
    
    def pack(self, **kwargs):
        self.frame.pack(**kwargs)
    
    def grid(self, **kwargs):
        self.frame.grid(**kwargs)


class AnimatedProgressBar:
    """Animated progress bar for skills"""
    
    def __init__(self, parent, width: int = 300, height: int = 20, bg_color: str = COLORS['bg_tertiary']):
        self.width = width
        self.height = height
        self.bg_color = bg_color
        self.fill_color = COLORS['accent']
        
        self.canvas = tk.Canvas(
            parent,
            width=width,
            height=height,
            bg=bg_color,
            highlightthickness=0
        )
        self.canvas.pack()
        
        # Background
        self.canvas.create_rectangle(
            2, 2, width-2, height-2,
            fill=bg_color,
            outline='',
            tags='bg'
        )
        
        # Progress fill
        self.progress_rect = self.canvas.create_rectangle(
            2, 2, 2, height-2,
            fill=self.fill_color,
            outline='',
            tags='progress'
        )
        
    def set_progress(self, target_percent: float, animate: bool = True):
        """Set progress with animation"""
        if animate:
            self.animate_to(target_percent)
        else:
            target_width = (self.width - 4) * (target_percent / 100)
            self.canvas.coords('progress', 2, 2, target_width + 2, self.height - 2)
    
    def animate_to(self, target_percent: float):
        """Animate progress bar to target percentage"""
        def animate():
            steps = 30
            current_width = self.canvas.coords('progress')[2] - 2
            target_width = (self.width - 4) * (target_percent / 100)
            step_size = (target_width - current_width) / steps
            
            for i in range(steps):
                new_width = current_width + (step_size * (i + 1))
                self.canvas.coords('progress', 2, 2, new_width + 2, self.height - 2)
                self.canvas.update()
                time.sleep(0.02)
        
        import threading
        thread = threading.Thread(target=animate, daemon=True)
        thread.start()


class FloatingContactButton:
    """Floating contact button that sticks to screen"""
    
    def __init__(self, parent, contact_info: dict):
        self.contact_info = contact_info
        self.is_expanded = False
        
        # Main container frame
        self.frame = tk.Frame(parent, bg=COLORS['bg_primary'])
        
        # Create main floating button
        self.main_btn = tk.Button(
            self.frame,
            text='📞 Contact',
            command=self.toggle_contact,
            bg=COLORS['accent'],
            fg=COLORS['text_primary'],
            font=('Segoe UI', 12, 'bold'),
            relief='raised',
            bd=2,
            padx=15,
            pady=10,
            cursor='hand2',
            activebackground=COLORS['accent_secondary'],
        )
        self.main_btn.pack(fill='both', expand=True)
        
        # Contact details frame (hidden by default)
        self.details_frame = tk.Frame(self.frame, bg=COLORS['card_bg'], padx=10, pady=10)
        
        # Email
        tk.Label(
            self.details_frame,
            text='📧 Email:',
            bg=COLORS['card_bg'],
            fg=COLORS['text_secondary'],
            font=('Segoe UI', 9)
        ).pack(anchor='w')
        tk.Label(
            self.details_frame,
            text=self.contact_info['email'],
            bg=COLORS['card_bg'],
            fg=COLORS['text_primary'],
            font=('Segoe UI', 9)
        ).pack(anchor='w', pady=0)
        
        # Phone
        tk.Label(
            self.details_frame,
            text='📱 Phone:',
            bg=COLORS['card_bg'],
            fg=COLORS['text_secondary'],
            font=('Segoe UI', 9)
        ).pack(anchor='w')
        tk.Label(
            self.details_frame,
            text=self.contact_info['phone'],
            bg=COLORS['card_bg'],
            fg=COLORS['text_primary'],
            font=('Segoe UI', 9)
        ).pack(anchor='w', pady=0)
        
        # Location
        tk.Label(
            self.details_frame,
            text='📍 Location:',
            bg=COLORS['card_bg'],
            fg=COLORS['text_secondary'],
            font=('Segoe UI', 9)
        ).pack(anchor='w')
        tk.Label(
            self.details_frame,
            text=self.contact_info['location'],
            bg=COLORS['card_bg'],
            fg=COLORS['text_primary'],
            font=('Segoe UI', 9)
        ).pack(anchor='w', pady=0)
    
    def toggle_contact(self):
        """Toggle contact details visibility"""
        self.is_expanded = not self.is_expanded
        
        if self.is_expanded:
            self.details_frame.pack(fill='both', expand=True)
            self.main_btn.config(text='✖ Close')
        else:
            self.details_frame.pack_forget()
            self.main_btn.config(text='📞 Contact')
    
    def pack(self, **kwargs):
        self.frame.pack(**kwargs)
    
    def place(self, **kwargs):
        self.frame.place(**kwargs)


class DigitalPortfolio:
    """Main Digital Portfolio Application"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Gerald Fabre - Digital Portfolio")
        self.root.geometry("1200x800")
        self.root.configure(bg=COLORS['bg_primary'])
        
        # Set minimum size
        self.root.minsize(1000, 700)
        
        # Current section
        self.current_section = 'home'
        self.animation_speed = 0.03
        
        # Create main container
        self.create_ui()
        
        # Center window on screen
        self.center_window()
        
        # Show home section by default
        self.show_section('home')
    
    def center_window(self):
        """Center window on screen"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def create_ui(self):
        """Create the main UI"""
        # Main container
        self.main_container = tk.Frame(self.root, bg=COLORS['bg_primary'])
        self.main_container.pack(fill='both', expand=True)
        
        # Navigation bar
        self.create_navigation()
        
        # Content area
        self.content_frame = tk.Frame(self.main_container, bg=COLORS['bg_primary'])
        self.content_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Create all sections (frames)
        self.sections = {}
        self.create_sections()
        
        # Floating contact button
        self.create_floating_contact()
        
        # Bind scroll events (for potential future use)
        self.content_frame.bind('<Configure>', self.on_resize)
    
    def create_navigation(self):
        """Create navigation bar"""
        # Navigation frame
        nav_frame = tk.Frame(self.main_container, bg=COLORS['bg_secondary'], height=60)
        nav_frame.pack(fill='x')
        nav_frame.pack_propagate(False)
        
        # Logo/Name
        logo_label = tk.Label(
            nav_frame,
            text='GF',
            bg=COLORS['bg_secondary'],
            fg=COLORS['accent'],
            font=('Segoe UI', 24, 'bold')
        )
        logo_label.pack(side='left', padx=20)
        
        # Navigation buttons container
        nav_btn_frame = tk.Frame(nav_frame, bg=COLORS['bg_secondary'])
        nav_btn_frame.pack(side='right', padx=20)
        
        # Navigation items
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
                activeforeground=COLORS['text_primary'],
            )
            btn.pack(side='left')
            btn.bind('<Enter>', lambda e, b=btn: self.on_nav_hover(b, True))
            btn.bind('<Leave>', lambda e, b=btn: self.on_nav_hover(b, False))
    
    def on_nav_hover(self, button, enter):
        """Handle navigation button hover"""
        if enter:
            button.config(bg=COLORS['nav_hover'])
        else:
            button.config(bg=COLORS['bg_secondary'])
    
    def create_sections(self):
        """Create all content sections"""
        self.sections['home'] = self.create_home_section()
        self.sections['about'] = self.create_about_section()
        self.sections['skills'] = self.create_skills_section()
        self.sections['experience'] = self.create_experience_section()
        self.sections['projects'] = self.create_projects_section()
        self.sections['services'] = self.create_services_section()
    
    def create_home_section(self):
        """Create home/hero section"""
        frame = tk.Frame(self.content_frame, bg=COLORS['bg_primary'])
        
        # Main container with two columns
        main_content = tk.Frame(frame, bg=COLORS['bg_primary'])
        main_content.pack(fill='both', expand=True)
        
        # Left side - Text content
        left_frame = tk.Frame(main_content, bg=COLORS['bg_primary'])
        left_frame.pack(side='left', fill='both', expand=True)
        
        # Greeting
        greeting = tk.Label(
            left_frame,
            text='Hello, I am',
            bg=COLORS['bg_primary'],
            fg=COLORS['text_secondary'],
            font=('Segoe UI', 18)
        )
        greeting.pack(anchor='w', pady=100)
        
        # Name
        name_label = tk.Label(
            left_frame,
            text=PERSONAL_INFO['name'],
            bg=COLORS['bg_primary'],
            fg=COLORS['accent'],
            font=('Segoe UI', 48, 'bold')
        )
        name_label.pack(anchor='w')
        
        # Title
        title_label = tk.Label(
            left_frame,
            text='Developer | ML Enthusiast | Problem Solver',
            bg=COLORS['bg_primary'],
            fg=COLORS['text_primary'],
            font=('Segoe UI', 20)
        )
        title_label.pack(anchor='w', pady=10)
        
        # Short bio
        bio_label = tk.Label(
            left_frame,
            text='Passionate about building innovative solutions through\ncode and machine learning. Turning ideas into reality.',
            bg=COLORS['bg_primary'],
            fg=COLORS['text_secondary'],
            font=('Segoe UI', 14),
            justify='left'
        )
        bio_label.pack(anchor='w', pady=0)
        
        # CTA Buttons
        btn_frame = tk.Frame(left_frame, bg=COLORS['bg_primary'])
        btn_frame.pack(anchor='w')
        
        AnimatedButton(
            btn_frame,
            'View My Work',
            lambda: self.show_section('projects'),
            bg=COLORS['accent'],
            hover=COLORS['accent_secondary']
        ).pack(side='left', padx=0)
        
        AnimatedButton(
            btn_frame,
            'Contact Me',
            self.toggle_contact_float,
            bg=COLORS['bg_tertiary'],
            hover=COLORS['accent_secondary']
        ).pack(side='left')
        
        # Right side - Profile image placeholder
        right_frame = tk.Frame(main_content, bg=COLORS['bg_primary'])
        right_frame.pack(side='right', fill='both', expand=True, padx=50)
        
        # Profile image container (placeholder)
        profile_container = tk.Frame(
            right_frame,
            bg=COLORS['bg_tertiary'],
            width=300,
            height=350
        )
        profile_container.pack(pady=80)
        profile_container.pack_propagate(False)
        
        # Profile placeholder icon
        profile_placeholder = tk.Label(
            profile_container,
            text='📷\n\n[Replace with\nYour Photo]',
            bg=COLORS['bg_tertiary'],
            fg=COLORS['text_secondary'],
            font=('Segoe UI', 16),
            justify='center'
        )
        profile_placeholder.pack(fill='both', expand=True, padx=5, pady=5)
        
        # Decorative border
        border_frame = tk.Frame(profile_container, bg=COLORS['accent'], padx=3, pady=3)
        border_frame.pack(fill='both', expand=True)
        
        inner_frame = tk.Frame(border_frame, bg=COLORS['bg_tertiary'])
        inner_frame.pack(fill='both', expand=True)
        
        profile_placeholder_re = tk.Label(
            inner_frame,
            text='📷\n\n[Replace with\nYour Photo]',
            bg=COLORS['bg_tertiary'],
            fg=COLORS['text_secondary'],
            font=('Segoe UI', 16),
            justify='center'
        )
        profile_placeholder_re.pack(fill='both', expand=True, padx=10, pady=10)
        
        return frame
    
    def create_about_section(self):
        """Create about section"""
        frame = tk.Frame(self.content_frame, bg=COLORS['bg_primary'])
        
        # Title
        title = tk.Label(
            frame,
            text='About Me',
            bg=COLORS['bg_primary'],
            fg=COLORS['accent'],
            font=('Segoe UI', 36, 'bold')
        )
        title.pack(anchor='w', pady=30)
        
        # Content container
        content = tk.Frame(frame, bg=COLORS['bg_primary'])
        content.pack(fill='both', expand=True)
        
        # Left - Bio
        left = tk.Frame(content, bg=COLORS['bg_primary'])
        left.pack(side='left', fill='both', expand=True, padx=0)
        
        bio_text = """Hi! I'm Gerald Fabre, a passionate developer and lifelong learner 
based in Bukidnon, Philippines.

I have a strong interest in open source development, machine learning, 
and creating impactful solutions through technology. When I'm not coding, 
you can find me exploring new places through photography, playing games, 
or diving into a good book.

I'm currently studying at Torres Capitol College Inc. and continuously 
working on improving my skills in various areas of technology."""
        
        bio_label = tk.Label(
            left,
            text=bio_text,
            bg=COLORS['bg_primary'],
            fg=COLORS['text_secondary'],
            font=('Segoe UI', 14),
            justify='left',
            wraplength=450
        )
        bio_label.pack(anchor='w')
        
        # Right - Info cards
        right = tk.Frame(content, bg=COLORS['bg_primary'])
        right.pack(side='right', fill='both', expand=True)
        
        # Education card
        edu_card = self.create_card(
            right,
            '🎓 Education',
            [f"{e['school']} ({e['year']})" for e in PERSONAL_INFO['education']],
            COLORS['card_bg']
        )
        edu_card.pack(fill='x', pady=0)
        
        # Interests card
        interests_card = self.create_card(
            right,
            '💡 Interests',
            PERSONAL_INFO['interests'],
            COLORS['card_bg']
        )
        interests_card.pack(fill='x', pady=0)
        
        # Achievements card
        achievements_card = self.create_card(
            right,
            '🏆 Achievements',
            [f"{a['title']} - {a['year']}" for a in PERSONAL_INFO['achievements']],
            COLORS['card_bg']
        )
        achievements_card.pack(fill='x')
        
        return frame
    
    def create_skills_section(self):
        """Create skills section"""
        frame = tk.Frame(self.content_frame, bg=COLORS['bg_primary'])
        
        # Title
        title = tk.Label(
            frame,
            text='My Skills',
            bg=COLORS['bg_primary'],
            fg=COLORS['accent'],
            font=('Segoe UI', 36, 'bold')
        )
        title.pack(anchor='w', pady=30)
        
        # Skills container
        skills_container = tk.Frame(frame, bg=COLORS['bg_primary'])
        skills_container.pack(fill='both', expand=True)
        
        # Left column
        left = tk.Frame(skills_container, bg=COLORS['bg_primary'])
        left.pack(side='left', fill='both', expand=True, padx=0)
        
        # Right column
        right = tk.Frame(skills_container, bg=COLORS['bg_primary'])
        right.pack(side='right', fill='both', expand=True)
        
        # Split skills into two columns
        mid = len(PERSONAL_INFO['skills']) // 2
        left_skills = PERSONAL_INFO['skills'][:mid]
        right_skills = PERSONAL_INFO['skills'][mid:]
        
        # Left skills
        for skill in left_skills:
            self.create_skill_item(left, skill['name'], skill['level'])
        
        # Right skills
        for skill in right_skills:
            self.create_skill_item(right, skill['name'], skill['level'])
        
        return frame
    
    def create_skill_item(self, parent, skill_name: str, level: int):
        """Create a skill item with progress bar"""
        container = tk.Frame(parent, bg=COLORS['bg_primary'], pady=10)
        container.pack(fill='x')
        
        # Skill name
        name_label = tk.Label(
            container,
            text=skill_name,
            bg=COLORS['bg_primary'],
            fg=COLORS['text_primary'],
            font=('Segoe UI', 12, 'bold')
        )
        name_label.pack(anchor='w')
        
        # Progress bar container
        progress_frame = tk.Frame(container, bg=COLORS['bg_tertiary'], height=8)
        progress_frame.pack(fill='x', pady=5)
        progress_frame.pack_propagate(False)
        
        # Progress fill
        progress_fill = tk.Frame(progress_frame, bg=COLORS['accent'], width=1)
        progress_fill.pack(side='left', fill='y')
        
        # Animate progress bar
        def animate_progress(fill=progress_fill, target=level, container=progress_frame):
            fill.update_idletasks()
            max_width = container.winfo_width()
            if max_width > 1:
                target_width = max_width * (target / 100)
                steps = 20
                step_size = target_width / steps
                for i in range(steps):
                    fill.config(width=int(step_size * (i + 1)))
                    container.update()
                    time.sleep(0.02)
        
        # Schedule animation after frame is rendered
        container.after(100, animate_progress)
        
        # Percentage label
        percent_label = tk.Label(
            container,
            text=f'{level}%',
            bg=COLORS['bg_primary'],
            fg=COLORS['text_secondary'],
            font=('Segoe UI', 10)
        )
        percent_label.pack(anchor='e', pady=5)
    
    def create_experience_section(self):
        """Create experience section"""
        frame = tk.Frame(self.content_frame, bg=COLORS['bg_primary'])
        
        # Title
        title = tk.Label(
            frame,
            text='Experience',
            bg=COLORS['bg_primary'],
            fg=COLORS['accent'],
            font=('Segoe UI', 36, 'bold')
        )
        title.pack(anchor='w', pady=30)
        
        # Experience cards container using place
        exp_container = tk.Frame(frame, bg=COLORS['bg_primary'])
        exp_container.place(x=0, y=80, relwidth=1, relheight=1)
        
        # Experience cards
        for i, exp in enumerate(PERSONAL_INFO['experience']):
            card = self.create_experience_card(exp)
            card.pack(fill='x', pady=0)
        
        return frame
    
    def create_experience_card(self, experience: dict):
        """Create an experience card"""
        card = tk.Frame(
            None,
            bg=COLORS['card_bg'],
            padx=30,
            pady=25
        )
        
        # Year badge
        year_badge = tk.Label(
            card,
            text=experience['year'],
            bg=COLORS['accent'],
            fg=COLORS['text_primary'],
            font=('Segoe UI', 10, 'bold'),
            padx=10,
            pady=5
        )
        year_badge.pack(anchor='w')
        
        # Role
        role_label = tk.Label(
            card,
            text=experience['role'],
            bg=COLORS['card_bg'],
            fg=COLORS['text_primary'],
            font=('Segoe UI', 18, 'bold'),
            pady=10
        )
        role_label.pack(anchor='w')
        
        # Company
        company_label = tk.Label(
            card,
            text=experience['company'],
            bg=COLORS['card_bg'],
            fg=COLORS['accent'],
            font=('Segoe UI', 14)
        )
        company_label.pack(anchor='w')
        
        # Description
        desc_label = tk.Label(
            card,
            text=experience['description'],
            bg=COLORS['card_bg'],
            fg=COLORS['text_secondary'],
            font=('Segoe UI', 12),
            wraplength=600,
            justify='left',
            pady=10
        )
        desc_label.pack(anchor='w')
        
        return card
    
    def create_projects_section(self):
        """Create projects section"""
        frame = tk.Frame(self.content_frame, bg=COLORS['bg_primary'])
        
        # Title
        title = tk.Label(
            frame,
            text='My Projects',
            bg=COLORS['bg_primary'],
            fg=COLORS['accent'],
            font=('Segoe UI', 36, 'bold')
        )
        title.pack(anchor='w', pady=30)
        
        # Projects grid container - use place instead of pack to avoid grid conflict
        projects_grid = tk.Frame(frame, bg=COLORS['bg_primary'])
        projects_grid.place(x=0, y=0, relwidth=1, relheight=1)
        
        # Create project cards in a grid using grid manager
        for i, project in enumerate(PERSONAL_INFO['projects']):
            row = i // 2
            col = i % 2
            
            card = self.create_project_card(project)
            card.grid(row=row, column=col, padx=10, pady=10, sticky='nsew')
            # Make the card expand
            projects_grid.grid_rowconfigure(row, weight=1)
            projects_grid.grid_columnconfigure(col, weight=1)
        
        return frame
    
    def create_project_card(self, project: dict):
        """Create a project card"""
        card = tk.Frame(
            None,
            bg=COLORS['card_bg'],
            padx=20,
            pady=20
        )
        
        # Project icon
        icon_label = tk.Label(
            card,
            text='💻',
            bg=COLORS['card_bg'],
            fg=COLORS['accent'],
            font=('Segoe UI', 32)
        )
        icon_label.pack()
        
        # Project name
        name_label = tk.Label(
            card,
            text=project['name'],
            bg=COLORS['card_bg'],
            fg=COLORS['text_primary'],
            font=('Segoe UI', 16, 'bold'),
            pady=10
        )
        name_label.pack()
        
        # Description
        desc_label = tk.Label(
            card,
            text=project['description'],
            bg=COLORS['card_bg'],
            fg=COLORS['text_secondary'],
            font=('Segoe UI', 12),
            wraplength=250,
            justify='center'
        )
        desc_label.pack()
        
        # Tech stack
        tech_label = tk.Label(
            card,
            text=f"Tech: {project['tech']}",
            bg=COLORS['card_bg'],
            fg=COLORS['accent'],
            font=('Segoe UI', 10),
            pady=10
        )
        tech_label.pack()
        
        return card
    
    def create_services_section(self):
        """Create services section"""
        frame = tk.Frame(self.content_frame, bg=COLORS['bg_primary'])
        
        # Title
        title = tk.Label(
            frame,
            text='Services',
            bg=COLORS['bg_primary'],
            fg=COLORS['accent'],
            font=('Segoe UI', 36, 'bold')
        )
        title.pack(anchor='w', pady=30)
        
        # Services grid container - use place instead of pack to avoid grid conflict
        services_grid = tk.Frame(frame, bg=COLORS['bg_primary'])
        services_grid.place(x=0, y=0, relwidth=1, relheight=1)
        
        # Create service cards in a grid using grid manager
        for i, service in enumerate(PERSONAL_INFO['services']):
            row = i // 2
            col = i % 2
            
            card = self.create_service_card(service)
            card.grid(row=row, column=col, padx=10, pady=10, sticky='nsew')
            services_grid.grid_rowconfigure(row, weight=1)
            services_grid.grid_columnconfigure(col, weight=1)
        
        return frame
    
    def create_service_card(self, service: dict):
        """Create a service card"""
        card = tk.Frame(
            None,
            bg=COLORS['card_bg'],
            padx=30,
            pady=25
        )
        
        # Service icon
        icons = {'Web Development': '🌐', 'Machine Learning': '🤖', 'Consulting': '📊', 'Tutoring': '📚'}
        icon = icons.get(service['name'], '💡')
        
        icon_label = tk.Label(
            card,
            text=icon,
            bg=COLORS['card_bg'],
            fg=COLORS['accent'],
            font=('Segoe UI', 36)
        )
        icon_label.pack()
        
        # Service name
        name_label = tk.Label(
            card,
            text=service['name'],
            bg=COLORS['card_bg'],
            fg=COLORS['text_primary'],
            font=('Segoe UI', 16, 'bold'),
            pady=10
        )
        name_label.pack()
        
        # Description
        desc_label = tk.Label(
            card,
            text=service['description'],
            bg=COLORS['card_bg'],
            fg=COLORS['text_secondary'],
            font=('Segoe UI', 12),
            wraplength=250,
            justify='center'
        )
        desc_label.pack()
        
        return card
    
    def create_card(self, parent, title: str, items: list, bg_color: str):
        """Create a generic card"""
        card = tk.Frame(parent, bg=bg_color, padx=20, pady=20)
        
        # Title
        title_label = tk.Label(
            card,
            text=title,
            bg=bg_color,
            fg=COLORS['text_primary'],
            font=('Segoe UI', 14, 'bold'),
            pady=0
        )
        title_label.pack(anchor='w')
        
        # Items
        for item in items:
            item_label = tk.Label(
                card,
                text=f'• {item}',
                bg=bg_color,
                fg=COLORS['text_secondary'],
                font=('Segoe UI', 11),
                wraplength=300,
                justify='left'
            )
            item_label.pack(anchor='w', pady=0)
        
        return card
    
    def create_floating_contact(self):
        """Create floating contact button"""
        contact_info = {
            'email': PERSONAL_INFO['email'],
            'phone': PERSONAL_INFO['phone'],
            'location': PERSONAL_INFO['location'],
        }
        
        self.floating_contact = FloatingContactButton(
            self.main_container,
            contact_info
        )
        
        # Position at bottom right corner, but handle in show_section
        self.floating_btn_frame = tk.Frame(self.main_container, bg=COLORS['bg_primary'])
        self.floating_btn_frame.place(relx=0.98, rely=0.95, anchor='se')
        
        # Create main floating button
        self.float_btn = tk.Button(
            self.floating_btn_frame,
            text='📞 Contact',
            command=self.toggle_contact_float,
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
        self.float_btn.pack()
        
        # Contact details popup (initially hidden)
        self.contact_popup = tk.Frame(self.main_container, bg=COLORS['card_bg'], padx=20, pady=20)
        
        # Email
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
        ).pack(anchor='w', pady=0)
        
        # Phone
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
        ).pack(anchor='w', pady=0)
        
        # Location
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
        ).pack(anchor='w', pady=0)
        
        self.contact_popup_visible = False
    
    def toggle_contact_float(self):
        """Toggle floating contact popup"""
        self.contact_popup_visible = not self.contact_popup_visible
        
        if self.contact_popup_visible:
            self.contact_popup.place(relx=0.98, rely=0.85, anchor='se')
            self.float_btn.config(text='✖ Close')
        else:
            self.contact_popup.place_forget()
            self.float_btn.config(text='📞 Contact')
    
    def show_section(self, section_name: str):
        """Show a specific section with animation"""
        # Hide all sections
        for section in self.sections.values():
            section.pack_forget()
        
        # Show selected section
        if section_name in self.sections:
            # Animate fade in
            self.animate_section(self.sections[section_name])
            self.sections[section_name].pack(fill='both', expand=True)
            self.current_section = section_name
    
    def animate_section(self, frame):
        """Simple animation for section appearance"""
        # Just a placeholder for potential fade-in effects
        frame.update_idletasks()
    
    def on_resize(self, event):
        """Handle window resize"""
        self.center_window()


class ScrollableFrame:
    """Scrollable frame container"""
    
    def __init__(self, parent, *args, **kwargs):
        self.parent = parent
        self.bg_color = kwargs.get('bg', COLORS['bg_primary'])
        
        # Create canvas
        self.canvas = tk.Canvas(
            parent,
            bg=self.bg_color,
            highlightthickness=0,
            *args,
            **kwargs
        )
        
        # Scrollbar
        self.scrollbar = ttk.Scrollbar(
            parent,
            orient='vertical',
            command=self.canvas.yview
        )
        self.scrollbar.pack(side='right', fill='y')
        
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.pack(side='left', fill='both', expand=True)
        
        # Create frame inside canvas
        self.scrollable_frame = tk.Frame(self.canvas, bg=self.bg_color)
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor='nw')
        
        self.scrollable_frame.bind(
            '<Configure>',
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox('all'))
        )
    
    def get_frame(self):
        """Get the scrollable frame"""
        return self.scrollable_frame


def main():
    """Main entry point"""
    root = tk.Tk()
    
    # Set window icon (optional - requires an icon file)
    # root.iconbitmap('icon.ico')
    
    # Create portfolio
    app = DigitalPortfolio(root)
    
    # Run main loop
    root.mainloop()


if __name__ == '__main__':
    main()