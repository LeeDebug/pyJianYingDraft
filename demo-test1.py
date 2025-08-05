# 导入模块
import os
import random
import pyJianYingDraft as draft
from pyJianYingDraft import IntroType, TransitionType, trange, tim

# 设置草稿文件夹
draft_folder = draft.DraftFolder(r"C:\ProgramData\JianyingPro Drafts")

# 指定视频文件路径
video_path = r"C:\Users\Edan\Videos\红果短剧\测试\第1集.mp4"
assert os.path.exists(video_path), f"未找到视频文件: {video_path}"

# 创建剪映草稿 - 使用手机屏幕尺寸 (9:16比例)
script = draft_folder.create_draft("红果短剧第1集", 1080, 1920)  # 手机屏幕尺寸 1080x1920

# 添加视频和文本轨道
script.add_track(draft.TrackType.video)
script.add_track(draft.TrackType.text, "主标题轨道")
script.add_track(draft.TrackType.text, "侧边文字轨道")

# 创建视频素材
video_material = draft.VideoMaterial(video_path)
video_duration = video_material.duration

# 转场时间配置参数
FIRST_TRANSITION_TIME = 2  # 第一次转场的时间（秒）
TRANSITION_INTERVAL = 10   # 后续转场间隔时间（秒）

# 定义免费转场效果列表（只使用免费素材）
free_transitions = [
    draft.TransitionType._3D空间,
    draft.TransitionType.云朵,
    draft.TransitionType.星星,
    draft.TransitionType.星星_II,
    draft.TransitionType.爱心,
    draft.TransitionType.爱心_II,
    draft.TransitionType.爱心上升,
    draft.TransitionType.分割,
    draft.TransitionType.分割_II,
    draft.TransitionType.分割_III,
    draft.TransitionType.分割_IV,
    draft.TransitionType.横向分割,
    draft.TransitionType.竖向分割,
    draft.TransitionType.斜向分割,
    draft.TransitionType.圆形分割_II,
    draft.TransitionType.矩形分割,
    draft.TransitionType.立方体,
    draft.TransitionType.漩涡,
    draft.TransitionType.放射,
    draft.TransitionType.色彩溶解,
    draft.TransitionType.色彩溶解_II,
    draft.TransitionType.色彩溶解_III,
    draft.TransitionType.向右擦除,
    draft.TransitionType.向左擦除,
    draft.TransitionType.向上擦除,
    draft.TransitionType.向下擦除,
    draft.TransitionType.顺时针旋转,
    draft.TransitionType.逆时针旋转,
    draft.TransitionType.中心旋转,
    draft.TransitionType.向右拉伸,
    draft.TransitionType.向左拉伸,
    draft.TransitionType.压缩,
    draft.TransitionType.拉伸,
    draft.TransitionType.拉伸_II,
    draft.TransitionType.拉远,
    draft.TransitionType.推近,
    draft.TransitionType.模糊,
    draft.TransitionType.竖向模糊,
    draft.TransitionType.竖向模糊_II,
    draft.TransitionType.马赛克,
    draft.TransitionType.故障,
    draft.TransitionType.雪花故障,
    draft.TransitionType.色差故障,
    draft.TransitionType.电视故障_I,
    draft.TransitionType.电视故障_II,
    draft.TransitionType.频闪,
    draft.TransitionType.震动,
    draft.TransitionType.抖动,
    draft.TransitionType.抖动_II,
    draft.TransitionType.泛光,
    draft.TransitionType.泛白,
    draft.TransitionType.渐变擦除,
    draft.TransitionType.滑动,
    draft.TransitionType.横向拉幕,
    draft.TransitionType.竖向拉幕,
    draft.TransitionType.横线,
    draft.TransitionType.竖线,
    draft.TransitionType.百叶窗,
    draft.TransitionType.窗格,
    draft.TransitionType.翻页,
    draft.TransitionType.翻篇,
    draft.TransitionType.开幕,
    draft.TransitionType.弹跳,
    draft.TransitionType.拍摄器,
    draft.TransitionType.撕纸拉屏,
    draft.TransitionType.画笔擦除,
    draft.TransitionType.白光快闪,
    draft.TransitionType.白色墨花,
    draft.TransitionType.白色烟雾,
    draft.TransitionType.眨眼,
    draft.TransitionType.圆形遮罩,
    draft.TransitionType.圆形遮罩_II,
    draft.TransitionType.圆形扫描,
    draft.TransitionType.岁月的痕迹,
    draft.TransitionType.复古放映,
    draft.TransitionType.回忆下滑,
    draft.TransitionType.左下角_II,
    draft.TransitionType.左移,
    draft.TransitionType.右移,
    draft.TransitionType.上移,
    draft.TransitionType.下移,
    draft.TransitionType.弹幕转场,
    draft.TransitionType.打板转场_I,
    draft.TransitionType.打板转场_II,
    draft.TransitionType.抠像旋转,
    draft.TransitionType.水波卷动,
    draft.TransitionType.水波向右,
    draft.TransitionType.水波向左,
    draft.TransitionType.波点向右,
    draft.TransitionType.泛白,
    draft.TransitionType.白色墨花,
    draft.TransitionType.白色烟雾,
    draft.TransitionType.竖线,
    draft.TransitionType.箭头向右,
    draft.TransitionType.冰雪结晶,
    draft.TransitionType.冲鸭,
    draft.TransitionType.前后对比_II,
    draft.TransitionType.动漫云朵,
    draft.TransitionType.动漫漩涡,
    draft.TransitionType.动漫火焰,
    draft.TransitionType.动漫闪电,
    draft.TransitionType.叠加,
    draft.TransitionType.叠化,
    draft.TransitionType.向上,
    draft.TransitionType.向下,
    draft.TransitionType.向下流动,
    draft.TransitionType.向右,
    draft.TransitionType.向右上,
    draft.TransitionType.向右下,
    draft.TransitionType.向右流动,
    draft.TransitionType.向左,
    draft.TransitionType.向左上,
    draft.TransitionType.向左下,
    draft.TransitionType.吸入,
    draft.TransitionType.气泡转场,
    draft.TransitionType.横线,
    draft.TransitionType.竖线,
]

