# RhinoProject

记录一些rhinoPython和ghPython的学习文件


## 关于rhinoPython和ghPython结合vsc的使用

### 参考网站
https://www.food4rhino.com/en/app/code-listener
https://marketplace.visualstudio.com/items?itemName=designtoproduction.rhinopython
https://zhuanlan.zhihu.com/p/259589783


需要插件：
Rhino、grasshopper
gh：GH_Cpython 也可以不用
rhino：Code-listener
vsc：Rhinopython（Visual Studio Code插件，在插件商店找）

### 思路：
简单来讲： 
1. 将editPython的module路径导入vsc中（有三个） 以及一切所需要的配置库环境
2. 将codeListener中的autoComplete folder 路径导入vsc中 导入代码如下
into the user settings
3. rhino中启动codeListener

## code:listener 设置：


Install VS code.

Install python for VS code. It's recommended to familarize yourself with python for VS code at this post first.

Install RhinoPython for VS code.

Download CodeListener file in food4rhino, and install it.

Start Rhino, click tools -> pythonscript -> edit, in the python editor, click tools -> options, copy those module paths. You might have additional libraries and you have to copy them as well.

In Rhino, click tools -> options -> Plug-ins -> CodeListener -> Proterties, copy the file containing folder path and open it in the explorer. Copy the AutoComplete folder path.


Start VS Code, open user settings by keyboard shortcut Ctrl+, paste the libraries paths and autocomplete path into the user settings with key "python.autoComplete.extraPaths", below is an example setting.


{
    // disable certain pylint messages
    "python.linting.pylintArgs": [
        "--errors-only",
        "--disable=E0001",
        "--disable=E0401"
    ],
    // python autocomplete extra path
    "python.autoComplete.extraPaths": [
        "C:\\Users\\jingcheng\\AppData\\Roaming\\McNeel\\Rhinoceros\\5.0\\Plug-ins\\CodeListener (8c4235b6-64bc-4508-9166-bef8aa151085)\\1.0.0.0\\AutoComplete",
        "C:\\Users\\jingcheng\\AppData\\Roaming\\McNeel\\Rhinoceros\\5.0\\Plug-ins\\IronPython (814d908a-e25c-493d-97e9-ee3861957f49)\\settings\\lib",
        "C:\\Program Files\\Rhinoceros 5 (64-bit)\\Plug-ins\\IronPython\\Lib",
        "C:\\Users\\jingcheng\\AppData\\Roaming\\McNeel\\Rhinoceros\\5.0\\scripts"
    ],

    // enable new language server. THIS IS EXTREMELY IMPORTANT TO HAVE FAST AUTOCOMPLETE!!
    "python.jediEnabled": false,

    // Enable/Disable rhinopython
    "RhinoPython.Enabled": true,
    // True if you want to reset script engine every time you send code, otherwise False
    "RhinoPython.ResetAndRun": true
}

### usage
Start Rhino, type command CodeListener. You should see VS Code Listener Started....
You can add CodeListener into Rhino Command Lists every time Rhino starts. There are other commands in Rhino: StopCodeListener, CodeListenerVersion

Start VS Code, create a new file (To have python autocomplete and lint working you have to specify it's python file) or open an existing python file or folder or workspace.
Send the your code by simply press F2 or by typing command CodeSender in Command Palette(F1 or Ctrl+Shift+P) You should then see returned printed message or errors in Debug Console. Depending on your RhinoPython.ResetAndRun settings, you might reset script engine every time before you send.
If you want to reset Rhino Python Script Engine, simply press Ctrl + R.


### ghPython使用vsc进行

使用 panel + path + readFile + ghPython 电池组