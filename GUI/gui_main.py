"""
Graphical user interface required for task 9.
Rudimentary first version calls existing scripts and plots results.
(Future version should combine scripts' behavior to avoid redundant processing.)
"""
import os
import tkinter as tk
from tkinter import filedialog
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import webbrowser
import task1, task2, task3, task4, task5, task67


"""
Plans:
    Main GUI window which opens new windows for processing and plotting different tasks
        Select a file to use as dataset
        Calculate task 1-8 (new window, main remains open)
    Each window has options to...
        Calculate and plot with currently chosen dataset
        Save calculated dataset or figures
        Close window (clear memory?)
"""

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.master = kwargs['master']
        self.create_frames()

    def create_frames(self):
        self.frm_plots = tk.Frame(self, relief=tk.SUNKEN, borderwidth=5)
        self.frm_info = tk.Frame(self)
        self.frm_plots.pack(side=tk.LEFT, fill='both', expand=True)
        self.frm_info.pack(side=tk.RIGHT)

        self.msg_info = tk.Message(self.frm_info, text='Task description')
        self.msg_info.pack(side='top', fill='both', expand=True)

    def save_file(self):
        return filedialog.asksaveasfilename(initialdir="./", title="Save results", filetypes=(("PNG files","*.png"),("all files","*.*")))

