def fix_marks(name):
    schoolkid = get_schoolkid(name)
    marks = Mark.objects.filter(schoolkid=schoolkid, points__in=[1, 2, 3]).update(points=5)
    return None


def remove_chastisements(name):
    schoolkid = get_schoolkid(name)
    chastisements = Chastisement.objects.filter(schoolkid=schoolkid).delete()
    return None


def create_commendation(name, subject):
    schoolkid = get_schoolkid(name)
    schoolkid_subject = Subject.objects.get_object_or_404(title=subject, year_of_study=schoolkid.year_of_study)
    lessons = Lesson.objects.filter(year_of_study=schoolkid.year_of_study, group_letter=schoolkid.group_letter, subject=schoolkid_subject)
    last_lesson = lessons.order_by('date').last()
    if last_lesson:
        last_lesson = lessons.order_by('date').last()
    else:
        print('Урок не найден!')
    Commendation.objects.create(text='Молодец!', created=last_lesson.date, schoolkid=schoolkid, subject=schoolkid_subject, teacher=last_lesson.teacher)
    return None


def get_schoolkid(name):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=name)
    except Schoolkid.MultipleObjectsReturned:
        print('Уточните введённые данные')
    return schoolkid