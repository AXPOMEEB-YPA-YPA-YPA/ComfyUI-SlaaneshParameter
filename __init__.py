# ==========================================
# 色孽の提示词控制 & 总线系统
# ==========================================

from .iterative_upscale_bus import IterativeUpscaleSettings, IterativeUpscaleUnpacker
from .first_ksampler_bus import FirstKSamplerSettings, FirstKSamplerUnpacker
from .second_ksampler_bus import SecondKSamplerSettings, SecondKSamplerUnpacker
from .partial_redraw_bus import PartialRedrawSettings, PartialRedrawUnpacker
from .manual_mask_redraw_bus import ManualMaskRedrawSettings, ManualMaskRedrawUnpacker

NODE_CLASS_MAPPINGS = {
    # 迭代放大组
    "IterativeUpscaleSettings": IterativeUpscaleSettings,
    "IterativeUpscaleUnpacker": IterativeUpscaleUnpacker,
    
    # 一采预测组
    "FirstKSamplerSettings": FirstKSamplerSettings,
    "FirstKSamplerUnpacker": FirstKSamplerUnpacker,
    
    # 二采润色组
    "SecondKSamplerSettings": SecondKSamplerSettings,
    "SecondKSamplerUnpacker": SecondKSamplerUnpacker,

    # 局部重绘组
    "PartialRedrawSettings": PartialRedrawSettings,
    "PartialRedrawUnpacker": PartialRedrawUnpacker,

    # 手动蒙版重绘组
    "ManualMaskRedrawSettings": ManualMaskRedrawSettings,
    "ManualMaskRedrawUnpacker": ManualMaskRedrawUnpacker,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    # 迭代放大组
    "IterativeUpscaleSettings": "迭代放大-参数设置 (Bus)",
    "IterativeUpscaleUnpacker": "迭代放大-数据展开 (Unpack)",
    
    # 一采预测组
    "FirstKSamplerSettings": "一采预测-参数设置 (Bus)",
    "FirstKSamplerUnpacker": "一采预测-数据展开 (Unpack)",
    
    # 二采润色组
    "SecondKSamplerSettings": "二采润色-参数设置 (Bus)",
    "SecondKSamplerUnpacker": "二采润色-数据展开 (Unpack)",

    # 局部重绘组
    "PartialRedrawSettings": "局部重绘-参数设置 (Bus)",
    "PartialRedrawUnpacker": "局部重绘-数据展开 (Unpack)",

    # 手动蒙版重绘组
    "ManualMaskRedrawSettings": "手动蒙版重绘-参数设置 (Bus)",
    "ManualMaskRedrawUnpacker": "手动蒙版重绘-数据展开 (Unpack)",
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]