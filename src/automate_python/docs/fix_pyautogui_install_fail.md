## Mac下安装 **pyautogui** 错误解决方案

在第18章-**用GUI自动化控制键盘和鼠标**中需要用到 **pyautogui**, 直接通过 
`pip install pyautogui` 安装报如下错误:

```bash
Downloading http://mirrors.aliyun.com/pypi/packages/ff
91654a05ac665b49ae939a0/PyAutoGUI-0.9.33.zip (55kB)
    100% |████████████████████████████████| 61kB 780kB/s
    Complete output from command python setup.py egg_inf
    Traceback (most recent call last):
      File "<string>", line 1, in <module>
      File "/private/var/folders/45/gs7p38ps78d775hycdds
/setup.py", line 6, in <module>
        version=__import__('pyautogui').__version__,
      File "/private/var/folders/45/gs7p38ps78d775hycdds
/pyautogui/__init__.py", line 110, in <module>
        from . import _pyautogui_osx as platformModule
      File "/private/var/folders/45/gs7p38ps78d775hycdds
/pyautogui/_pyautogui_osx.py", line 4, in <module>
        import Quartz
    ModuleNotFoundError: No module named 'Quartz'
   ----------------------------------------
Command "python setup.py egg_info" failed with error cod
d775hycddsq_640000gn/T/pip-build-g9m_kzii/pyautogui/
```

通过 [google-No module named 'Quartz'](https://www.google.com.hk/?gws_rd=ssl#safe=strict&q=No+module+named+%27Quartz%27&*),
找到解决方案: [PyAutoGui: Installing on Mac OS X – Medium](https://medium.com/@tracy_blog/pyautogui-installing-on-mac-os-x-86e397428b3#.myy0aj1xl),
按步骤执行后，问题解决。




