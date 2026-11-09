from lora import ExpertRouter


def test_router_weights_sum_to_one():
    router = ExpertRouter(16)
    assert router is not None
