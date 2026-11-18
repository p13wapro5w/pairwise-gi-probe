import pytest
from render import gi_probe as mod

CASES = [
    ("offset_x", "m.surface_offset((1.0, 0.0), 0.1) == approx((0.1, 0.0))"),
    ("offset_y_zero", "m.surface_offset((0.0, 1.0), 0.1)[0] == approx(0.0)"),
    ("priority_near", "m.update_priority(1.0, 0) > m.update_priority(10.0, 0)"),
    ("priority_moved", "m.update_priority(10.0, 1) > m.update_priority(10.0, 0)"),
    ("normal_bias_grow", "m.normal_bias(0.5, 0.1) > 0.1"),
    ("ray_step_half", "m.ray_step(10.0, 20) == approx(0.5)"),
    ("temporal_full", "m.temporal_blend(0.0, 1.0, 1.0, 1.0) == approx(1.0)"),
    ("temporal_partial", "m.temporal_blend(0.0, 1.0, 0.5, 1.0) == approx(0.5)"),
    ("bounds_true", "m.in_bounds((0.5, 0.5), (0.0, 0.0), (1.0, 1.0)) is True"),
    ("bounds_false", "m.in_bounds((2.0, 0.5), (0.0, 0.0), (1.0, 1.0)) is False"),
    ("weights_sum", "sum(m.interpolate_weights([1.0, 3.0])) == approx(1.0)"),
    ("weights_zero", "m.interpolate_weights([0.0, 0.0]) == [0.5, 0.5]"),
    ("clear_true", "m.clear_history(True) is True"),
    ("clear_false", "m.clear_history(False) is False"),
    ("normal_bias_same", "m.normal_bias(0.0, 0.1) == approx(0.1)")
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx})