class MainMenu(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.master = kwargs['master']
        self.pack()

        self.filename = ''
        self.results = ''

        self.container = tk.Frame(self, height=400)
        self.container.pack(side='top', fill='both', expand=True)
        self.controls = tk.Frame(self, height=25, relief='ridge', borderwidth=5)
        self.controls.pack(anchor='s', fill='x', expand=True)

        self.p1 = Page1(master=self.container)
        self.p2 = Page2(master=self.container)
        self.p3 = Page3(master=self.container)
        self.p4 = Page4(master=self.container)
        self.p5 = Page5(master=self.container)
        self.p6 = Page6(master=self.container)
        #self.p7 = Page7(master=self.container)
        self.p8 = Page8(master=self.container)
        self.info = InfoPage(master=self.container)

        self.p1.place(in_=self.container, x=0, y=0, relwidth=1, relheight=1)
        self.p2.place(in_=self.container, x=0, y=0, relwidth=1, relheight=1)
        self.p3.place(in_=self.container, x=0, y=0, relwidth=1, relheight=1)
        self.p4.place(in_=self.container, x=0, y=0, relwidth=1, relheight=1)
        self.p5.place(in_=self.container, x=0, y=0, relwidth=1, relheight=1)
        self.p6.place(in_=self.container, x=0, y=0, relwidth=1, relheight=1)
        #self.p7.place(in_=self.container, x=0, y=0, relwidth=1, relheight=1)
        self.p8.place(in_=self.container, x=0, y=0, relwidth=1, relheight=1)
        self.info.place(in_=self.container, x=0, y=0, relwidth=1, relheight=1)

        self.create_widgets()

        self.lift()

    def load_data(self):
        self.filename = filedialog.askopenfilename(initialdir = './', title='Load dataset', filetypes=(("text", "*.txt"), ("all files", "*.*")))
        print(self.filename)

    def create_widgets(self):
        self.frm_btn_top = tk.Frame(self.controls, background='#c0c4cc')
        self.frm_btn_bottom = tk.Frame(self.controls, background='#c0c4cc')
        self.frm_btn_top.pack(side='top', fill='x', )
        self.frm_btn_bottom.pack(side='bottom', fill='x')

        self.btn_task1 = tk.Button(self.frm_btn_top, width=10, text='Task 1', highlightbackground='#c0c4cc', command=self.p1.lift)
        self.btn_task1.pack(side='left')

        self.btn_task2 = tk.Button(self.frm_btn_top, width=10, text='Task 2', highlightbackground='#c0c4cc', command=self.p2.lift)
        self.btn_task2.pack(side='left')

        self.btn_task3 = tk.Button(self.frm_btn_top, width=10, text='Task 3', highlightbackground='#c0c4cc', command=self.p3.lift)
        self.btn_task3.pack(side='left')

        self.btn_task4 = tk.Button(self.frm_btn_top, width=10, text='Task 4', highlightbackground='#c0c4cc', command=self.p4.lift)
        self.btn_task4.pack(side='left')

        self.btn_task5 = tk.Button(self.frm_btn_bottom, width=10, text='Task 5', highlightbackground='#c0c4cc', command=self.p5.lift)
        self.btn_task5.pack(side='left')

        self.btn_task6 = tk.Button(self.frm_btn_bottom, width=10, text='Task 6 & 7', highlightbackground='#c0c4cc', command=self.p6.lift)
        self.btn_task6.pack(side='left')

        #self.btn_task7 = tk.Button(self.frm_btn_bottom, width=10, fg='gray', text='Task 7', highlightbackground='#c0c4cc', command=self.p7.lift)
        #self.btn_task7.pack(side='left')

        self.btn_task8 = tk.Button(self.frm_btn_bottom, width=10, text='Task 8', highlightbackground='#c0c4cc', command=self.p8.lift)
        self.btn_task8.pack(side='left')

        self.btn_info = tk.Button(self.frm_btn_top, width=10, text='Info', highlightbackground='#c0c4cc', command=self.info.lift)
        self.btn_info.pack(side='right')

        self.btn_load = tk.Button(self.frm_btn_top, width=10, text='Load dataset', highlightbackground='#c0c4cc', command=self.load_data)
        self.btn_load.pack(side='right')

        self.btn_quit = tk.Button(self.frm_btn_bottom, width=10, text="QUIT", highlightbackground='#c0c4cc', command=root.destroy)
        self.btn_quit.pack(side='right')


class Page1(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.desc = 'Task 1\n\nDraw a histogram of thirty most frequent words in a corpus.\n'
        self.msg_info['text'] = self.desc
        self.btn_calc = tk.Button(self.frm_info, width=10, text='Calculate', command=self.calculate)
        self.btn_calc.pack(side='bottom')
        self.btn_save = tk.Button(self.frm_info, width=10, text='Save figure', command=self.plot_save)
        self.btn_save.pack(side='bottom')

    def calculate(self):
        if app.filename:
            path, dataset = os.path.split(app.filename)
            self.plt = task1.main(path, dataset)

            clear_frame(self.frm_plots)
            self.canvas = FigureCanvasTkAgg(self.plt, self.frm_plots)
            self.canvas.draw()
            self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
            
        else:
            self.msg_info['text'] = self.desc + '\nERROR: No dataset loaded\n'

    def plot_save(self):
        try:
            print(self.plt)
            save_as = self.save_file()
            self.plt.savefig(save_as)
        except (AttributeError, NameError):
            self.msg_info['text'] = self.desc + '\nERROR: Plot not calculated\n'

class Page2(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.desc = 'Task 2\n\nPlot Zipf\'s law associated to whole corpus.\n'
        self.msg_info['text'] = self.desc
        self.btn_calc = tk.Button(self.frm_info, width=10, text='Calculate', command=self.calculate)
        self.btn_calc.pack(side='bottom')
        self.btn_save = tk.Button(self.frm_info, width=10, text='Save figure', command=self.plot_save)
        self.btn_save.pack(side='bottom')

    def calculate(self):
        if app.filename:
            path, dataset = os.path.split(app.filename)
            self.plt = task2.main(path, dataset)
            
            clear_frame(self.frm_plots)
            self.canvas = FigureCanvasTkAgg(self.plt, self.frm_plots)
            self.canvas.draw()
            self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
            
        else:
            self.msg_info['text'] = self.desc + '\nERROR: No dataset loaded\n'

    def plot_save(self):
        try:
            print(self.plt)
            save_as = self.save_file()
            self.plt.savefig(save_as)
        except (AttributeError, NameError):
            self.msg_info['text'] = self.desc + '\nERROR: Plot not calculated\n'


class Page3(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.desc = 'Task 3\n\nQuantify the goodness of fit for Zipf\'s law at 80%-95% confidence levels.\n'
        self.msg_info['text'] = self.desc
        self.btn_calc = tk.Button(self.frm_info, width=10, text='Calculate', command=self.calculate)
        self.btn_calc.pack(side='bottom')
        self.btn_save = tk.Button(self.frm_info, width=10, text='Save figure', command=self.plot_save)
        self.btn_save.pack(side='bottom')

    def calculate(self):
        if app.filename:
            path, dataset = os.path.split(app.filename)
            self.plt = task3.main(path, dataset)
            
            clear_frame(self.frm_plots)
            self.canvas = FigureCanvasTkAgg(self.plt, self.frm_plots)
            self.canvas.draw()
            self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
            
        else:
            self.msg_info['text'] = self.desc + '\nERROR: No dataset loaded\n'

    def plot_save(self):
        try:
            print(self.plt)
            save_as = self.save_file()
            self.plt.savefig(save_as)
        except (AttributeError, NameError):
            self.msg_info['text'] = self.desc + '\nERROR: Plot not calculated\n'

class Page4(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.desc = 'Task 4\n\nQuery two opposing topics from corpus. Output the articles which matched queries best.\n'
        self.msg_info['text'] = self.desc
        self.btn_calc = tk.Button(self.frm_info, width=10, text='Calculate', command=self.calculate)
        self.btn_calc.pack(side='bottom')
        self.btn_save = tk.Button(self.frm_info, width=10, text='Save articles', command=self.query_save)
        self.btn_save.pack(side='bottom')
        self.frm_entry = tk.Frame(self.frm_info)
        self.frm_entry.pack(side='bottom')
        self.lbl_e1 = tk.Label(self.frm_entry, text='1st Query')
        self.lbl_e2 = tk.Label(self.frm_entry, text='2nd Query')
        self.entry1 = tk.Entry(self.frm_entry)
        self.entry2 = tk.Entry(self.frm_entry)
        self.lbl_e1.grid(row=0, column=0)
        self.entry1.grid(row=0, column=1)
        self.lbl_e2.grid(row=1, column=0)
        self.entry2.grid(row=1, column=1)


    def calculate(self):
        if app.filename:
            if self.entry1.get() and self.entry2.get():
                path, dataset = os.path.split(app.filename)
                self.article_1, self.article_2 = task4.main(path, dataset, self.entry1.get(), self.entry2.get())
                msg_out = tk.Message(self.frm_plots, text=self.entry1.get() + ':\n' + self.article_1[:500] + '...\n\n' + self.entry2.get() + ':\n' + self.article_2[:500] + '...\n')
                msg_out.pack(fill='both')
            else:
                self.msg_info['text'] = self.desc + '\nERROR: Topic(s) for query missing\n'
        else:
            self.msg_info['text'] = self.desc + '\nERROR: No dataset loaded\n'

    def query_save(self):
        try:
            print(self.article_1[0], self.article_2[0])
            save_as = filedialog.asksaveasfilename(initialdir="./", title="Save first article", filetypes=(("text files","*.txt"),("all files","*.*")))
            with open(save_as, "w", encoding= "utf-8") as f:
                f.write(self.article_1)

            save_as = filedialog.asksaveasfilename(initialdir="./", title="Save second article", filetypes=(("text files","*.txt"),("all files","*.*")))
            with open(save_as, "w", encoding= "utf-8") as f:
                f.write(self.article_2)
            
        except (AttributeError, NameError):
            self.msg_info['text'] = self.desc + '\nERROR: Query not calculated\n'

class Page5(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.desc = 'Task 5\n\nConsider a vocabulary of the 1000 most frequent words for each task 4 queries. Explore the behavior of vocabulary for each query\'s outcome.\nPlot frequency vs rank for both.\n'
        self.msg_info['text'] = self.desc
        self.data1 = None
        self.data2 = None

        self.e1 = tk.Entry(self.frm_info)
        self.e2 = tk.Entry(self.frm_info)
        self.btn_open1 = tk.Button(self.frm_info, width=5, text='Open', command=self.open1)
        self.btn_open2 = tk.Button(self.frm_info, width=5, text='Open', command=self.open2)
        self.btn_calc = tk.Button(self.frm_info, width=10, text='Calculate', command=self.calculate)
        self.btn_calc.pack(side='bottom')
        self.btn_save = tk.Button(self.frm_info, width=10, text='Save figure', command=self.plot_save)
        self.btn_save.pack(side='bottom')
        self.btn_open2.pack(side='bottom', anchor='e')
        self.e2.pack(fill='x', side='bottom')
        self.btn_open1.pack(side='bottom', anchor='e')
        self.e1.pack(fill='x', side='bottom')

    def open1(self):
        self.data1 = filedialog.askopenfilename(initialdir='./', title='Load dataset', filetypes=(("text", "*.txt"), ("all files", "*.*")))
        self.e1.insert(0, self.data1)

    def open2(self):
        self.data2 = filedialog.askopenfilename(initialdir='./', title='Load dataset', filetypes=(("text", "*.txt"), ("all files", "*.*")))
        self.e2.insert(0, self.data2)

    def calculate(self):
        if self.data1 and self.data2:
            path, set1 = os.path.split(self.data1)
            _, set2 = os.path.split(self.data2)
            self.plt = task5.main(path, set1, set2)
            
            clear_frame(self.frm_plots)
            self.canvas = FigureCanvasTkAgg(self.plt, self.frm_plots)
            self.canvas.draw()
            self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
            
        else:
            self.msg_info['text'] = self.desc + '\nERROR: No dataset loaded\n'

    def plot_save(self):
        try:
            print(self.plt)
            save_as = self.save_file()
            self.plt.savefig(save_as)
        except (AttributeError, NameError):
            self.msg_info['text'] = self.desc + '\nERROR: Plot not calculated\n'

class Page6(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.desc = 'Tasks 6 and 7\n\nInvestigate the common wording between V1 and V2. Report the value of Jaccard similarity J(V1,V2).\nAnalyze the variation of common word with respect to frequency.\n'
        self.msg_info['text'] = self.desc
        self.data1 = None
        self.data2 = None

        self.e1 = tk.Entry(self.frm_info)
        self.e2 = tk.Entry(self.frm_info)
        self.btn_open1 = tk.Button(self.frm_info, width=5, text='Open', command=self.open1)
        self.btn_open2 = tk.Button(self.frm_info, width=5, text='Open', command=self.open2)
        self.btn_calc = tk.Button(self.frm_info, width=10, text='Calculate', command=self.calculate)
        self.btn_calc.pack(side='bottom')
        self.btn_save = tk.Button(self.frm_info, width=10, text='Save figure', command=self.plot_save)
        self.btn_save.pack(side='bottom')
        self.btn_open2.pack(side='bottom', anchor='e')
        self.e2.pack(fill='x', side='bottom')
        self.btn_open1.pack(side='bottom', anchor='e')
        self.e1.pack(fill='x', side='bottom')

    def open1(self):
        self.data1 = filedialog.askopenfilename(initialdir='./', title='Load article', filetypes=(("text", "*.txt"), ("all files", "*.*")))
        self.e1.insert(0, self.data1)

    def open2(self):
        self.data2 = filedialog.askopenfilename(initialdir='./', title='Load article', filetypes=(("text", "*.txt"), ("all files", "*.*")))
        self.e2.insert(0, self.data2)

    def calculate(self):
        if self.data1 and self.data2:
            path, set1 = os.path.split(self.data1)
            _, set2 = os.path.split(self.data2)
            jaccard, self.plt = task67.main(path, set1, set2)
            self.msg_info['text'] = '{}\nJaccard distance between texts is {}\n'.format(self.desc, round(jaccard, 4))
            
            clear_frame(self.frm_plots)
            self.canvas = FigureCanvasTkAgg(self.plt, self.frm_plots)
            self.canvas.draw()
            self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
            
        else:
            self.msg_info['text'] = self.desc + '\nERROR: No dataset loaded\n'

    def plot_save(self):
        try:
            print(self.plt)
            save_as = self.save_file()
            self.plt.savefig(save_as)
        except (AttributeError, NameError):
            self.msg_info['text'] = self.desc + '\nERROR: Plot not calculated\n'

"""
class Page7(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.desc = 'Task 7\n\nThis is currently just a placeholder.\nIf same calculations are already done for task6, they should be grouped together.\n'
        self.msg_info['text'] = self.desc
        #self.btn_calc = tk.Button(self.frm_info, width=10, text='Calculate', command=self.calculate)
        #self.btn_calc.pack(side='bottom')
        #self.btn_save = tk.Button(self.frm_info, width=10, text='Save figure', command=self.plot_save)
        #self.btn_save.pack(side='bottom')

    
    def calculate(self):
        if app.filename:
            path, dataset = app.filename.rsplit('/', 1)
            self.plt = task3.main(path, dataset)
            
            self.canvas = FigureCanvasTkAgg(self.plt, self.frm_plots)
            self.canvas.draw()
            self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
            
        else:
            self.msg_info['text'] = self.desc + '\nERROR: No dataset loaded\n'

    def plot_save(self):
        try:
            print(self.plt)
            save_as = self.save_file()
            self.plt.savefig(save_as)
        except (AttributeError, NameError):
            self.msg_info['text'] = self.desc + '\nERROR: Plot not calculated\n'
"""

class Page8(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.desc = 'Task 8\n\nFind out the categories of wording available in common vocabulary.\nUse the general inquirer provided to identify the categories present in vocabularies.\n'
        self.msg_info['text'] = self.desc
        #self.btn_calc = tk.Button(self.frm_info, width=10, text='Calculate', command=self.calculate)
        #self.btn_calc.pack(side='bottom')
        #self.btn_save = tk.Button(self.frm_info, width=10, text='Save figure', command=self.plot_save)
        #self.btn_save.pack(side='bottom')

    """
    def calculate(self):
        if app.filename:
            path, dataset = app.filename.rsplit('/', 1)
            self.plt = task3.main(path, dataset)
            
            self.canvas = FigureCanvasTkAgg(self.plt, self.frm_plots)
            self.canvas.draw()
            self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
            
        else:
            self.msg_info['text'] = self.desc + '\nERROR: No dataset loaded\n'

    def plot_save(self):
        try:
            print(self.plt)
            save_as = self.save_file()
            self.plt.savefig(save_as)
        except (AttributeError, NameError):
            self.msg_info['text'] = self.desc + '\nERROR: Plot not calculated\n'
    """

class InfoPage(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.master = kwargs['master']
        self.pack()
        desc = 'Group info:\n    Aapo Juutinen, Project leader\n    Eetu Ervasti\n    Niklas Riikonen\n\nProject topic:\n    Zipf Law and validation 2\n    Testing Zipf\'s law on a large scale WikiCorpus.'
        self.msg_info = tk.Message(self, text=desc, width=350, borderwidth=10)
        self.msg_info.pack(fill='both', pady='100')
        body = 'mailto: ?to=***REMOVED***, ***REMOVED***, ***REMOVED***&subject=521158S Group project'
        self.btn_contact = tk.Button(self, text='Contact', width=10, command=lambda: webbrowser.open(body, new=1))
        self.btn_contact.pack()


def clear_frame(frm):
    for widget in frm.winfo_children():
        widget.destroy()


root = tk.Tk()
app = MainMenu(master=root)
app.pack(fill='both', expand=True)
root.wm_geometry("1024x720")
app.mainloop()
