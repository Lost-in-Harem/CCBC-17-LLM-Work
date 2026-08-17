"""Reproduce the four locked ledger calculations and A1Z26 extraction."""

from __future__ import annotations

from decimal import Decimal, ROUND_FLOOR, getcontext


getcontext().prec = 50
D = Decimal

RATE = {
    "travel_per_km": D("195"),
    "investment_per_kg": D("964"),
    "water_per_kg": D("925"),
    "solid_food_per_kg": D("139"),
    "milk_per_litre": D("156"),
}

# Units needed to rebuild the visible inner formula amounts.
MAINLAND_LI_KM = D("0.5")
MAINLAND_JIN_KG = D("0.5")
MAINLAND_LIANG_KG = D("0.05")
US_STATUTE_MILE_KM = D("1.609344")

# Units used by the four OUTER records. The symbol changes meaning with the
# city's local convention and, for investment, the precious-metal context.
NAUTICAL_MILE_KM = D("1.852")
HK_TROY_TAEL_KG = D("0.037429")
TROY_POUND_KG = D("0.3732417216")
US_FLUID_OUNCE_L = D("0.0295735295625")

LOCKED_AMOUNT = {
    "上海": D("195.254"),
    "香港": D("901.2765"),
    "伦敦": D("14259.162"),
    "纽约": D("24041.336628107183"),
}

# The service-introduction sentence supplies this order. Each tuple is the
# zero-padded A1Z26 segmentation encoded by that row's integer part.
EXTRACTION = {
    "伦敦": ("5", "13", "05", "18"),
    "上海": ("7", "05", "14"),
    "香港": ("3", "25", "19"),
    "纽约": ("11", "09", "14"),
}


def decode_tokens(tokens: tuple[str, ...]) -> str:
    values = [int(token) for token in tokens]
    assert all(1 <= value <= 26 for value in values)
    return "".join(chr(ord("A") + value - 1) for value in values)


def main() -> None:
    # The first three visible nested sums reproduce exactly. The New York
    # backend amount carries extra precision, so its locked value is used.
    inner_rebuilt = {
        "上海": (
            D("0.007") * MAINLAND_JIN_KG * RATE["investment_per_kg"]
            + D("1.968") * MAINLAND_LI_KM * RATE["travel_per_km"]
        ),
        "香港": (
            D("0.577") * MAINLAND_JIN_KG * RATE["solid_food_per_kg"]
            + D("1.862") * MAINLAND_JIN_KG * RATE["water_per_kg"]
        ),
        "伦敦": (
            D("0.064") * RATE["water_per_kg"]
            + D("102.158") * RATE["solid_food_per_kg"]
        ),
        "纽约": (
            D("36.673") * MAINLAND_LIANG_KG * RATE["solid_food_per_kg"]
            + D("75.796") * US_STATUTE_MILE_KM * RATE["travel_per_km"]
        ),
    }

    final = {
        "伦敦": LOCKED_AMOUNT["伦敦"] * TROY_POUND_KG * RATE["investment_per_kg"],
        "上海": LOCKED_AMOUNT["上海"] * NAUTICAL_MILE_KM * RATE["travel_per_km"],
        "香港": LOCKED_AMOUNT["香港"] * HK_TROY_TAEL_KG * RATE["investment_per_kg"],
        "纽约": LOCKED_AMOUNT["纽约"] * US_FLUID_OUNCE_L * RATE["milk_per_litre"],
    }

    print("region\tinner_rebuilt\tinner_locked\tfinal_exact\tinteger_part\tgrouping\ttext")
    chunks: list[str] = []
    for region, tokens in EXTRACTION.items():
        integer_part = int(final[region].to_integral_value(rounding=ROUND_FLOOR))
        assert "".join(tokens).lstrip("0") == str(integer_part)
        extracted = decode_tokens(tokens)
        chunks.append(extracted)
        print(
            region,
            inner_rebuilt[region],
            LOCKED_AMOUNT[region],
            final[region],
            integer_part,
            "-".join(tokens),
            extracted,
            sep="\t",
        )

    answer = "".join(chunks)
    assert answer == "EMERGENCYSKIN"
    print(f"answer\t{answer}")


if __name__ == "__main__":
    main()
