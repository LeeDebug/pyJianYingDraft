#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 直接从转场元数据文件中提取免费转场效果
free_transitions = [
    "3D空间", "上移", "下移", "中心旋转", "云朵", "倒影", "冰雪结晶", "冲鸭",
    "分割", "分割_II", "分割_III", "分割_IV", "前后对比_II", "动漫云朵", "动漫漩涡", 
    "动漫火焰", "动漫闪电", "压缩", "叠加", "叠化", "右移", "向上", "向上擦除",
    "向下", "向下擦除", "向下流动", "向右", "向右上", "向右下", "向右拉伸", 
    "向右擦除", "向右流动", "向左", "向左上", "向左下", "向左拉伸", "向左擦除",
    "吸入", "回忆下滑", "圆形分割_II", "圆形扫描", "圆形遮罩", "圆形遮罩_II",
    "复古放映", "岁月的痕迹", "左下角_II", "左移", "开幕", "弹幕转场", "弹跳",
    "打板转场_I", "打板转场_II", "抖动", "抖动_II", "抠像旋转", "拉伸", "拉伸_II",
    "拉远", "拍摄器", "推近", "撕纸拉屏", "放射", "故障", "斜向分割", "星星", 
    "星星_II", "模糊", "横向分割", "横向拉幕", "横线", "气泡转场", "水波卷动",
    "水波向右", "水波向左", "泛光", "泛白", "波点向右", "渐变擦除", "滑动", 
    "漩涡", "爱心", "爱心_II", "爱心上升", "电视故障_I", "电视故障_II", 
    "画笔擦除", "白光快闪", "白色墨花", "白色烟雾", "百叶窗", "眨眼", "矩形分割",
    "窗格", "立方体", "竖向分割", "竖向拉幕", "竖向模糊", "竖向模糊_II", "竖线",
    "箭头向右"
]

print("=" * 60)
print("剪映免费转场效果分析")
print("=" * 60)

print(f"\n📊 统计信息:")
print(f"免费转场效果: {len(free_transitions)} 个")

print(f"\n✅ 免费转场效果列表:")
print("-" * 50)

for i, transition in enumerate(free_transitions, 1):
    print(f"{i:3d}. {transition}")

print(f"\n💻 免费转场效果代码列表 (可直接使用):")
print("-" * 50)

print("free_transitions = [")
for i, transition in enumerate(free_transitions):
    comma = "," if i < len(free_transitions) - 1 else ""
    print(f"    draft.TransitionType.{transition}{comma}")
print("]")

# 推荐一些效果明显的免费转场
recommended_free = [
    "分割", "分割_II", "分割_III", "分割_IV",
    "横向分割", "竖向分割", "斜向分割",
    "圆形分割_II", "矩形分割",
    "模糊", "竖向模糊", "竖向模糊_II",
    "泛光", "渐变擦除",
    "滑动", "横向拉幕", "竖向拉幕",
    "翻页", "翻篇", "开幕",
    "弹跳", "拍摄器",
    "放射", "漩涡",
    "爱心", "爱心_II", "爱心上升",
    "星星", "星星_II",
    "云朵", "倒影",
    "电视故障_I", "电视故障_II",
    "画笔擦除", "白光快闪",
    "百叶窗", "眨眼", "窗格",
    "立方体", "圆形扫描",
    "圆形遮罩", "圆形遮罩_II",
    "复古放映", "岁月的痕迹",
    "抖动", "抖动_II",
    "抠像旋转", "拉伸", "拉伸_II",
    "撕纸拉屏", "吸入",
    "回忆下滑", "左下角_II"
]

print(f"\n🌟 推荐免费转场效果 (效果明显):")
print("-" * 40)

found_recommended = []
for name in recommended_free:
    if name in free_transitions:
        found_recommended.append(name)

for i, transition in enumerate(found_recommended, 1):
    print(f"{i:2d}. {transition}")

print(f"\n🎉 分析完成！")
print(f"💡 提示: 使用免费转场效果可以避免VIP限制，同时保持视频的专业效果。") 