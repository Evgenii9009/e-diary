def fix_marks(schoolkid):
    marks = Mark.objects.filter(schoolkid=schoolkid, points__in=[1, 2, 3])
    for mark in marks:
        mark.points = 5
        mark.save()
    return None


def remove_chastisements(schoolkid):
    schoolkid_chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    for chastisement in schoolkid_chastisements:
        chastisement.delete()
    return None


def create_commendation(name, subject):
    schoolkid = Schoolkid.objects.get(full_name__contains=name)
    schoolkid_subject = Subject.objects.get(title=subject, year_of_study=schoolkid.year_of_study)
    lessons = Lesson.objects.filter(year_of_study=schoolkid.year_of_study, group_letter=schoolkid.group_letter, subject=schoolkid_subject)
    last_lesson = lessons.order_by('date').reverse()[0]
    Commendation.objects.create(text='Молодец!', created=last_lesson.date, schoolkid=schoolkid, subject=schoolkid_subject, teacher=last_lesson.teacher)
    return None

