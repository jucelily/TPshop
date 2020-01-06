from selenium import webdriver


def get_tip_message():
    """获取弹窗信息方法"""
    # msg = self.driver.find_element_by_class_name('layui-layer-content').text
    msg = DriverUtil.get_driver().find_element_by_class_name('layui-layer-content').text
    print('msg:', msg)
    return msg


class DriverUtil(object):
    """浏览器驱动对象工具类"""

    driver = None  # 驱动对象初始化状态

    @classmethod
    def get_driver(cls):
        """获取驱动对象方法"""
        # 判断浏览器对象不存在时再进行创建操作
        if cls.driver is None:
            cls.driver = webdriver.Chrome()
            # 由于判断条件下的代码只会执行一次, 因此将打开和最大化和隐式等待的设置暂时放置到这里
            cls.driver.get('http:127.0.0.1')
            cls.driver.maximize_window()
            cls.driver.implicitly_wait(10)
        return cls.driver

    @classmethod
    def quit_driver(cls):
        """退出驱动对象方法"""
        # 判断驱动对象存在时再执行退出操作
        if cls.driver:
            cls.driver.quit()
            cls.driver = None


if __name__ == '__main__':
    DriverUtil.get_driver()
    DriverUtil.quit_driver()
