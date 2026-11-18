"""第 53 批：室内外过渡时墙角漏光、动态物体发黑、探头更新时间..."""

def surface_offset(normal, bias):
    """沿探针表面法线返回采样偏移。"""
    raise NotImplementedError("TODO: surface_offset")

def update_priority(distance, moved):
    """返回探针更新优先级。"""
    raise NotImplementedError("TODO: update_priority")

def normal_bias(thickness, base):
    """按遮挡厚度返回自适应法线偏移。"""
    raise NotImplementedError("TODO: normal_bias")

def ray_step(scene_scale, probes):
    """按场景尺度返回遮挡射线步长。"""
    raise NotImplementedError("TODO: ray_step")

def temporal_blend(previous, current, dt, rate):
    """按时间累积新旧辐射度。"""
    raise NotImplementedError("TODO: temporal_blend")

def in_bounds(probe, minimum, maximum):
    """判断探针是否在有效边界内。"""
    raise NotImplementedError("TODO: in_bounds")

def interpolate_weights(weights):
    """归一化探针插值权重。"""
    raise NotImplementedError("TODO: interpolate_weights")

def clear_history(scene_changed):
    """判断场景切换是否清空探针历史。"""
    raise NotImplementedError("TODO: clear_history")
