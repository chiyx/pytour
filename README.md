# 我的 python3 学习之路
------------

## 环境准备

### 基础环境 - python3

- 安装

    ```bash
    brew install python3
    ```

- pypi镜像设置
    > 加速pip安装第三方库

    ```bash
    mkdir -p ~/.pip
    touch ~/.pip/pip.conf
    cat > ~/.pip/pip.conf <<EOF
    [global]
    trusted-host = mirrors.aliyun.com
    index-url = https://mirrors.aliyun.com/pypi/simple/
    EOF
    ```

### 编辑器 - vscode

- 安装
    - 从官方网站下载[vscode](https://code.visualstudio.com/)最新版
    - vscode相关插件安装
        - Python: 智能提示，格式化，lint等
        - MagicPython: 语法高亮
        - CodeRunner: 代码运行
        - vim: Vim编辑模式, 个人习惯，可选
        - Sublime Material Theme: 主题, 个人习惯, 个人习惯, 可选
        - VSCode Great Icons: 文件图标, 个人习惯, 可选
- 用户级别配置

    ```json
    {
        // vscode 终端配置
        "terminal.integrated.shell.osx": "/bin/zsh",
        "terminal.integrated.fontSize": 16,
        // 编辑器字体配置
        "editor.fontFamily": "'Source Code Pro for Powerline', Menlo, Monaco, 'Courier New', monospace",
        "editor.fontSize": 16,
        "editor.renderWhitespace": "boundary",
        // python配置-采用pyyhon3同时编码风格采用pep8
        "python.pythonPath": "/usr/local/bin/python3",
        "python.linting.pep8Enabled": true,
        "python.linting.pylintEnabled": false,
        // code-runner 配置python的执行器
        "code-runner.executorMap": {
            "python": "/usr/local/bin/python3",
        }
    }
    ```
### 工作空间

- 创建目录

    ```bash
    mkdir pytour
    cd pyour
    git init
    ```

- 创建虚拟环境
    > 何为虚拟环境: http://docs.pythontab.com/python/python3.4/venv.html

    ```bash
    pyvenv pytour-venv
    source pytour-venv/bin/activate
    ```

- vscode工作空间配置
    > 主要是将工作空间的相关python配置，指向当前的虚拟环境

    ```json
    {
        "python.pythonPath": "./pytour-venv/bin/python",
        "code-runner.executorMap": {
            "python": "./pytour-venv/bin/python"
        }
    }
    ```

## 进阶之路

1. 书籍: [Python语言及其应用](https://book.douban.com/subject/26675127/)
    - [相关练习Code](./src/introducing_python)
1. 书籍: [Python编程快速上手 让繁琐的工作自动化](https://book.douban.com/subject/26836700/)
    - [相关练习Code](./src/automate_python)
    - 学习记录
        - [Mac下安装pyautogui错误解决方案](./src/automate_python/docs/fix_pyautogui_install_fail.md)
1. 书籍: [数据结构与算法：Python语言描述](https://book.douban.com/subject/26702568/)
    - [相关练习](./src/algo_in_python)
1. [leetCode](https://leetcode.com/problemset/algorithms/)解题
    - [相关练习](./src/leetcode)
1. 书籍: [Python网络编程(第三版)](https://book.douban.com/subject/26869212/)
    - [相关练习](./src/network_python)
1. 书籍: [机器学习实战](https://book.douban.com/subject/24703171/)
    - [相关练习](./src/machine_learn_action)