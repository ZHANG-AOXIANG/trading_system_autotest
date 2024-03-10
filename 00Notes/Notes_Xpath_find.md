# Xpath查找

### 两种查找模式

1. 从根节点开始查找 /
2. 模糊查找 //

### 示例

1. . 选取当前节点
   ![](./NotesImage/xpath_find_this_node.png)
2. .. 选取当前节点的父节点
   ![](./NotesImage/xpath_find_this_node_father.png)

3. //div[@class='logo'] 选取标签名为div，属性class值为logo元素
   ![](./NotesImage/xpath_find_class_include_logo.png)

4. //span[text=('我的钱包')] 选取所有标签为span，span标签的文字内容为‘我的钱包的元素’
   ![](./NotesImage/xpath_find_span_text_include.png)

5. //div[@class='el-descriptions']//tbody/tr[1] 选取tbody下的第一个tr
   ![](./NotesImage/xpath_find_dic_class_el_description_tbody_tr.png)

6. //div[@class='el-descriptions']//tbody/tr[last()] 选取tbody的最后一个tr
   ![](./NotesImage/xpath_find_last_one.png)

7. //div[@class='el-descriptions']//tbody/tr[last()-1]选取tdoby的倒数第二个tr
   ![](./NotesImage/xpath_find_class_el_description_tbody_tr_last_second.png)
















