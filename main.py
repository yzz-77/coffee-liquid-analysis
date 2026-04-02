# 咖啡液品类自动分析脚本 + 阿里云通义千问AI分析
import requests
import json
from litellm import completion
import os

# 1. 配置阿里云通义千问模型
os.environ["DASHSCOPE_API_KEY"] = os.getenv("DASHSCOPE_API_KEY")
model = "qwen-turbo"

# 2. 自动抓取电商咖啡液公开数据（淘宝/天猫）
def get_coffee_data():
    print="正在自动抓取咖啡液品类数据..."
    # 模拟公开数据（真实场景可替换为电商API，小白用这个直接跑）
    data = {
        "top_brands": ["瑞幸", "永璞", "隅田川", "三顿半", "星巴克"],
        "price_range": "3.5元~12元/杯",
        "hot_flavors": ["生椰", "无糖冷萃", "燕麦拿铁", "原味浓缩"],
        "sales_rank": "瑞幸咖啡液月销第一",
        "user_demand": ["便携", "0糖", "高性价比", "门店同款"]
    }
    return data

# 3. 通义千问AI自动生成品类分析报告
def ai_analysis(data):
    print="AI正在生成咖啡液品类分析报告..."
    prompt = f"""
    你是专业电商品类分析师，基于以下数据生成【线上咖啡液品类分析报告】：
    头部品牌：{data['top_brands']}
    价格区间：{data['price_range']}
    热门口味：{data['hot_flavors']}
    销量排名：{data['sales_rank']}
    用户需求：{data['user_demand']}
    
    报告必须包含4部分：
    1. 市场整体趋势
    2. 竞品格局分析
    3. 价格带与爆款特征
    4. 品类机会点
    
    语言简洁、专业、可直接使用。
    """
    
    # 调用阿里云模型
    response = completion(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# 4. 主程序：自动执行+保存报告
if __name__ == "__main__":
    data = get_coffee_data()
    report = ai_analysis(data)
    
    # 自动生成分析报告文件
    with open("咖啡液品类分析报告.md", "w", encoding="utf-8") as f:
        f.write(report)
    
    print("✅ 自动分析完成！报告已生成")
    print(report)
