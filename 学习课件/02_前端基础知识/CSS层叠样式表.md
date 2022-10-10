#  CSS层叠样式表

一、css的语法
-----------------------------

+ 什么是css？

  层叠样式表

+ 命名规则：

  使用字母、数字或下划线和减号构成，不要以数字开头

+ 格式： 

  选择器{属性:值;属性:值;属性:值;....}

  其中选择器也叫选择符

+ CSS中注释

  ```css
  /* ... */
  ```

  

## 二、在HTML中如何使用css样式（html中嵌入css的方式）

### 1、内联方式（行内样式）

就是在HTML的标签中使用style属性来设置css样式
 格式： `<html标签 style="属性:值;属性:值;....">被修饰的内容</html标签>`

 `<p style="color:blue;font-family:隶书">在HTML中如何使用css样式</p>`
 特点：仅作用于本标签

### 2、内部方式（内嵌样式）

就是在head标签中使用`<style type="text/css">....</style>`标签来设置css样式
 格式：

```python
 <style type="text/css">
 	....css样式代码
 </style>
```

 **特点：**作用于当前整个页面

### 3、外部导入方式（外部链入）

+ （推荐）就是在head标签中使用`<link/>`标签导入一个css文件，在作用于本页面，实现css样式设置

   格式：

  ```Css
  <link href="文件名.css" type="text/css" rel="stylesheet"/>
  ```

  + 还可以使用import在style标签中导入css文件。

   特点：作用于整个网站





三、**css2的选择符：
---------------------------------------------------------------
### 1、html选择符（标签选择器）

 就是把html标签作为选择符使用
 如 p{....}  网页中所有p标签采用此样式
```css
h2{....}  网页中所有h2标签采用此样式
```
### 2、class类选择符 (使用点.将自定义名（类名）来定义的选择符)（类选择器P）

定义： 		  .类名{样式....}    匿名类

   其他选择符名.类名{样式....}
 使用：`<html标签 class="类名">...</html标签>`

 .mc{color:blue;} /* 凡是class属性值为mc的都采用此样式 */

 p .ps{color:green;}  /*只有p标签中class属性值为ps的才采用此样式*/

 注意：类选择符可以在网页中重复使用

### 3、Id选择符(ID选择器)

 定义： #id名{样式.....}
 使用：`<html标签 id="id名">...</html标签>`

 注意：id选择符只在网页中使用一次

选择符的优先级：从大到小 [ID选择符]->[class选择符]->[html选择符]->[html属性]

### 4、关联选择符（包含选择符）

 格式： 选择符1 选择符2 选择符3 ...{样式....}
 例如： table a{....} /\*table标签里的a标签才采用此样式*/

 	h1 p{color:red} /*只有h1标签中的p标签才采用此样式*/

### 5、组合选择符（选择符组）

 格式： 选择符1,选择符2,选择符3 ...{样式....}

 	h3,h4,h5{color:green;} /*h3、h4和h5都采用此样式*/

### 6、*通配符（全局选择器）

 说明：

 通配符的写法是“*”，其含义就是所有元素。

 用法：

 常用来重置样式   

 	*{padding:0; margin:0;}

### 7、伪类选(伪元素)择符：

格式： 标签名:伪类名{样式....}

```css
 a:link {color: #FF0000; text-decoration: none} 	    /* 未访问的链接 */

 a:visited {color: #00FF00; text-decoration: none} 	    /* 已访问的链接 */

 a:hover {color: #FF00FF; text-decoration: underline} /* 鼠标在链接上 */

 a:active {color: #0000FF; text-decoration: underline} /* 激活链接 */
```

 为了简化代码，可以把伪类选择符中相同的声明提出来放在a选择符中；

#####  例如：

 a{color:red;}     a:hover{color:green;} 表示超链接的三种状态都相同，只有鼠标划过变颜色。

伪类（Pseudo classes）是选择符的螺栓，用来指定一个或者与其相关的选择符的状态

##### 优先级:行内->css3选择器->id->class->html->html属性

## 四、  CSS3中的选择器

1. ##### 关系选择器：

 div>p 选择所有作为div元素的子元素p
 div+p 选择紧贴在div元素之后p元素
 div~p 选择div元素后面的所有兄弟元素p

2. ##### 属性选择器：

 [attribute]选择具有attribute属性的元素。
 [attribute=value]选择具有attribute属性且属性值等于value的元素。

3. ##### 结构性伪类选择器：

伪类选择器（简称：伪类）通过冒号来定义，它定义了元素的状态，如点击按下，点击完成等，通过伪类可以为元素的状态修改样式。
 :before设置在对象前（依据对象树的逻辑结构）发生的内容。
 :after设置在对象后（依据对象树的逻辑结构）发生的内容。

```css
span:before{
    content: '必须存在的属性';
    display: block;
    border:1px solid red;
}
span:after{
    content: '必须存在的属性';
    display: block;
    border:1px solid red;
}
```



五、CSS中常用的属性：
---------------------------------------------------------------------------------------
### 1、color颜色属性：

color 英文单词

```css
{color:red;}
```

### 2、字体属性： font

font
 *font-size: 		字体大小：20px，60%基于父对象的百分比取值
 *font-family：	字体：宋体，Arial
 *font-weight：	字体加粗 ：bold

### 3、文本属性：

*text-align: 	文本的位置：left center right
*text-decoration: 字体画线：none无、underline下画线，line-through贯穿线
*line-height：行高
*color： 字体颜色

### 5、背景属性：background

+ *background-color: 背景颜色
+ \*background-image: 背景图片

  







