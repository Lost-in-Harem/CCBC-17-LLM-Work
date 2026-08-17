"""Reproduce the four locked ledger calculations and direct ECVX extraction."""

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

MAINLAND_LI_KM = D("0.5")
MAINLAND_JIN_KG = D("0.5")
MAINLAND_LIANG_KG = D("0.05")
US_MILE_KM = D("1.609344")

# Hong Kong's ordinary customary tael is one sixteenth of its statutory catty.
# The locked record contains no gold item marker, so the gold-market troy tael
# is not used. London likewise uses the ordinary avoirdupois pound.
HK_CATTY_KG = D("0.60478982")
HK_TAEL_KG = HK_CATTY_KG / D("16")
AVOIRDUPOIS_POUND_KG = D("0.45359237")
US_FLUID_OUNCE_L = D("0.0295735295625")

LOCKED_AMOUNT = {
    "上海": D("195.254"),
    "香港": D("901.2765"),
    "伦敦": D("14259.162"),
    "纽约": D("24041.336628107183"),
}


def a1z26(value: int) -> str:
    """Wrap a positive integer into the one-based A1Z26 cycle."""

    return chr(ord("A") + (value - 1) % 26)


def main() -> None:
    # These checks reconstruct three displayed nested sums. The New York
    # locked quantity has additional backend precision and is used verbatim.
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
            + D("75.796") * US_MILE_KM * RATE["travel_per_km"]
        ),
    }

    final = {
        "上海": LOCKED_AMOUNT["上海"] * MAINLAND_LI_KM * RATE["travel_per_km"],
        "香港": LOCKED_AMOUNT["香港"] * HK_TAEL_KG * RATE["investment_per_kg"],
        "伦敦": (
            LOCKED_AMOUNT["伦敦"]
            * AVOIRDUPOIS_POUND_KG
            * RATE["investment_per_kg"]
        ),
        "纽约": (
            LOCKED_AMOUNT["纽约"] * US_FLUID_OUNCE_L * RATE["milk_per_litre"]
        ),
    }

    print(
        "region\tinner_rebuilt\tinner_locked\tfinal_exact\tinteger_part"
        "\traw_a1z26"
    )
    raw: list[str] = []
    for region in ("上海", "香港", "伦敦", "纽约"):
        integer_part = int(final[region].to_integral_value(rounding=ROUND_FLOOR))
        letter = a1z26(integer_part)
        raw.append(letter)
        print(
            region,
            inner_rebuilt[region],
            LOCKED_AMOUNT[region],
            final[region],
            integer_part,
            letter,
            sep="\t",
        )

    answer = "".join(raw)
    assert answer == "ECVX"
    print(f"answer\t{answer}")


if __name__ == "__main__":
    main()