# 创建视频片段列表
video_segments = []

# 计算分段点：0秒、FIRST_TRANSITION_TIME秒、(FIRST_TRANSITION_TIME+TRANSITION_INTERVAL)秒...直到视频结束
segment_points = [0]  # 从0秒开始
segment_points.append(tim(f"{FIRST_TRANSITION_TIME}s"))  # 第一个转场时间
current_time = tim(f"{FIRST_TRANSITION_TIME + TRANSITION_INTERVAL}s")  # 从第一个转场后开始每TRANSITION_INTERVAL秒一个转场

while current_time < video_duration:
    segment_points.append(current_time)
    current_time += tim(f"{TRANSITION_INTERVAL}s")

# 添加视频结束点
segment_points.append(video_duration)

# 定义特别明显的免费转场效果（用于开场转场）
opening_free_transitions = [
    draft.TransitionType.分割,
    draft.TransitionType.分割_II,
    draft.TransitionType.分割_III,
    draft.TransitionType.分割_IV,
    draft.TransitionType.横向分割,
    draft.TransitionType.竖向分割,
    draft.TransitionType.斜向分割,
    draft.TransitionType.模糊,
    draft.TransitionType.竖向模糊,
    draft.TransitionType.竖向模糊_II,
    draft.TransitionType.泛光,
    draft.TransitionType.渐变擦除,
    draft.TransitionType.滑动,
    draft.TransitionType.横向拉幕,
    draft.TransitionType.竖向拉幕,
    draft.TransitionType.开幕,
    draft.TransitionType.弹跳,
    draft.TransitionType.拍摄器,
    draft.TransitionType.放射,
    draft.TransitionType.漩涡,
    draft.TransitionType.爱心,
    draft.TransitionType.爱心_II,
    draft.TransitionType.爱心上升,
    draft.TransitionType.星星,
    draft.TransitionType.星星_II,
    draft.TransitionType.云朵,
    draft.TransitionType.倒影,
    draft.TransitionType.电视故障_I,
    draft.TransitionType.电视故障_II,
    draft.TransitionType.画笔擦除,
    draft.TransitionType.白光快闪,
    draft.TransitionType.百叶窗,
    draft.TransitionType.眨眼,
    draft.TransitionType.窗格,
    draft.TransitionType.立方体,
    draft.TransitionType.圆形扫描,
    draft.TransitionType.圆形遮罩,
    draft.TransitionType.圆形遮罩_II,
    draft.TransitionType.复古放映,
    draft.TransitionType.岁月的痕迹,
    draft.TransitionType.抖动,
    draft.TransitionType.抖动_II,
    draft.TransitionType.抠像旋转,
    draft.TransitionType.拉伸,
    draft.TransitionType.拉伸_II,
    draft.TransitionType.撕纸拉屏,
    draft.TransitionType.吸入,
    draft.TransitionType.回忆下滑,
    draft.TransitionType.左下角_II,
]

