def fix_marks(name):
    schoolkid = get_schoolkid(name)
    marks = Mark.objects.filter(schoolkid=schoolkid, points__in=[1, 2, 3]).update(points=5)


def remove_chastisements(name):
    schoolkid = get_schoolkid(name)
    chastisements = Chastisement.objects.filter(schoolkid=schoolkid).delete()


def create_commendation(name, subject):
    schoolkid = get_schoolkid(name)
    try:
        schoolkid_subject = Subject.objects.get(title=subject, year_of_study=schoolkid.year_of_study)
    except Subject.DoesNotExist:
        print('Предмет не найден, уточните название')
    except Subject.MultipleObjectsReturned:
        print('Найдено больше одного предмета, уточните название')
    lessons = Lesson.objects.filter(year_of_study=schoolkid.year_of_study, group_letter=schoolkid.group_letter, subject=schoolkid_subject)
    last_lesson = lessons.order_by('date').last()
    if last_lesson:
        Commendation.objects.create(text='Молодец!', created=last_lesson.date, schoolkid=schoolkid, subject=schoolkid_subject, teacher=last_lesson.teacher)
    else:
        print('Урок не найден!')


def get_schoolkid(name):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=name)
    except Schoolkid.MultipleObjectsReturned:
        print('Найдено несколько учеников, уточните ФИО')
    except Schoolkid.DoesNotExist:
        print('Ученик не найден, уточните ФИО')
    return schoolkid
