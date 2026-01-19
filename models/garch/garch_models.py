from arch import arch_model


def build_garch_model(name: str, params: dict):
    """Instantiate a single GARCH‑family model based on params."""
    # This is a stub; you can extend for EGARCH/FIGARCH using `vol` argument.
    def model_factory(returns):
        am = arch_model(
            returns,
            mean=params.get("mean", "constant"),
            vol=params.get("type", "GARCH"),
            p=params.get("p", 1),
            o=params.get("o", 0),
            q=params.get("q", 1),
            dist=params.get("dist", "normal"),
        )
        return am

    return model_factory
