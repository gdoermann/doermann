from django.db import models
from django.contrib.auth.models import User
from limbo.models import TrackedModel

class Section(TrackedModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    description = models.TextField(blank=True)
    link = models.URLField(blank=True, null=True)
    order = models.SmallIntegerField(default=1)

    def __str__(self):
        return self.name


    class Meta:
        abstract=True
        ordering = ('order',)


class RangeSection(Section):
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    location = models.ForeignKey('ContactInfo')

    class Meta:
        abstract=True
        ordering = ('order',)


class LEVEL:
    NATIVE = 'native'
    FLUENT = 'fluent'
    BASIC = 'basic'
    CHOICES = (
        (NATIVE, NATIVE.title()),
        (FLUENT, FLUENT.title()),
        (BASIC, BASIC.title()),
    )

class Language(models.Model):
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=30, choices=LEVEL.CHOICES)


class SkillHeading(Section):
    pass

class Skill(Section):
    skill_heading = models.ForeignKey(SkillHeading)
    projects = models.ManyToManyField('Project', null=True, blank=True)
    experience = models.CharField(max_length=200)
    proficiency = models.IntegerField(default=0)

    def __str__(self):
        return self.skill_heading.name + ": " + super(Skill, self).__str__()

class Project(RangeSection):
    pass

class WorkExperience(RangeSection):
    title = models.CharField(max_length=100)
    company_link = models.URLField(blank=True, null=True)

class Responsibility(Section):
    work_experience = models.ForeignKey(WorkExperience)

    def __str__(self):
        return self.work_experience.name + ": " + self.description[:50] + "..."

class Education(RangeSection):
    degree = models.CharField(max_length=200, blank=True)
    minor = models.CharField(max_length=100, blank=True)

class CourseWork(Section):
    education = models.ForeignKey(Education)

class ContactInfo(TrackedModel):
    street = models.CharField(max_length=30, blank=True)
    city = models.CharField(max_length=30, blank=True)
    province = models.CharField(max_length=30, blank=True)
    zipcode = models.CharField(max_length=5, blank=True, null=True)
    country = models.CharField(max_length=30, blank=True)
    phone = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.city

class ContactAccount(TrackedModel):
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=200)
    icon = models.CharField(max_length=100)

class UserProfile(TrackedModel):
    user = models.ForeignKey(User)
    address = models.ForeignKey(ContactInfo)
    current_activities = models.TextField()
    bio = models.TextField(blank=True)

    def __str__(self):
        return "Profile: " + self.user.username

class ResumeProfile(TrackedModel):
    name = models.CharField(max_length=200)

    skill_headings = models.ManyToManyField(SkillHeading)
    skills = models.ManyToManyField(Skill)
    projects = models.ManyToManyField(Project)
    work_experience = models.ManyToManyField(WorkExperience)
    responsibilities = models.ManyToManyField(Responsibility)
    education = models.ManyToManyField(Education)
    course_work = models.ManyToManyField(CourseWork)
    languages = models.ManyToManyField(Language)

    def __str__(self):
        return "Resume: " + self.name
