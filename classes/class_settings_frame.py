import wx
from classes.class_config import AppConfig

LABEL_WIDTH = 100
TEXT_WIDTH = 80


class SettingsWindow(wx.Dialog):

    def __init__(self, parent, title='Settings'):
        super(SettingsWindow, self).__init__(parent, title=title, style=wx.DEFAULT_FRAME_STYLE)

        self.Config = AppConfig()
        self.InitUI()
        self.Centre()

    def InitUI(self):
        """ Initialise Controls """
        self.panel = wx.Panel(self)
        outer_sizer = wx.BoxSizer(wx.VERTICAL)

        fits_box = wx.StaticBox(self.panel, wx.ID_ANY, 'FITS Keywords')
        fits_sizer = wx.StaticBoxSizer(fits_box, wx.VERTICAL)

        #chkUseFits = wx.CheckBox(self.panel, wx.ID_ANY, 'Use FITS IMAGETYP')
        lbl1 = wx.StaticText(self.panel, wx.ID_ANY, 'Light Frames:', size=(LABEL_WIDTH, -1),
                             style=wx.ALIGN_RIGHT)
        lbl2 = wx.StaticText(self.panel, wx.ID_ANY, 'Dark Frames:', size=(LABEL_WIDTH, -1),
                             style=wx.ALIGN_RIGHT)
        lbl3 = wx.StaticText(self.panel, wx.ID_ANY, 'Flat Frames:', size=(LABEL_WIDTH, -1),
                             style=wx.ALIGN_RIGHT)
        lbl4 = wx.StaticText(self.panel, wx.ID_ANY, 'Bias Frames:', size=(LABEL_WIDTH, -1),
                             style=wx.ALIGN_RIGHT)
        lbl5 = wx.StaticText(self.panel, wx.ID_ANY, 'FlatDark Frames:', size=(LABEL_WIDTH, -1),
                             style=wx.ALIGN_RIGHT)
        textLight = wx.TextCtrl(self.panel, wx.ID_ANY, size=(TEXT_WIDTH, -1))
        textDark = wx.TextCtrl(self.panel, wx.ID_ANY, size=(TEXT_WIDTH, -1))
        textFlat = wx.TextCtrl(self.panel, wx.ID_ANY, size=(TEXT_WIDTH, -1))
        textBias = wx.TextCtrl(self.panel, wx.ID_ANY, size=(TEXT_WIDTH, -1))
        textFlatDark = wx.TextCtrl(self.panel, wx.ID_ANY, size=(TEXT_WIDTH, -1))

        light_sizer = wx.BoxSizer(wx.HORIZONTAL)
        dark_sizer = wx.BoxSizer(wx.HORIZONTAL)
        flat_sizer = wx.BoxSizer(wx.HORIZONTAL)
        bias_sizer = wx.BoxSizer(wx.HORIZONTAL)
        fl_dark_sizer = wx.BoxSizer(wx.HORIZONTAL)

        light_sizer.Add(lbl1, 0, wx.RIGHT | wx.TOP, 2)
        light_sizer.Add(textLight, 1, wx.RIGHT, 5)
        fits_sizer.Add(light_sizer, 1, wx.TOP | wx.EXPAND, 10)

        dark_sizer.Add(lbl2, 0, wx.RIGHT | wx.TOP, 2)
        dark_sizer.Add(textDark, 1, wx.RIGHT, 5)
        fits_sizer.Add(dark_sizer, 1, wx.TOP | wx.EXPAND, 10)

        flat_sizer.Add(lbl3, 0, wx.RIGHT | wx.TOP, 2)
        flat_sizer.Add(textFlat, 1, wx.RIGHT, 5)
        fits_sizer.Add(flat_sizer, 1, wx.TOP | wx.EXPAND, 10)

        bias_sizer.Add(lbl4, 0, wx.RIGHT | wx.TOP, 2)
        bias_sizer.Add(textBias, 1, wx.RIGHT, 5)
        fits_sizer.Add(bias_sizer, 1, wx.TOP | wx.EXPAND, 10)

        fl_dark_sizer.Add(lbl5, 0, wx.RIGHT | wx.TOP, 2)
        fl_dark_sizer.Add(textFlatDark, 1, wx.RIGHT, 5)
        fits_sizer.Add(fl_dark_sizer, 1, wx.TOP | wx.EXPAND, 10)

        outer_sizer.Add(fits_sizer, 1, wx.ALL | wx.EXPAND, 10)

        #############################
        # Pack the self.panel and then Fit
        #############################
        self.panel.SetSizer(outer_sizer)
        self.panel.Fit()
        self.Fit()