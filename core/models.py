from django.db import models

# project page
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models. TextField()
    github_link = models.URLField(blank=True)

    def __str__(self):
        return self.title
    

# Skills page 
class Skill(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(
        max_length=10,
        help_text="Emoji icon, e.g. 🐍, 🐳, ☁️ "
    )
    level = models.CharField(
        max_length=50,
        choices=[
            ('Beginner', 'Beginner'),
            ('Intermediate', 'Intermediate'),
            ('Advanced', 'Advanced'),
            ('Expert', 'Expert'),

        ]
    )
    def __str__(self):
        return self.name