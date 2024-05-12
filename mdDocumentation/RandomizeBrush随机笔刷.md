# RandomizeBrush插件说明文档
*本文档最后一次修改时间：2024.05.12*

### 插件描述
Randomize Brush 是 Aseprite 的扩展插件，它为Aseprite添加了更多功能

### 插件安装及使用
安装：编辑-首选项-扩展-添加扩展-打开扩展所在文件夹-点击扩展本体\
使用：到“编辑”菜单并单击“BrushProperties”选项，从对话框窗口中选择一种效果并使用

### 插件选项
- **尺寸(Mode)**
  - **静止**：无效果。
  - **生长(Grow)**：每次点击笔刷都会以“value”为单位递增
    - 数值(Value)：每次增加的笔刷大小数值
  - **衰减(Shrink)**：每次点击笔刷都会以“value”为单位递减
    - 数值(Value)：每次减少的笔刷大小数值
  - **随机范围(Random [Range])**：根据最小值与最大值进行随机
    - 最小值/最大值(Min/Max)：最小值与最大值
  - **随机自定义范围(Random [Set])**：根据自定义的数值进行随机
    - 数值(Value)：格式(1,2,3)，可以无限添加
- **角度(Angle)**
  - **静止**：无效果。
  - **旋转(Rotate)**：必须用“线笔刷”，每次点击旋转角度
    - 数值(Value)：每次旋转的角度数值
  - **随机范围(Random [Range])**：根据最小值与最大值进行随机
    - 最小值/最大值(Min/Max)：最小值与最大值
  - **随机自定义范围(Random [Set])**：根据自定义的数值进行随机
    - 数值(Value)：格式(1,2,3)，可以无限添加
- **颜色(Color)**
  - **静止**：无效果。
  - **顺序(Next)**：按照选定的颜色顺序往下变换【每次刷一次颜色都会顺序变一次】
  - **倒序(Previous)**：按照选定的颜色顺序往上变换【每次刷一次颜色都会倒序变一次】
  - **随机自定义范围(Random [Set])**：根据选定的颜色随机变换

### 已知问题
>- **暂无**

### 插件预览
*↓尺寸演示↓*\
![轮廓生成-跟随笔刷演示](https://img.itch.zone/aW1hZ2UvMjEzNTg5MS8xMjYzMzMzOC5naWY=/original/ZyxzQF.gif)  
*↓角度演示↓*\
![混合方式-唯一混合演示](https://img.itch.zone/aW1hZ2UvMjEzNTg5MS8xMjYzMzM3Mi5naWY=/original/5DlFqg.gif)  
*↓颜色演示↓*\
![混合方式-唯一混合演示](https://img.itch.zone/aW1hZ2UvMjEzNTg5MS8xMjYzMzM5NC5naWY=/original/SBiJpl.gif)  

### 插件作者
>**作者**：[Kacper Woźniak](https://thkaspar.itch.io/)\
>**最新版本**：[1.0.0](https://thkaspar.itch.io/randomize-brush/download/eyJleHBpcmVzIjoxNzE1NTAyMjI2LCJpZCI6MjEzNTg5MX0%3d.lp0CGeoG9CwUfmYjpssQ1CBIGjg%3d)\
>**版本发布时间**：2023.07.30

### 说明文档撰写人
>[YueHaxgu月](https://github.com/YueHaxgu)
