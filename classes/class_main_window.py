import wx


class MainWindow(wx.Frame):

    def __init__(self, parent, title):
        super(MainWindow, self).__init__(parent, title=title, style=wx.DEFAULT_FRAME_STYLE)

        self.InitUI()
        self.Centre()

    def InitUI(self):
        """ Build the main window controls """

        self.panel = wx.Panel(self)
        outer_sizer = wx.BoxSizer(wx.VERTICAL)

        ########################
        # Source and Destination
        ########################
        src_label = wx.StaticText(self.panel, wx.ID_ANY, '&Source Folder', size=(100, -1),
                                  style=wx.ALIGN_RIGHT)
        self.src_text = wx.TextCtrl(self.panel, wx.ID_ANY)
        dest_label = wx.StaticText(self.panel, wx.ID_ANY, 'Des&tination Folder', size=(100, -1),
                                   style=wx.ALIGN_RIGHT)
        self.dest_text = wx.TextCtrl(self.panel, wx.ID_ANY, size=(200, -1))
        src_choose = wx.Button(self.panel, wx.ID_ANY, '...', style=wx.BU_EXACTFIT)
        destination_choose = wx.Button(self.panel, wx.ID_ANY, '...', style=wx.BU_EXACTFIT)
        src_tip = wx.ToolTip('Select the source folder')
        dest_tip = wx.ToolTip('Select the top level destination folder')
        src_choose.SetToolTip(src_tip)
        destination_choose.SetToolTip(dest_tip)

        # SRC and DESTINATION have separate sizers
        inout_box = wx.StaticBox(self.panel, wx.ID_ANY, 'Source and Destination')
        inout_sizer = wx.StaticBoxSizer(inout_box, wx.VERTICAL)

        source_sizer = wx.BoxSizer(wx.HORIZONTAL)
        dest_sizer = wx.BoxSizer(wx.HORIZONTAL)

        source_sizer.Add(src_label, 0, wx.RIGHT | wx.TOP, 5)
        source_sizer.Add(self.src_text, 1, wx.RIGHT, 5)
        source_sizer.Add(src_choose, 0, wx.RIGHT, 5)

        dest_sizer.Add(dest_label, 0, wx.RIGHT | wx.TOP, 5)
        dest_sizer.Add(self.dest_text, 1, wx.RIGHT, 5)
        dest_sizer.Add(destination_choose, 0, wx.RIGHT, 5)

        inout_sizer.Add(source_sizer, 1, wx.ALL | wx.EXPAND, 5)
        inout_sizer.Add(dest_sizer, 1, wx.ALL | wx.EXPAND, 5)

        #############
        # Sub Folders
        #############
        folders_box = wx.StaticBox(self.panel, wx.ID_ANY, '&Folders')
        folders_sizer = wx.StaticBoxSizer(folders_box, wx.HORIZONTAL)

        # Add the bitmap buttons
        self.lstFolders = wx.ListBox(self.panel)
        bmp = wx.ArtProvider.GetBitmap(wx.ART_GO_UP, wx.ART_BUTTON, (16, 16))
        up_id = wx.NewId()
        self.btnFolderUp = wx.BitmapButton(self.panel, up_id, bitmap=bmp,)
        bmp = wx.ArtProvider.GetBitmap(wx.ART_GO_DOWN, wx.ART_BUTTON, (16, 16))
        self.btnFolderDown = wx.BitmapButton(self.panel, wx.ID_ANY, bitmap=bmp)
        bmp = wx.ArtProvider.GetBitmap(wx.ART_PLUS, wx.ART_BUTTON, (16, 16))
        add_id = wx.NewId()
        self.btnAdd = wx.BitmapButton(self.panel, add_id, bitmap=bmp)
        bmp = wx.ArtProvider.GetBitmap(wx.ART_MINUS, wx.ART_BUTTON, (16, 16))
        rem_id = wx.NewId()
        self.btnRem = wx.BitmapButton(self.panel, rem_id, bitmap=bmp)

        # These have a separate sizer so that the list control sizes properly
        # and the buttons can stack vertically
        f_buttons_sizer = wx.BoxSizer(wx.VERTICAL)
        f_buttons_sizer.Add(self.btnAdd, 0, wx.ALL, 5)
        f_buttons_sizer.Add(self.btnRem, 0, wx.ALL, 5)
        f_buttons_sizer.Add(self.btnFolderUp, 0, wx.ALL, 5)
        f_buttons_sizer.Add(self.btnFolderDown, 0, wx.ALL, 5)

        # The list control sizer
        list_folder_sizer = wx.BoxSizer(wx.HORIZONTAL)
        list_folder_sizer.Add(self.lstFolders, 3, wx.ALL | wx.EXPAND, 5)

        # Then add both sizers to the Folder sizer
        folders_sizer.Add(list_folder_sizer, 1, wx.ALL | wx.EXPAND, 5)
        folders_sizer.Add(f_buttons_sizer, 0, wx.ALL, 5)

        ####################
        # Run / Exit Buttons
        ####################
        buttons_box = wx.StaticBox(self.panel, wx.ID_ANY)
        buttons_sizer = wx.StaticBoxSizer(buttons_box, wx.HORIZONTAL)
        button_go = wx.Button(self.panel, wx.ID_ANY, '&Run')
        button_exit = wx.Button(self.panel, wx.ID_ANY, 'E&xit')

        buttons_sizer.Add(button_go, 1, wx.ALL , 10)
        buttons_sizer.Add(button_exit, 1, wx.ALL , 10)

        ##############################################
        # Pack the outer sizer with the other 3 sizers
        ##############################################
        outer_sizer.Add(inout_sizer, 1, wx.ALL | wx.EXPAND, 10)
        outer_sizer.Add(folders_sizer, 2, wx.LEFT | wx.RIGHT | wx.BOTTOM | wx.EXPAND, 10)
        outer_sizer.Add(wx.StaticText(self.panel, wx.ID_ANY, 'ALT+A or D to Add or Delete '
                                                             'folders, ALT+Up or Down arrow to '
                                                             'move'), 0, wx.CENTER, 20)
        outer_sizer.Add(buttons_sizer, 0, wx.LEFT | wx.RIGHT | wx.BOTTOM | wx.EXPAND, 10)

        #######################
        # Button Event Bindings
        #######################
        self.Bind(wx.EVT_BUTTON, self.close_program, button_exit)
        self.Bind(wx.EVT_BUTTON, self.run, button_go)
        self.Bind(wx.EVT_BUTTON, self.add_folder, self.btnAdd)
        self.Bind(wx.EVT_MENU, self.add_folder, id=add_id)
        self.Bind(wx.EVT_BUTTON, self.remove_folder, self.btnRem)
        self.Bind(wx.EVT_MENU, self.remove_folder, id=rem_id)
        self.Bind(wx.EVT_BUTTON, self.folder_up, self.btnFolderUp)
        self.Bind(wx.EVT_BUTTON, self.folder_down, self.btnFolderDown)
        self.Bind(wx.EVT_BUTTON, self.choose_src, src_choose)
        self.Bind(wx.EVT_BUTTON, self.choose_dest, destination_choose)
        self.Bind(wx.EVT_LISTBOX, self.listClicked, self.lstFolders)
        self.Bind(wx.EVT_MENU, self.folder_up, id=up_id)

        self.ac_tbl = wx.AcceleratorTable([
            (wx.ACCEL_ALT, ord('A'), add_id),
            (wx.ACCEL_ALT, ord('M'), rem_id),
            (wx.ACCEL_ALT, wx.WXK_UP, up_id)
        ])
        self.SetAcceleratorTable(self.ac_tbl)

        #############################
        # Pack the self.panel and then Fit
        #############################
        self.panel.SetSizer(outer_sizer)
        self.panel.Fit()
        self.Fit()
        self.initial_UI()

    def initial_UI(self):
        self.load_values()
        self.btnRem.Enable(False)
        self.btnFolderDown.Enable(False)
        self.btnFolderUp.Enable(False)

    def load_values(self):
        """
        Load saved values from config
        """
        self.lstFolders.Append('First')
        self.UpdateUI()

    def UpdateUI(self):
        print(self.lstFolders.GetSelection())
        if self.lstFolders.Count == 0:
            self.btnRem.Enable(False)
            self.btnFolderUp.Enable(False)
            self.btnFolderDown.Enable(True)
        elif self.lstFolders.Count == 1:
            self.btnFolderUp.Enable(False)
            self.btnFolderDown.Enable(True)

    def close_program(self, event):
        """ Exit """
        self.Close()

    def run(self, event):
        """ Run """

    def add_folder(self, event):
        """ Add folder
            Update the Config with the folder 
        """
        new_folder = wx.TextEntryDialog(self.panel, 'Enter the folder name', 'Add New Folder')
        if new_folder.ShowModal() == wx.ID_OK:
            self.lstFolders.Append(new_folder.GetValue())
            #self.lstFolders.SetSelection(self.lstFolders.Count-1)
        self.UpdateUI()
            
    def remove_folder(self, event):
        """ remove folder """
        confirm = wx.MessageBox(
            f'Confirm you want to remove the folder ' 
            f'{self.lstFolders.GetString(self.lstFolders.GetSelection())}?',
            'Confirm Deletion', wx.OK | wx.CANCEL | wx.ICON_EXCLAMATION)
        if confirm == wx.OK:
            self.lstFolders.Delete(self.lstFolders.GetSelection())
            if self.lstFolders.Count > 0:
                self.lstFolders.SetSelection(self.lstFolders.Count - 1)
        self.UpdateUI()
        
    def folder_up(self, event):
        """ move folder up """
        print('Folder up')

    def folder_down(self, event):
        """ move folder down """

    def choose_src(self, event):
        """ Select the source folder
            Read the Config object to get the starting point
        """
        dialog = wx.DirDialog(self.panel, 
                              message='Select the Source directory',
                              style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dialog.ShowModal() == wx.ID_OK:
            self.src_text.SetValue(dialog.GetPath())
        # self.UpdateUI()

    def choose_dest(self, event):
        """ Select the source folder
            Read the Config object to get the starting point
        """
        dialog = wx.DirDialog(self.panel,
                              message='Select the Destination directory',
                              style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dialog.ShowModal() == wx.ID_OK:
            self.dest_text.SetValue(dialog.GetPath())
        # self.UpdateUI()

    def listClicked(self, event):
        sel = self.lstFolders.GetSelection()
        self.btnRem.Enable(True)
        if self.lstFolders.GetCount() > 1:
            if sel == 0:
                self.btnFolderUp.Enable(False)
                self.btnFolderDown.Enable(True)
            elif sel == self.lstFolders.GetCount() - 1:
                self.btnFolderUp.Enable(True)
                self.btnFolderDown.Enable(False)
            else:
                self.btnFolderUp.Enable(True)
                self.btnFolderDown.Enable(True)
        else:
            self.btnFolderUp.Enable(False)
            self.btnFolderDown.Enable(False)