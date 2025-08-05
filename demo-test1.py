# 导入模块
import os
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

# 创建视频片段
video_material = draft.VideoMaterial(video_path)
video_segment = draft.VideoSegment(video_material, trange("0s", video_material.duration))

# 为视频片段添加转场效果
video_segment.add_transition(draft.TransitionType.叠化, duration=tim("0.5s"))

# 创建主标题文本片段，显示"深情诱惑 第1集" - 红色，位于屏幕下方
main_text_segment = draft.TextSegment(
    "深情诱惑 第1集", 
    video_segment.target_timerange,  # 文本片段的首尾与视频片段一致
    font=draft.FontType.文轩体,      # 设置字体为文轩体
    style=draft.TextStyle(
        color=(1.0, 0.0, 0.0),      # 字体颜色为红色
        size=30,                    # 字体大小适中
        max_line_width=0.8          # 最大行宽占屏幕 80%
    ),
    clip_settings=draft.ClipSettings(
        transform_y=-0.7             # 位置在屏幕下方
    )
)

# 创建右侧竖排文本片段，显示"点我查看更多免费短剧" - 黄色，竖向排列
side_text_segment = draft.TextSegment(
    "点我查看更多免费短剧", 
    video_segment.target_timerange,  # 文本片段的首尾与视频片段一致
    font=draft.FontType.文轩体,      # 设置字体为文轩体
    style=draft.TextStyle(
        color=(1.0, 1.0, 0.0),      # 字体颜色为黄色
        size=20,                    # 字体大小适中
        vertical=True               # 竖向排列
    ),
    clip_settings=draft.ClipSettings(
        transform_x=0.8,            # 位置在屏幕右侧
        transform_y=0.0            # 垂直居中
    )
)

# 将片段添加到轨道中
script.add_segment(video_segment)  # 视频片段添加到视频轨道
script.add_segment(main_text_segment, "主标题轨道")  # 主标题文本添加到指定轨道
script.add_segment(side_text_segment, "侧边文字轨道")  # 侧边文本添加到指定轨道

# 保存草稿
script.save()

print(f"草稿已保存，视频文件: {video_path}")
print("主标题: 深情诱惑 第1集 (红色，屏幕下方)")
print("侧边文字: 点我查看更多免费短剧 (黄色，右侧竖排)")
print("分辨率: 1080x1920 (手机屏幕尺寸)")
