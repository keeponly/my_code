# _*_coding: utf-8 _*_
# @Time     :2020/1/16  15:19
# @Author   :wang-kai
# @tel      :15313929271
# @ File    :project_data.py
# 登录
user_info_success = [
    {"username": "18611815532", "password": "222222", "code": "1111", "expect": "张倩倩"}, ]

user_info_error = [
    {"username": "18611815532", "password": "", "code": "1111", "expect": "请输入密码"},
    {"username": "18611815532", "password": "222222", "code": "", "expect": "请输入验证码"}]

# 创建项目
creat_project = [
    {"project_name": "auto14", "project_type": "//span[text()='评估报告']"},
    {"project_name": "auto15", "project_type": "//span[text()='估值报告']"},
    {"project_name": "auto16", "project_type": "//span[text()='咨询报告']"},
    {"project_name": "auto17", "project_type": "//span[text()='土地估价报告']"},
    {"project_name": "auto18", "project_type": "//span[text()='矿权评估报告']"},
    {"project_name": "auto19", "project_type": "//span[text()='矿权咨询报告']"},
    {"project_name": "auto20", "project_type": "//span[text()='房地产估价报告']"}]
# 共享作价
test_data = [
    {"username": "18611815532", "password": "222222", "code": "1111", "project_name": "测试共享中心送审"}
]


# 编辑项目
edit_project = [
    {"project_name": "auto14", "project_type": "//span[text()='通用项目']", "level": '//span[text()="A"]',
     "object type": '//span[text()="企业价值"]', "object type_01": '//span[text()="股东全部权益价值"]'},
    {"project_name": "auto15", "project_type": "//span[text()='涉军项目']", "level": '//span[text()="B"]',
     "object type": '//span[text()="单项资产"]', "object type_01": '//span[text()="房建类"]'},
    {"project_name": "auto16", "project_type": "//span[text()='房地产项目 ']", "level": '//span[text()="C"]',
     "object type": '//span[text()="资产组合"]', "object type_01": '//span[text()="实物资产组合"]'},
    {"project_name": "auto17", "project_type": "//span[text()='矿权项目']", "level": '//span[text()="C"]',
     "object type": '//span[text()="企业价值"]', "object type_01": '//span[text()="股东全部权益价值"]'},
    {"project_name": "auto18", "project_type": "//span[text()='土地项目']", "level": '//span[text()="B"]',
     "object type": '//span[text()="企业价值"]', "object type_01": '//span[text()="股东全部权益价值"]'},
    {"project_name": "auto19", "project_type": "//span[text()='研究课题项目']", "level": '//span[text()="A"]',
     "object type": '//span[text()="企业价值"]', "object type_01": '//span[text()="股东全部权益价值"]'},
    {"project_name": "auto20", "project_type": "//span[text()='通用项目']", "level": '//span[text()="A"]',
     "object type": '//span[text()="企业价值"]', "object type_01": '//span[text()="股东全部权益价值"]'}]

push_project = [
    "评估说明封面至第二部分有关事项说明",
    "第三部分资产清查核实情况说明",
    "宏观经济形势分析",
    "行业分析",
    "企业分析",
    "资产基础法评估说明",
    "流动资产标题",
    "货币资金",
    "现金",
    "银行存款",
    "其他货币资金",
    "货币资金结论",
    "交易性金融资产标题",
    "交易性金融资产股票",
    "交易性金融资产债券",
    "交易性金融资产基金",
    "交易性金融资产结论",
    "应收票据",
    "应收账款",
    "预付账款",
    "应收利息",
    "应收股利",
    "其他应收款",
    "一年到期非流动资产",
    "其他流动资产",
    "存货总述",
    "材料采购",
    "原材料",
    "在库周转材料",
    "委托加工物资",
    "产成品",
    "在产品",
    "发出商品",
    "在用周转材料",
    "工程施工",
    "可供出售金融资产标题",
    "可供出售金融资产股票",
    "可供出售金融资产债券",
    "可供出售金融资产其他投资",
    "可供出售金融资产结论",
    "持有至到期投资",
    "长期应收款",
    "长期股权投资",
    "投资性房地产（一项）",
    "投资性房地产（多项）",
    "固定资产",
    "房屋建筑物（一项）",
    "房屋建筑物（多项）",
    "设备类资产评估技术说明",
    "在建工程",
    "在建工程土建",
    "在建工程设备",
    "工程物资",
    "固定资产清理",
    "生产性生物资产",
    "油气资产",
    "无形资产",
    "无形资产-土地使用权（一宗）",
    "无形资产-土地使用权（多宗）",
    "无形资产矿业权",
    "无形资产其他",
    "开发支出",
    "商誉",
    "长期待摊费用",
    "递延所得税资产",
    "其他非流动资产",
    "负债",
    "流动负债",
    "短期借款",
    "应付票据",
    "应付账款",
    "预收账款",
    "职工薪酬",
    "应交税费",
    "应付利息",
    "应付股利",
    "其他应付款",
    "一年内到期非流动负债",
    "其他流动负债",
    "非流动负债",
    "长期借款",
    "应付债券",
    "长期应付款",
    "专项应付款",
    "预计负债",
    "递延所得税负债",
    "其他非流动负债",
    "收益法评估说明",
    "市场法评估说明",
    "评估结论总述",
    "资产基础法评估结论",
    "收益法评估结论",
    "市场法评估结论",
    "成本法和收益法评估结果差异",
    "成本法和市场法评估结果差异",
    "收益法和市场法评估结果差异",
    "评估结果选取",
    "企业关于进行资产评估有关事项的说明"]
