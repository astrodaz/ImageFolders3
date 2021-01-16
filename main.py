import wx
from classes.class_main_window import MainWindow


def main():

    app = wx.App()
    ex = MainWindow(None, title='Image Folder Generator - V3')
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
