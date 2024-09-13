import time
class User:
    """
    Каждый объект класса User должен обладать следующими атрибутами и методами:
    Атриубуты: nickname(имя пользователя, строка), password(в хэшированном виде, число), age(возраст, число)
    """
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age
        #print(f'Привет, меня зовут: {self.nickname}, мой возраст : {self.age}.')
    def __str__(self):
        return f'{self.nickname}'

class Video:
    """
    Каждый объект класса Video должен обладать следующими атрибутами и методами:
    Атриубуты: title(заголовок, строка), duration(продолжительность, секунды),
    time_now(секунда остановки (изначально 0)), adult_mode(ограничение по возрасту, bool (False по умолчанию))

    """
    def __init__(self, title, duration, time_now = 0, adult_mode = False ):
        self.title = str(title)
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode
        #print(f'title : {self.title}, duration  : {self.duration}, time now: {self.time_now}, Mode - ', {self.adult_mode})

class UrTube:
    """
    Атриубты: users(список объектов User), videos(список объектов Video), current_user(текущий пользователь, User)
    """
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    """
    Метод log_in, который принимает на вход аргументы: nickname, password и пытается найти пользователя в users 
    с такими же логином и паролем. Если такой пользователь существует, то current_user меняется на найденного. 
    Помните, что password передаётся в виде строки, а сравнивается по хэшу.
    """
    def log_in(self, nickname, password):
        hash_password = hash(password)
        for user in self.users:
            if user.nickname == nickname and user.password == hash_password:
                self.current_user = user
            print('Ошибочка в логине / пароле.....')

    """
    Метод register, который принимает три аргумента: nickname, password, age, и добавляет пользователя в список, 
    если пользователя не существует (с таким же nickname). Если существует, выводит на экран: 
    "Пользователь {nickname} уже существует". 
    После регистрации, вход выполняется автоматически.
    """
    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f'Пользователь <{nickname}> уже существует')
                return
        hash_password = hash(password)
        newuser = User(nickname=nickname, password=hash_password, age=age)
        self.users.append(newuser)
        self.current_user = newuser

    """
    Метод log_out для сброса текущего пользователя на None
    """
    def log_out(self):
        self.current_user = None

    """
    Метод add, который принимает неограниченное кол-во объектов класса Video и все добавляет в videos, 
    если с таким же названием видео ещё не существует. В противном случае ничего не происходит.
    """

    def add(self, *args):
        for new_video in args:
            flag_ = True
            for video in self.videos:
                if video.title == new_video.title:
                    flag_ = False
                    break
            if flag_:
                self.videos.append(new_video)
            else:
                print(f'Видео с названием "{new_video.title}" уже существует.')

    """
    Метод get_videos, который принимает поисковое слово и возвращает список названий всех видео, 
    содержащих поисковое слово. Следует учесть, что слово 'UrbaN' присутствует в строке 
    'Urban the best' (не учитывать регистр).
    """
    def get_videos(self, search_word):
        search_list = []
        for k in self.videos:
            if search_word.lower() in k.title.lower():
                search_list.append(k.title)
        return search_list

    """
    Метод watch_video, который принимает название фильма, если не находит точного совпадения(вплоть до пробела),
    то ничего не воспроизводится, если же находит - ведётся отчёт в консоль на какой секунде ведётся просмотр. 
    После текущее время просмотра данного видео сбрасывается.
    """

    def watch_video(self, name_video):
        if self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео.')
            return
        video_found = False
        for k in self.videos:
            if k.title == name_video:
                video_found = True
                if self.current_user.age < 18 and k.adult_mode:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    return
                for _time in range(1, k.duration + 1):
                    print(_time, end=' ')
                    time.sleep(1)
                print('Конец видео')
                break
        if not video_found:
            print('Такого видео не существует')



if __name__ == '__main__':
    # name = "Alex"
    # psw = "1234"
    # age = 20
    # example_User = User(name, psw, age)
    # example_video = Video('T2', 2, 15, adult_ := True)

    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)
    # print(ur.videos)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')