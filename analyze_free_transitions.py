#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
分析剪映转场效果中哪些是免费的
"""

import pyJianYingDraft as draft
from pyJianYingDraft.metadata.transition_meta import TransitionType
from pyJianYingDraft.metadata.effect_meta import TransitionMeta

def analyze_free_transitions():
    """分析所有转场效果，区分免费和付费"""
    
    free_transitions = []
    vip_transitions = []
    
    # 遍历所有转场类型
    for transition_name in dir(TransitionType):
        if transition_name.startswith('_'):
            continue
            
        transition_enum = getattr(TransitionType, transition_name)
        if isinstance(transition_enum.value, TransitionMeta):
            transition_meta = transition_enum.value
            
            if transition_meta.is_vip:
                vip_transitions.append({
                    'name': transition_meta.name,
                    'duration': transition_meta.default_duration / 1000000,  # 转换为秒
                    'is_overlap': transition_meta.is_overlap
                })
            else:
                free_transitions.append({
                    'name': transition_meta.name,
                    'duration': transition_meta.default_duration / 1000000,  # 转换为秒
                    'is_overlap': transition_meta.is_overlap
                })
    
    return free_transitions, vip_transitions

def print_analysis_report(free_transitions, vip_transitions):
    """打印分析报告"""
    
    print("=" * 60)
    print("剪映转场效果分析报告")
    print("=" * 60)
    
    print(f"\n📊 统计信息:")
    print(f"免费转场效果: {len(free_transitions)} 个")
    print(f"VIP转场效果: {len(vip_transitions)} 个")
    print(f"总计: {len(free_transitions) + len(vip_transitions)} 个")
    
    print(f"\n🎯 免费转场效果占比: {len(free_transitions) / (len(free_transitions) + len(vip_transitions)) * 100:.1f}%")
    
    print(f"\n✅ 免费转场效果列表 (按名称排序):")
    print("-" * 50)
    
    # 按名称排序
    free_transitions.sort(key=lambda x: x['name'])
    
    for i, transition in enumerate(free_transitions, 1):
        duration_str = f"{transition['duration']:.1f}s"
        overlap_str = "重叠" if transition['is_overlap'] else "不重叠"
        print(f"{i:3d}. {transition['name']:<15} ({duration_str}, {overlap_str})")
    
    print(f"\n💎 VIP转场效果列表 (按名称排序):")
    print("-" * 50)
    
    # 按名称排序
    vip_transitions.sort(key=lambda x: x['name'])
    
    for i, transition in enumerate(vip_transitions, 1):
        duration_str = f"{transition['duration']:.1f}s"
        overlap_str = "重叠" if transition['is_overlap'] else "不重叠"
        print(f"{i:3d}. {transition['name']:<15} ({duration_str}, {overlap_str})")
    
    # 分析免费转场的时长分布
    print(f"\n📈 免费转场效果时长分布:")
    print("-" * 30)
    
    duration_ranges = {
        "0.5秒以下": 0,
        "0.5-1.0秒": 0,
        "1.0-2.0秒": 0,
        "2.0秒以上": 0
    }
    
    for transition in free_transitions:
        duration = transition['duration']
        if duration < 0.5:
            duration_ranges["0.5秒以下"] += 1
        elif duration < 1.0:
            duration_ranges["0.5-1.0秒"] += 1
        elif duration < 2.0:
            duration_ranges["1.0-2.0秒"] += 1
        else:
            duration_ranges["2.0秒以上"] += 1
    
    for range_name, count in duration_ranges.items():
        print(f"{range_name}: {count} 个")
    
    # 推荐一些效果明显的免费转场
    print(f"\n🌟 推荐免费转场效果 (效果明显):")
    print("-" * 40)
    
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
    
    found_recommended = []
    for name in recommended_free:
        for transition in free_transitions:
            if transition['name'] == name:
                found_recommended.append(transition)
                break
    
    for i, transition in enumerate(found_recommended, 1):
        duration_str = f"{transition['duration']:.1f}s"
        overlap_str = "重叠" if transition['is_overlap'] else "不重叠"
        print(f"{i:2d}. {transition['name']:<15} ({duration_str}, {overlap_str})")

def generate_free_transitions_code(free_transitions):
    """生成免费转场效果的代码列表"""
    
    print(f"\n💻 免费转场效果代码列表 (可直接使用):")
    print("-" * 50)
    
    # 按名称排序
    free_transitions.sort(key=lambda x: x['name'])
    
    print("free_transitions = [")
    for i, transition in enumerate(free_transitions):
        comma = "," if i < len(free_transitions) - 1 else ""
        print(f"    draft.TransitionType.{transition['name']}{comma}")
    print("]")

if __name__ == "__main__":
    print("正在分析剪映转场效果...")
    
    free_transitions, vip_transitions = analyze_free_transitions()
    
    print_analysis_report(free_transitions, vip_transitions)
    generate_free_transitions_code(free_transitions)
    
    print(f"\n🎉 分析完成！")
    print(f"💡 提示: 使用免费转场效果可以避免VIP限制，同时保持视频的专业效果。") 