import wx
import configparser


class MainWindow(wx.Frame):

    def __init__(self, parent, title):
        super(MainWindow, self).__init__(parent, title=title, style=wx.DEFAULT_FRAME_STYLE)

        self.InitUI()
        self.Centre()

    def InitUI(self):
        """ Build the main window controls """

        panel = wx.Panel(self)
        outer_sizer = wx.BoxSizer(wx.HORIZONTAL)

        src_label = wx.StaticText(panel, wx.ID_ANY, 'Source Folder', size=(100, -1),
                                  style=wx.ALIGN_RIGHT)
        src_text = wx.TextCtrl(panel, wx.ID_ANY)
        dest_label = wx.StaticText(panel, wx.ID_ANY, 'Destination Folder', size=(100, -1),
                                   style=wx.ALIGN_RIGHT)
        dest_text = wx.TextCtrl(panel, wx.ID_ANY, size=(300, -1))

        inout_box = wx.StaticBox(panel, wx.ID_ANY, 'Source and Destination')
        inout_sizer = wx.StaticBoxSizer(inout_box, wx.VERTICAL)

        source_sizer = wx.BoxSizer(wx.HORIZONTAL)
        dest_sizer = wx.BoxSizer(wx.HORIZONTAL)

        source_sizer.Add(src_label, 0, wx.ALL, 10)
        source_sizer.Add(src_text, 1, wx.ALL, 10)
        dest_sizer.Add(dest_label, 0, wx.ALL, 10)
        dest_sizer.Add(dest_text, 1, wx.ALL, 10)

        inout_sizer.Add(source_sizer, 1, wx.ALL | wx.EXPAND, 10)
        inout_sizer.Add(dest_sizer, 1, wx.ALL | wx.EXPAND, 10)

        outer_sizer.Add(inout_sizer, 1, wx.ALL | wx.EXPAND, 10)

        panel.SetSizer(outer_sizer)
        panel.Fit()
        self.Fit()
