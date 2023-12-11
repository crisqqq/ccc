import tkinter as tk
from views import AboutFrame
from views import ChangeFrame,InsertFrame,SearchFrame,DeleteFrame



class MianPage:
    def __init__(self,master:tk.Tk):
        self.root = master
        self.root.title('用户管理系统 V0.0.1')
        self.root.geometry('600x400')
        self.create_page()

    def create_page(self):

        self.about_frame = AboutFrame(self.root)
        #tk.Label(self.about_frame, text='作者信息：本作品由TK制作').pack()
        #tk.Label(self.about_frame, text='作品信息：信息管理系统').pack()
        #tk.Label(self.about_frame, text='联系信息：1000000').pack()

        self.change_frame = ChangeFrame(self.root)
        #tk.Label(self.change_frame, text='修改信息').pack()

        self.insert_frame = InsertFrame(self.root)
        self.search_frame = SearchFrame(self.root)
        self.delete_frame = DeleteFrame(self.root)



        menubar = tk.Menu(self.root)

        menubar.add_command(label='查询',command=self.show_search)
        menubar.add_command(label='录入', command=self.show_insert)
        menubar.add_command(label='删除',command=self.show_delete)
        menubar.add_command(label='修改',command=self.show_change)
        menubar.add_command(label='关于',command=self.show_about)
        self.root['menu'] = menubar



    def show_insert(self):
        self.about_frame.pack_forget()
        self.insert_frame.pack()
        self.delete_frame.pack_forget()
        self.search_frame.pack_forget()
        self.change_frame.pack_forget()



    def show_search(self):
        self.about_frame.pack_forget()
        self.insert_frame.pack_forget()
        self.delete_frame.pack_forget()
        self.search_frame.pack()
        self.change_frame.pack_forget()


    def show_delete(self):
        self.about_frame.pack_forget()
        self.insert_frame.pack_forget()
        self.delete_frame.pack()
        self.search_frame.pack_forget()
        self.change_frame.pack_forget()


    def show_change(self):
        self.about_frame.pack_forget()
        self.insert_frame.pack_forget()
        self.delete_frame.pack_forget()
        self.search_frame.pack_forget()
        self.change_frame.pack()


    def show_about(self):
        self.about_frame.pack()
        self.insert_frame.pack_forget()
        self.delete_frame.pack_forget()
        self.search_frame.pack_forget()
        self.change_frame.pack_forget()












if __name__ == '__main__':
    root = tk.Tk()
    MianPage(master=root)
    root.mainloop()