#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
import pathlib
import platform
import subprocess
import sys
import time

import PyQt5
import yaml
from PyQt5 import QtWidgets, QtCore

import ht_gui_main
import ht_gui_init
import ht_gui_loading
import ht_gui_setting
import ht_gui_theme_select
import ht_gui_help
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
import configparser

cfg_file = './ht_cfg.ini'
path_flag = 1


class dispose_ini:

    def __init__(self, filepath):
        self._path = filepath
        self.config = configparser.ConfigParser()
        self.config.read(filepath, encoding='utf-8')

    def get_sections(self):
        sect = self.config.sections()
        return sect

    def get_options(self, sec):
        return self.config.options(sec)

    def get_items(self, sec):
        return self.config.items(sec)

    def get_option(self, sec, opt):
        res = self.config.get(sec, opt)

        return res

    def write(self):
        with open(self._path, 'w') as fp:
            self.config.write(fp)

    def add_section(self, sec):
        self.config.add_section(sec)
        self.write()

    def set_option(self, sec, opt, value):
        self.config.set(sec, opt, value)
        self.write()  # 鍐欏叆鏂囦欢

    def remove_sec(self, sec):
        self.config.remove_section(sec)
        self.write()  # 鍐欏叆鏂囦欢

    def remove_opt(self, sec, opt):
        self.config.remove_option(sec, opt)
        self.write()  # 鍐欏叆鏂囦欢


dis = dispose_ini(cfg_file)


def path_trans(path_str=""):
    if path_flag != 1:
        return path_str
    return str(path_str).replace('/', '\\')


class help_dialog(QtWidgets.QDialog):

    def __init__(self, parent=None):
        super(help_dialog, self).__init__(parent)
        self.ui = ht_gui_help.Ui_Dialog()
        self.ui.setupUi(self)


class loading_dialog(QtWidgets.QDialog):

    def __init__(self, parent=None, content=""):
        super(loading_dialog, self).__init__(parent)
        self.setWindowFlags(
            PyQt5.QtCore.Qt.Dialog | PyQt5.QtCore.Qt.FramelessWindowHint | PyQt5.QtCore.Qt.Tool | PyQt5.QtCore.Qt.WindowStaysOnTopHint)
        self.setStyleSheet('background-color: #f0f0f0;')
        self.setAttribute(PyQt5.QtCore.Qt.WA_TranslucentBackground)
        self.ui = ht_gui_loading.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.tload.setText(content)


class theme_select_dialog(QtWidgets.QDialog):
    themes_list = []
    select_theme = ""

    def __init__(self, parent=None):
        super(theme_select_dialog, self).__init__(parent)
        self.ui = ht_gui_theme_select.Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.themes_list.clear()
        hexo_root = dis.get_option('hexo_init_cfg', 'hexo_root')
        for item in pathlib.Path(hexo_root + "themes").iterdir():
            if item.is_dir():
                self.themes_list.append(f"{item}".split("\\")[-1])
        self.ui.lw_theme.clear()
        self.ui.lw_theme.addItems(self.themes_list)

    def accept(self) -> None:
        self.select_theme = f"{self.themes_list[self.ui.lw_theme.currentIndex().row()]}"
        dis.set_option('hexo_tmp_arg', 'tmp_selected_theme', self.select_theme)
        self.done(1)

    def reject(self) -> None:
        self.done(0)


class setting_dialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(setting_dialog, self).__init__(parent)
        self.ui = ht_gui_setting.Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

        try:
            self.ui.le_note.setText(dis.get_option('hexo_exe_cfg', 'note_exe'))
            self.ui.le_md.setText(dis.get_option('hexo_exe_cfg', 'md_exe'))
            self.ui.le_web.setText(dis.get_option('hexo_exe_cfg', 'web_exe'))
        except:
            pass

    def select_def(self):
        self.ui.le_note.setText("notepad")
        self.ui.le_md.setText("notepad")
        self.ui.le_web.setText("msedge")

    def select_note_exe(self):
        filename, filetype = QFileDialog.getOpenFileName(None, "为[文本文件]选择程序", filter="exe(*.exe);;all(*.*)")
        if len(str(filename).strip()) != 0:
            self.ui.le_note.setText(filename)

    def select_md_exe(self):
        filename, filetype = QFileDialog.getOpenFileName(None, "为[md文件]选择程序", filter="exe(*.exe);;all(*.*)")
        if len(str(filename).strip()) != 0:
            self.ui.le_md.setText(filename)

    def select_web_exe(self):
        filename, filetype = QFileDialog.getOpenFileName(None, "为[预览网页]选择程序", filter="exe(*.exe);;all(*.*)")
        if len(str(filename).strip()) != 0:
            self.ui.le_web.setText(filename)

    def accept(self) -> None:
        dis.set_option('hexo_exe_cfg', 'note_exe', self.ui.le_note.text())
        dis.set_option('hexo_exe_cfg', 'md_exe', self.ui.le_md.text())
        dis.set_option('hexo_exe_cfg', 'web_exe', self.ui.le_web.text())
        self.done(1)

    def reject(self) -> None:
        self.done(0)


