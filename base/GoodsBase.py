# @PURPOSE:
# @AUTHOR: Aoxiang Zhang
# @TIME: 22:19 2024/5/9 UTC+8


class GoodsBase:
    def goods_title_xpath(self):
        """
        Xpath for goods title
        """
        return "//textarea[@placeholder='请输入商品标题']"

    def goods_detail_xpath(self):
        """
        Xpath for goods detail
        """
        return "//textarea[@placeholder='请输入商品详情']"

    def goods_num_input_xpath(self):
        """
        Xpath for the goods number input box
        """
        return "//input[@placeholder='商品数量']"

    def goods_img_xpath(self):
        """
        Xpath for goods image input box
        """
        return "//input[@type='file']"

    def goods_price_xpath(self):
        """
        Xpath fot goods price input box
        """
        return "//input[@placeholder='请输入商品单价']"

    def goods_status_xpath(self):
        """
        Xpath for goods status selection box
        """
        return "//input[@placeholder='请选择商品状态']"

    def select_goods_status_xpath(self, select_status: str):
        """
        Xpath for selecting goods status
        :param select_status: "上架", "下架"
        :return
        """
        return "//span[text()='" + select_status + "']/parent::li"

    def button_goods_page_bottom_xpath(self, button_name: str):
        """
        Xapth for the button at goods page bottom
        :param button_name: "提交", "重置"
        :return
        """

        return "//span[text()='" + button_name + "']/parent::button"
