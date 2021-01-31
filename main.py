import wx
from classes.class_main_window import MainWindow


def main():

    app = wx.App()
    ex = MainWindow(None, title='Image Folder Generator - V3')
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()


# TODO create the settings frame and various options for that
# TODO - FITS header keywords for Lights/Darks/Flats
# TODO Swap the LKistBox for a Tree Controla nd rework to add roots/children
