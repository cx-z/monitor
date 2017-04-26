# Monitor
## 1. 引言

### 1.1 写作目地

欢迎浏览Monitor说明文档，这是我们进入syslab的第一个程序，奋斗了很久，从中学到很多。

### 1.2意义

我们总是需要展示数据，最方便的方法就是print出来，但是这样展示的数据很不直观，而且如果想看它随时间变化的过程也没办法。然后现有的组态软件大多是闭源的，而且一般很臃肿，而且一般是本地，不能多终端访问，不够灵活。为改变一些现状，写了这个项目。

## 2. 概述

### 2.1 功能介绍

简单地说，程序能够实现对自动化过程和装备的监视和控制。它能从自动化过程和装备中采集各种信息，并将信息以图形化等更易于理解的方式进行显示，将重要的信息以各种手段传送到相关人员，对信息执行必要分析处理和存储，发出控制指令（待完善）等等。

### 2.2实现方式

python flask做后端

- 收集数据（包括视频，数字，字符串，可能还包括一些提示信息），
- 以合适的频率把数据发送给浏览器
- 接受浏览器返回的信息

web的一套东西做前端

- 展示数据
- 提供交互（按钮，文本框）
- 如果可能的话，提供一些改变布局的方法

交互的模型

- 表示更新方式（被动接受，主动获取：每隔一段时间，事件触发）
- 表示展示方式（简单数值，时间折线图，历史，颜色）
- 将浏览器返回的数据加入客户端程序逻辑

## 3.python代码详解

### 3.1 storage.py

这段代码主要建立了一个类VariableTable，共包含四个函数：

1._ _init_ _用于初始化变量

2.add_var 接收name与format

3.update通过时间对比来确定是否更新数据

4.extract整理数据到result中


### 3.2 monitor_server.py

这段程序主要实现两个功能：

1.利用flask中render_template函数渲染index.html

2.将类的实例用json格式返回

### 3.3 test_index.py

这段程序主要实现了多线程：

对于不同的数据类型的信息实现多线程。利用while的无限循环不断更新。

## 4.前端代码详解

### 4.1 index.html

1.javascript部分用jquery库实现了以1Hz的频率访问后台，并将后台的数据包括不断更新的数字和图片展示在网页上

2.图片部分收到的是base64码，所以需要先解析再展示

3.UI中的按钮点击start时开始访问后台，并且按钮的value变为stop；点击stop时停止访问后台，并将按钮的值变为start

4.点击页面顶部的Logout退出数据展示页面，跳转到登录页面

### 4.2 play.html

1.本文件实现的功能和index.html相同，只是没有设计UI

2.因为此份文档的代码量较少，在添加新功能时先在此文档上测试，等功能实现后再编辑index.html

### 4.3 login.html

本文档实现了登录页面，包含用户名框、密码框和一个提交按钮