# 创建视频片段（每个片段在轨道上连续排列，但截取素材的不同部分）
for i in range(len(segment_points) - 1):
    start_time = segment_points[i]
    end_time = segment_points[i + 1]
    duration = end_time - start_time
    
    # 计算轨道上的位置（每个片段紧挨着前一个片段）
    if i == 0:
        track_start = 0  # 第一个片段从0开始
    else:
        # 后续片段紧挨着前一个片段
        track_start = video_segments[i-1].end
    
    # 创建视频片段，在轨道上连续排列，但截取素材的不同部分
    segment = draft.VideoSegment(
        video_material, 
        trange(track_start, duration),  # 轨道上的时间范围
        source_timerange=trange(start_time, duration)  # 素材的截取范围
    )
    
    # 为每个片段添加转场效果
    if i == 0:  # 第一个片段（0-FIRST_TRANSITION_TIME秒），不添加转场（因为没有前一个片段）
        print(f"片段 {i}: 轨道{track_start/1000000:.1f}s-{(track_start+duration)/1000000:.1f}s, 素材{start_time/1000000:.1f}s-{end_time/1000000:.1f}s, 无转场")
    elif i == 1:  # 第二个片段（FIRST_TRANSITION_TIME-(FIRST_TRANSITION_TIME+TRANSITION_INTERVAL)秒），添加开场转场到前一个片段
        opening_transition = random.choice(opening_free_transitions)
        segment.add_transition(opening_transition, duration=tim("0.5s"))  # 开场转场时间稍短
        print(f"片段 {i}: 轨道{track_start/1000000:.1f}s-{(track_start+duration)/1000000:.1f}s, 素材{start_time/1000000:.1f}s-{end_time/1000000:.1f}s, 开场转场: {opening_transition.name}")
    else:  # 后续片段，使用普通转场
        random_transition = random.choice(free_transitions)
        segment.add_transition(random_transition, duration=tim("0.8s"))
        print(f"片段 {i}: 轨道{track_start/1000000:.1f}s-{(track_start+duration)/1000000:.1f}s, 素材{start_time/1000000:.1f}s-{end_time/1000000:.1f}s, 转场: {random_transition.name}")
    
    video_segments.append(segment)

# 创建主标题文本片段，显示"深情诱惑 第1集" - 红色，位于屏幕下方
main_text_segment = draft.TextSegment(
    "深情诱惑 第1集", 
    trange("0s", video_duration),  # 文本片段覆盖整个视频时长
    font=draft.FontType.文轩体,      # 设置字体为文轩体
    style=draft.TextStyle(
        color=(1.0, 0.0, 0.0),      # 字体颜色为红色
        size=24,                    # 字体大小适中
        max_line_width=0.8          # 最大行宽占屏幕 80%
    ),
    clip_settings=draft.ClipSettings(
        transform_y=-0.7             # 位置在屏幕下方
    )
)

# 创建右侧竖排文本片段，显示"点我查看更多免费短剧" - 黄色，竖向排列
side_text_segment = draft.TextSegment(
    "点我查看更多免费短剧", 
    trange("0s", video_duration),  # 文本片段覆盖整个视频时长
    font=draft.FontType.文轩体,      # 设置字体为文轩体
    style=draft.TextStyle(
        color=(1.0, 1.0, 0.0),      # 字体颜色为黄色
        size=18,                    # 字体大小适中
        vertical=True               # 竖向排列
    ),
    clip_settings=draft.ClipSettings(
        transform_x=0.8,            # 位置在屏幕右侧
        transform_y=0.0            # 垂直居中
    )
)

# 将片段添加到轨道中
for segment in video_segments:
    script.add_segment(segment)  # 视频片段添加到视频轨道

script.add_segment(main_text_segment, "主标题轨道")  # 主标题文本添加到指定轨道
script.add_segment(side_text_segment, "侧边文字轨道")  # 侧边文本添加到指定轨道

# 保存草稿
script.save()

print(f"草稿已保存，视频文件: {video_path}")
print(f"视频总时长: {video_duration/1000000:.1f}秒")
print(f"共创建了 {len(video_segments)} 个视频片段")
print("主标题: 深情诱惑 第1集 (红色，屏幕下方)")
print("侧边文字: 点我查看更多免费短剧 (黄色，右侧竖排)")
print("分辨率: 1080x1920 (手机屏幕尺寸)")
print(f"转场效果: 开场{FIRST_TRANSITION_TIME}秒处 + 每{TRANSITION_INTERVAL}秒一个随机转场")
print(f"✅ 所有转场效果均为免费素材，无需VIP！")
print(f"📊 使用了 {len(free_transitions)} 种免费转场效果")
