![插件头图](https://img.itch.zone/aW1nLzkwODY4NTQucG5n/original/ssth9P.png)
# MagicPencil插件说明文档
*本文档最后一次修改时间：2024.05.12*

### 插件描述
Magic Pencil 是 Aseprite 的扩展插件，它为Aseprite添加了更多功能

### 插件安装及使用
安装：编辑-首选项-扩展-添加扩展-打开扩展所在文件夹-点击扩展本体\
使用：到“编辑”菜单并单击“魔术铅笔”选项，从对话框窗口中选择一种效果并使用铅笔工具\
注意：大多数选项使用魔术颜色，关闭魔术铅笔对话框窗口或选择常规选项后将恢复所选颜色

### 插件选项
- **模式(Mode)**
  - **常规模式(Regular)**：默认绘画模式
  - **涂鸦模式(Graffiti)**：选中此选项后，笔刷刷出内容会有滴蜡的效果[(✿◡‿◡)]
- **轮廓生成(Outline)**
  - **封闭图形(Tool)**：当你选了这个选项之后，画笔触及区域的闭合路径会自动生成一圈描边。【比如你画了一个icon，你在这个icon上点了一笔就会自动把这个icon描个边，描边颜色是你当前的选中颜色】
  - **跟随笔刷(Brush)**：当你选择这个选项之后，你的笔刷会自动添加一层描边，且重叠部分会自动修改，描边颜色在下方更改
- **变换**
  - **选择区(Selection)**：选中后出现紫色笔刷，左键笔刷刷到的区域即可添加选区，右键笔刷刷到的区域即可删除选区
  - **上移(Lift)**：选中后出现紫色笔刷，用紫色笔刷左键覆盖当前画布的内容即可自动复制覆盖内容到上一个新图层，右键则向下生成
- **混合方式(Mix)**
  - **唯一混合(Unique)**：混合颜色，左键单击使用 RGB 颜色模型混合颜色，而右键单击使用 HSV
  - **成比混合(Proportional)**：混合颜色考虑到每种颜色的像素数，左键单击使用 RGB 颜色模型混合颜色，而右键单击使用 HSV
- **鲜艳化(Colorize)** ：更改颜色（色调），适用于前景（左键单击）和背景（右键单击）颜色
- **去饱和(Desaturate)**：遗像，完全去除颜色（色调）
- **转变(Shift)**： 根据所选属性（RGB、HSL、HSV）更改颜色，左键单击添加，右键单击减去。可以通过更改这些选项下的百分比滑块来更改将应用​​多少次
  - **RGB**：R红、G绿、B蓝
  - **HSL**：H色相、S饱和度、L亮度
  - **HSV**：H色相、S饱和度、明度
- **索引模式(Indexed Mode)**：启用后，防止引入新颜色，并且任何修改颜色的选项都将使用调色板中的颜色

### 已知问题
>- **在完全空的单元格上使用 Magic Pencil 中的任何选项将导致第一个笔划被视为普通铅笔；**
>- **当使用除 轮廓生成(Outline) 或 鲜艳化(Colorize) 之外的 Magic Pencil 中的任何选项（实际上使用所选颜色）时，从调色板中选择颜色会干扰其工作并导致奇怪的行为。**

### 插件预览
*↓轮廓生成-跟随笔刷演示↓*\
![轮廓生成-跟随笔刷演示](https://s2.loli.net/2024/05/12/ZoNnxY2FefWMT7D.gif)  
*↓混合方式-唯一混合演示↓*\
![混合方式-唯一混合演示](https://s2.loli.net/2024/05/12/5nsDEtMNPa2f4Lo.gif)  
*↓混合方式-唯一混合演示↓*\
![混合方式-唯一混合演示](https://s2.loli.net/2024/05/12/Zvol8UfA29h3wBr.gif)  
*↓变换-选择区演示↓*\
![变换-选择区演示](https://s2.loli.net/2024/05/12/PdDSFyGYrmResLQ.gif)  
*↓改变-鲜艳化颜色↓*\
![改变-鲜艳化颜色](https://s2.loli.net/2024/05/12/gI9sHhaqiCzAYZU.gif)

### 插件作者
>**作者**：[Kacper Woźniak](https://thkaspar.itch.io/)\
>**最新版本**：[v1.0.5](https://thkaspar.itch.io/magic-pencil/download/eyJpZCI6MTU1NzE3MiwiZXhwaXJlcyI6MTcxNTUwMjEyMX0%3d.3zyiNefyKmU6H4pxc2gegd8jjkM%3d)\
>**版本发布时间**：2022.06.02

### 说明文档撰写人
>[YueHaxgu月](https://github.com/YueHaxgu)
>
>[66six11](https://github.com/66six11)