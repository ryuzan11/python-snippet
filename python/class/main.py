
class School:

    def __init__(self, name):
        self.__name = name

    def get_school_name(self):
        return f'{self.__name} School'


class Student(School):
    time_to_go_home = '18:00'

    def __init__(self, school_name, name):
        super().__init__(school_name)
        self.__name = name
        self.__hobby = list()

    # クラス変数を読み込む
    @classmethod
    def get_class_time_to_go_home(cls):
        return cls.time_to_go_home

    # インスタンス変数は定義していない場合、同名のクラス変数を読み込む
    def get_instance_time_to_go_home(self):
        return self.time_to_go_home

    def get_student_name(self):
        return f'{self.__name} Kun'

    def get_student_hobby(self):
        return self.__hobby

    def set_student_hobby(self, hobby):
        self.__hobby.append(hobby)
        return


def main():
    """
    python python/class/main.py

    # クラス変数とインスタンス変数
    https://qiita.com/kxphotographer/items/60588b7c747094eba9f1

    :return:
    """

    # クラス変数を直接読み込む
    print(Student.get_class_time_to_go_home())
    # クラスのインスタンス化
    school_name = 'mita'
    student_name = 'taro'
    taro = Student(school_name, student_name)
    print(taro.get_school_name())
    print(taro.get_student_name())

    # 定義されていないインスタンス変数を呼ぼうとすると、同名のクラス変数を参照する
    print('クラス変数を読み込む：', taro.get_class_time_to_go_home())
    print('インスタンス変数がないので、同名のクラス変数を読み込む：', taro.get_instance_time_to_go_home())

    # getterとsetter
    print(taro.get_student_hobby())
    hobby = 'soccer'
    taro.set_student_hobby(hobby)
    print(taro.get_student_hobby())

    # TODO もう一つ下位のクラスを作成し、上位のクラスを上書きした場合どうなるか


main()
