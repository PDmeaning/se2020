# 欢迎来到SE2020!

该项目为重庆大学软件工程课程2020年课程设计。课程设计目标为让学生们使用多种语言来实现三角函数的4种函数并以此学习Github的使用。


## 文件目录

该项目的文件目录如下：
    
    └─ se2020-master    //主目录
       │  README.md     //说明文件
       ├─Python1.0      //Python三角函数源码目录
       │  │  test_1.0.py     //测试文件
       │  │  trigon_1.0.py     //三角函数1.0版源码
       │  │  trigon_1.1.py     //三角函数1.1版源码
       │  │  trigon_1.2.py     //三角函数1.2版源码
       │  │
       │  └─.idea     //intellij idea工程配置目录
       │          misc.xml
       │          modules.xml
       │          se2020.iml     
       │          vcs.xml
       │          workspace.xml
       │
       └─sanjiaoF_c      //C语言三角函数源码目录
          │  C_sanjiaofunction.c      //C语言三角函数源码
          │  C_sanjiaofunction.ncb
          │  C_sanjiaofunction.opt
          │  C_sanjiaofunction.plg
          │
          └─Debug        //C语言三角函数Debug目录
                C_sanjiaofunction.exe      //最终生成的可执行程序
                C_sanjiaofunction.ilk
                C_sanjiaofunction.obj
                C_sanjiaofunction.pch
                C_sanjiaofunction.pdb
                vc60.idb
                vc60.pdb

## 如何使用
以下是两种不同语言代码的使用方法。
- **Python**
> 1.[安装Python（点击可以看到教程）](https://www.cnblogs.com/lvtaohome/p/11121377.html)

> 2.直接运行目录中的trigon_1.2.py

> 3.输入角度值

> 4.得到运行结果

- **C语言**
> 1.直接运行Debug目录下的C_sanjiaofunction.exe

> 2.输入弧度值（1°=π/180°，1rad=180°/π依据此进行弧度换算）

> 3.得到运行结果。

> **注:** 如果出现使用问题建议搭建好全套开发环境（见后）。
## 修改文件（开发环境搭建）
如果需要修改源码文件，则需要搭建开发环境。以下给出两个安装开发环境的教程，可以据此进行搭建。

[C语言（VC++6.0）](http://c.biancheng.net/view/463.html)

[Python（Pycharm）](https://www.cnblogs.com/du-hong/p/10244304.html)

## 运行结果

- **Python**
![效果图](https://github.com/PDmeaning/se2020/blob/master/Py.png)



 - **C语言**
![效果图](https://github.com/PDmeaning/se2020/blob/master/C.png)



# ChangeLog
  **2020年4月9日**
-    修复C和Python运行一闪而过的问题
-    README说明文件第三版

  **2020年3月27日**
  -    修复Python第二版BUG
  -    README说明文件第一版
  
 **2020年3月21日**
 -    上传C语言第一版代码
 -    README说明文件第一版
 -    Python第二版加入函数
 
 **2020年3月15日**
 -    上传Python第一版代码
 

 **2020年3月6日**
 -    项目建立



