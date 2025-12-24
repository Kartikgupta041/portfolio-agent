from src.config import DATA_DIR
from src.portfolio import load_portfolio


def main():
    portfolio_path = DATA_DIR / "portfolio.json"
    portfolio = load_portfolio(str(portfolio_path))

    print("\nLoaded portfolio:")
    for p in portfolio.positions:
        print(f" - {p.ticker}: {p.weight:.3f}")

    print(f"\nRisk tolerance: {portfolio.constraints.risk_tolerance}")
    print(f"Max position weight: {portfolio.constraints.max_position_weight}\n")


if __name__ == "__main__":
    main()

