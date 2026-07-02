import os
import requests

# 从github密钥读取账号信息
account_info = os.getenv("WDT_ACCOUNTS")

def main():
    print("===== 开始执行WDT自动退货审批任务 =====")
    print("读取到账号配置：", account_info)

    # ==========这里改成你自己的业务逻辑==========
    # 1. 请求接口获取待审批退货单列表
    # url = "你的退货单查询接口地址"
    # resp = requests.get(url)
    # order_list = resp.json()

    # 2. 循环逐个审批通过
    # for order in order_list:
    #     approve_url = "审批接口地址"
    #     requests.post(approve_url, data={"order_id": order["id"]})
    # =========================================

    print("===== 自动审批任务执行完成 =====")

if __name__ == "__main__":
    main()

