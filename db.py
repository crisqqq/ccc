import json


class MysqlDatabases:
    def __init__(self):
        with open('users.json',mode='r',encoding='utf-8')as f:
            text=f.read()
        self.users = json.loads(text)

        with open('students.json',mode='r',encoding="utf-8")as F:
            text2=F.read()
        self.students = json.loads(text2)
    def check_login(self,username,password):
        for user in self.users:
            if username == user['username']:
                if password == user['password']:
                    return True, '登陆成功'
                else:
                    return False, '登录失败，密码错误'
        return False,'登录失败，用户不存在'

    def all(self):
        return self.students

    def insert(self,student):
        self.students.append(student)

    def delete_by_username(self,name):
        for student in self.students:
            print(student)
            if student['name']==name:
                self.students.remove(student)
                return True,f'{name}用户删除成功'
        return False, f'{name}用户不存在'


    def search_by_username(self,name):
        for student in self.students:
            if student['name']==name:
                return True,student
        return False, f'{name}用户不存在'

    def update(self,stu):
        for student in self.students:
            if student['name']==stu['name']:
                student.update(stu)
                return True,f'{stu["name"]} 用户数据修改成功'
        return False, f'{stu["name"]}用户不存在'




db = MysqlDatabases()
if __name__ == '__main__':
    #print(db.check_login('admin','123456'))
    #print(db.all())
    print(db.search_by_username('张三'))