class hexo_init_dialog(QtWidgets.QDialog):

    def __init__(self, parent=None):
        super(hexo_init_dialog, self).__init__(parent)
        self.ui = ht_gui_init.Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

    def select_init_folder(self):
        init_path = QFileDialog.getExistingDirectory(None, "閫夊彇hexo鍒濆§嬪寲鐨勬牴鏂囦欢澶¹", "")
        self.ui.le_path.setText(init_path)

    def accept(self) -> None:
        dis.set_option('hexo_init_cfg', 'hexo_save_folder', self.ui.le_save.text())
        dis.set_option('hexo_init_cfg', 'hexo_save_folder_root', str(self.ui.le_path.text()).split(':')[0] + ":")
        dis.set_option('hexo_init_cfg', 'hexo_save_path_root', self.ui.le_path.text())
        dis.set_option('hexo_init_cfg', 'github_repo', self.ui.le_github.text())
        dis.set_option('hexo_init_cfg', 'hexo_root', "{}/{}/".format(self.ui.le_path.text(), self.ui.le_save.text()))
        self.done(1)

    def reject(self) -> None:
        self.done(0)


class hexo_tool_main_win(QMainWindow):
    cfg_name = r"_config.yml"
    note_exe_name = r""
    md_exe_name = r""
    web_exe_name = r""

    def __init__(self, parent=None):
        super(hexo_tool_main_win, self).__init__(parent)
        self.ui = ht_gui_main.Ui_MainWindow()
        self.ui.setupUi(self)

        self.setFixedSize(self.width(), self.height())

        ver_str = str(self.run_cmd("hexo -v")).split("\n")[0]
        self.ui.tb_hexo_version.setText(ver_str)

        self.ui.lb_init_info.setStyleSheet("QLabel{color:green;}")

        if not os.path.exists(cfg_file):
            f = open(cfg_file, 'w', encoding='utf-8')
            f.close()
            dis.add_section('hexo_init_cfg')
            dis.add_section('hexo_exe_cfg')
        try:
            self.get_def_exe()
            self.ui.le_hexo_roo_path.setText(dis.get_option('hexo_init_cfg', 'hexo_root'))
        except:
            pass

    def show_setting(self):
        set = setting_dialog()
        if set.exec() == 1:
            self.get_def_exe()

    def get_def_exe(self):
        self.note_exe_name = dis.get_option('hexo_exe_cfg', 'note_exe')
        self.md_exe_name = dis.get_option('hexo_exe_cfg', 'md_exe')
        self.web_exe_name = dis.get_option('hexo_exe_cfg', 'web_exe')

    def show_version(self):
        QMessageBox.information(self, 'About', "3hex \n v1.0.1")

    def pre_init_more_info(self):
        QMessageBox.information(self, 'Detail', self.run_cmd("hexo -v"))

    def pre_init_install_hexo(self):
        self.run_cmd("start" + " " + self.web_exe_name + " https://hexo.io/zh-cn/docs/index.html")

    def change_hexo_root(self):
        root_path = QFileDialog.getExistingDirectory(None, "选择Hexo切换到", "")
        if len(str(root_path).replace("/", "").strip()) != 0:
            save_folder = str(root_path).split('/')[-1]
            save_folder_root = str(root_path).split(':')[0]
            save_path_root = str(root_path).replace("/" + save_folder, "")
            hexo_root = str(root_path) + "/"

            dis.set_option('hexo_init_cfg', 'hexo_save_folder', save_folder)
            dis.set_option('hexo_init_cfg', 'hexo_save_folder_root', save_folder_root)
            dis.set_option('hexo_init_cfg', 'hexo_save_path_root', save_path_root)
            dis.set_option('hexo_init_cfg', 'github_repo', "")
            dis.set_option('hexo_init_cfg', 'hexo_root', hexo_root)

            self.ui.le_hexo_roo_path.setText(hexo_root)

    def init_hexo(self):
        init_dialog = hexo_init_dialog()
        if init_dialog.exec() != 1:
            return

        hexo_root = dis.get_option('hexo_init_cfg', 'hexo_root')
        github_repo = dis.get_option('hexo_init_cfg', 'github_repo')

        if not os.path.exists(path_trans(hexo_root)):
            os.mkdir(path_trans(hexo_root))

        self.ui.le_hexo_roo_path.setText(hexo_root)

        if len(str(github_repo).strip()) == 0:
            self.ui.te_exe_info.append("[info]hexo init开始初始化，请耐心等待")
            self.ui.lb_init_info.setText("init...")
            self.ui.lb_init_info.setStyleSheet("QLabel{color:red;}")
            QMessageBox.information(self, '提示', "开始[hexo init]\n点击[确定]继续")

            self.run_cmd("hexo init {}".format(hexo_root))

            self.ui.te_exe_info.append("[info]hexo init完成")
            self.ui.lb_init_info.setText("ready")
            self.ui.lb_init_info.setStyleSheet("QLabel{color:green;}")
        else:
            self.ui.te_exe_info.append("[info]hexo init开始，开始clone目标repo")

            cd_cwd = '''cd {} ;'''.format(hexo_root)

            with open('mps_hexo_init_from_git.mps1', 'r', encoding='utf-8') as f:
                cmd = f.read()
                cmd = cmd.replace('@@cd_cwd', cd_cwd)
                cmd = cmd.replace('@@git_repo', github_repo)
                cmd = cmd.replace('@@repo_name', github_repo.split('/')[-1][0:-4])
                with open('ps_hexo_init_from_git.ps1', 'w', encoding='gbk') as f2:
                    f2.write(cmd)
            self.run_cmd('start powershell ./ps_hexo_init_from_git.ps1')


    def modify_hexo_base_cfg(self):
        hexo_root = dis.get_option('hexo_init_cfg', 'hexo_root')
        self.run_cmd("start" + " " + self.note_exe_name + " " + path_trans(hexo_root + self.cfg_name))

    def modify_hexo_theme_cfg(self):
        theme_select = theme_select_dialog()
        if theme_select.exec() == 1:
            hexo_root = dis.get_option('hexo_init_cfg', 'hexo_root')
            select_theme = dis.get_option('hexo_tmp_arg', 'tmp_selected_theme')
            cfg_path = path_trans(hexo_root + "themes/" + select_theme + "/" + self.cfg_name)
            if os.path.exists(cfg_path):
                self.run_cmd("start" + " " + self.note_exe_name + " " + cfg_path)
            else:
                QMessageBox.warning(self, "提示", "[{}]主题未找到配置文件".format(select_theme))

    def open_root_explorer(self):
        hexo_root = dis.get_option('hexo_init_cfg', 'hexo_root')
        self.run_cmd("explorer " + path_trans(hexo_root))

    def init_page(self):
        self.ui.te_exe_info.append("[info]hexo开始初始化默认page(about、tags、categories)")
        QMessageBox.information(self, '提示', "开始[hexo new page(about、tags、categories)]\n点击[确定]继续")

        hexo_root = dis.get_option('hexo_init_cfg', 'hexo_root')
        cd_cwd = '''cd {} ;'''.format(hexo_root)
        # about
        if self.ui.cb_inti_page_about.isChecked():
            if not os.path.exists(hexo_root + 'source/about/index.md'):
                self.run_cmd(cd_cwd + 'hexo new page --path about/index "About_me"')
            else:
                QMessageBox.warning(self, "提示", "about已经存在")
                self.ui.te_exe_info.append("[info]about已经存在")
        # tags
        if self.ui.cb_init_page_tags.isChecked():
            if not os.path.exists(hexo_root + 'source/tags/index.md'):
                self.run_cmd(cd_cwd + 'hexo new page "tags"')
                self.tc_part('tags')
            else:
                QMessageBox.warning(self, "提示", "tags已经存在")
                self.ui.te_exe_info.append("[info]tags已经存在")
        # categories
        if self.ui.cb_inti_page_categories.isChecked():
            if not os.path.exists(hexo_root + 'source/categories/index.md'):
                self.run_cmd(cd_cwd + 'hexo new page "categories"')
                self.tc_part('categories')
            else:
                QMessageBox.warning(self, "提示", "categories已经存在")
                self.ui.te_exe_info.append("[info]categories已经存在")

    def tc_part(self, ftype=''):
        if ftype != '':
            hexo_root = dis.get_option('hexo_init_cfg', 'hexo_root')
            with open(hexo_root + "source/{}/index.md".format(ftype), 'r+') as f:
                init_content = f.read()
                new_content = init_content.replace('title: {}'.format(ftype), 'title: tags\nlayout: "{}"'.format(ftype))
            with open(hexo_root + "source/{}/index.md".format(ftype), 'r+') as f2:
                f2.write(new_content)

    def create_blog(self):
        blog_name = self.ui.le_blog_name.text().encode('gbk').decode('gbk')

        hexo_root = dis.get_option('hexo_init_cfg', 'hexo_root')
        cd_cwd = '''cd {} ;'''.format(hexo_root)

        with open('mps_new_blog.mps1', 'r', encoding='utf-8') as f:
            cmd = f.read()
            cmd = cmd.replace('@@cd_cwd', cd_cwd)
            cmd = cmd.replace('@@blog_name', blog_name)
            cmd = cmd.replace('@@md_exe_name', self.md_exe_name)
            cmd = cmd.replace('@@blog_path', "{}{}/{}.md".format(hexo_root, 'source/_posts', blog_name))
            with open('ps_new_blog.ps1', 'w', encoding='gbk') as f2:
                f2.write(cmd)
        self.run_cmd('start powershell ./ps_new_blog.ps1')

    def show_all_blog(self):
        hexo_root = dis.get_option('hexo_init_cfg', 'hexo_root')
        self.run_cmd("explorer " + path_trans(hexo_root + 'source/_posts/'))

    def modify_about_page(self):
        hexo_root = dis.get_option('hexo_init_cfg', 'hexo_root')
        for item in pathlib.Path(hexo_root + "source/about/").iterdir():
            if item.is_file() and len(str(item).strip()) != 0:
                about_page_path = hexo_root + "source/about/" + f'{item.name}'
                self.run_cmd('start ' + self.md_exe_name + ' ' + about_page_path)
                break

    def local_deploy(self):
        clean_cache_cmd = '''hexo clean ;'''
        if os.path.exists('./local_deploy.ps1'):
            self.run_cmd('''gps | ? {$_.mainwindowtitle -like 'hexo'} | stop-process''')
            self.run_cmd('''gps | ? {$_.mainwindowtitle -like 'hexo'} | stop-process''')

        hexo_root = dis.get_option('hexo_init_cfg', 'hexo_root')
        if not self.ui.cb_local_deploy_clean_cache.isChecked():
            clean_cache_cmd = ''''''

        cd_cwd = '''cd {} ;'''.format(hexo_root)
        with open('mps_local_deploy.mps1', 'r', encoding='utf-8') as f:
            cmd = f.read()
            cmd = cmd.replace('@@cd_cwd', cd_cwd)
            cmd = cmd.replace('@@clean_cache', clean_cache_cmd)
            with open('ps_local_deploy.ps1', 'w', encoding='utf-8') as f2:
                f2.write(cmd)
        self.run_cmd('start powershell .\ps_local_deploy.ps1')

        if self.ui.cb_local_deploy_auto_preview.isChecked():
            self.run_cmd("start" + " " + self.web_exe_name + " http://localhost:4000/")

    def to_top(self, select=False):
        if not select:
            self.setWindowFlags(QtCore.Qt.Widget)
        else:
            self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.show()

    def git_push(self):
        hexo_root = dis.get_option('hexo_init_cfg', 'hexo_root')
        cd_cwd = '''cd {} ;'''.format(hexo_root)

        data = yaml.load(open(hexo_root + '_config.yml', 'r'), Loader=yaml.FullLoader)
        repo = data['deploy']['repo']
        if len(str(repo).strip()) != 0:
            with open('mps_deploy.mps1', 'r', encoding='utf-8') as f:
                cmd = f.read()
                cmd = cmd.replace('@@cd_cwd', cd_cwd)
                with open('ps_deploy.ps1', 'w', encoding='utf-8') as f2:
                    f2.write(cmd)
            self.ui.te_exe_info.append('[info]开始部署到github,请耐心等待')
            self.run_cmd(r'start powershell .\ps_deploy.ps1')

    def help(self):
        help_win = help_dialog()
        help_win.exec()

    def hexo_web(self):
        self.run_cmd("start" + " " + self.web_exe_name + " https://hexo.io/zh-cn/")

    def hexo_theme_web(self):
        self.run_cmd("start" + " " + self.web_exe_name + " https://hexo.io/themes/")

    def hexo_official_introduce_web(self):
        self.run_cmd("start" + " " + self.web_exe_name + " https://hexo.io/zh-cn/docs/index.html")

    def run_cmd(self, cmd_str=""):
        time_str = time.strftime('%H:%M:%S', time.localtime(int(time.time())))

        proc = subprocess.Popen(args='''powershell.exe -noprofile -Command "&{''' + cmd_str + '''}"''', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return_str = proc.stdout.read().decode()

        self.ui.te_exe_info.append("{}-[cmd] 执行命令: {}\n".format(time_str, cmd_str))
        if len(str(return_str).strip()) != 0:
            self.ui.te_exe_info.append("{}-[info] 执行返回结果: {}".format(time_str, "-" * 30))
            self.ui.te_exe_info.append(return_str)
            self.ui.te_exe_info.append("{}\n".format("-" * 30))
        return return_str


def main():
    global path_flag
    if platform.system() == "Windows":
        path_flag = 1
    else:
        path_flag = 2
    myapp = QApplication(sys.argv)
    myWin = hexo_tool_main_win()
    myWin.show()
    sys.exit(myapp.exec_())


if __name__ == '__main__':
    main()