"""Reproduce the ledger's nested conversions with exact decimal arithmetic."""

from __future__ import annotations

from decimal import Decimal, ROUND_HALF_UP, getcontext


getcontext().prec = 40
D = Decimal

# Unified Internet "prices" (ability points per SI unit), recovered from the
# three free quick entries and the four locked inner sums.
RATE = {
    "travel_per_km": D("195"),
    "investment_per_kg": D("964"),
    "water_per_kg": D("925"),
    "butter_per_kg": D("139"),
    "milk_per_litre": D("156"),
}

# Regional interpretations of the abstract units needed by the four records.
MAINLAND_LI_KM = D("0.5")
US_MILE_KM = D("1.609344")
MAINLAND_JIN_KG = D("0.5")
MAINLAND_LIANG_KG = D("0.05")
HK_CATTY_KG = D("0.60478982")
HK_TAEL_KG = HK_CATTY_KG / D("16")
AVOIRDUPOIS_POUND_KG = D("0.45359237")
US_FLUID_OUNCE_L = D("0.0295735295625")


def q2(value: Decimal) -> Decimal:
    return value.quantize(D("0.01"), rounding=ROUND_HALF_UP)


def decimal_places(value: Decimal) -> int:
    """Count significant places after the point, ignoring trailing zeroes."""

    return max(0, -value.normalize().as_tuple().exponent)


def fractional_digits(value: Decimal) -> str:
    """Return every digit after the point in the exact Decimal value."""

    _, _, fraction = format(value, "f").partition(".")
    return fraction


def nonzero_fraction_digits(value: Decimal) -> int:
    """Count the 'black' (non-zero) digits after the decimal point."""

    return sum(digit != "0" for digit in fractional_digits(value))


def main() -> None:
    inner = {
        "上海": (
            D("0.007") * MAINLAND_JIN_KG * RATE["investment_per_kg"]
            + D("1.968") * MAINLAND_LI_KM * RATE["travel_per_km"]
        ),
        "香港": (
            D("0.577") * MAINLAND_JIN_KG * RATE["butter_per_kg"]
            + D("1.862") * MAINLAND_JIN_KG * RATE["water_per_kg"]
        ),
        "伦敦": (
            D("0.064") * RATE["water_per_kg"]
            + D("102.158") * RATE["butter_per_kg"]
        ),
        "纽约": (
            D("36.673") * MAINLAND_LIANG_KG * RATE["butter_per_kg"]
            + D("75.796") * US_MILE_KM * RATE["travel_per_km"]
        ),
    }
    observed = {
        "上海": D("195.254"),
        "香港": D("901.2765"),
        "伦敦": D("14259.162"),
        "纽约": D("24041.336628107183"),
    }

    implied_chicago_mile_km = (
        observed["纽约"]
        - D("36.673") * MAINLAND_LIANG_KG * RATE["butter_per_kg"]
    ) / (D("75.796") * RATE["travel_per_km"])

    final = {
        # Use the authoritative locked amount returned by listEntries.  The
        # reconstructed New York inner sum differs by 9.0e-4 because the
        # backend retained more precision than the displayed/free factors.
        "上海": observed["上海"] * MAINLAND_LI_KM * RATE["travel_per_km"],
        "香港": observed["香港"] * HK_TAEL_KG * RATE["investment_per_kg"],
        "伦敦": observed["伦敦"] * AVOIRDUPOIS_POUND_KG * RATE["investment_per_kg"],
        "纽约": observed["纽约"] * US_FLUID_OUNCE_L * RATE["milk_per_litre"],
    }

    print(
        "region\tinner_rebuilt\tinner_observed\tdifference"
        "\tfinal_exact\tfinal_rounded_2dp\tdecimal_places"
        "\tnonzero_fraction_digits\textracted_letter"
    )
    for region in ("上海", "香港", "伦敦", "纽约"):
        print(
            region,
            inner[region],
            observed[region],
            inner[region] - observed[region],
            final[region],
            q2(final[region]),
            decimal_places(final[region]),
            nonzero_fraction_digits(final[region]),
            chr(64 + nonzero_fraction_digits(final[region])),
            sep="\t",
        )
    print(f"implied_chicago_mile_km\t{implied_chicago_mile_km}")
    print(f"one_over_0.621371\t{D(1) / D('0.621371')}")
    # Read the four locked regions in their selector order.  Treat zero as
    # white and every other fractional digit as black, then use A1Z26 as
    # demonstrated by the banner's 16.1.9.4 = PAID.
    region_order = ("上海", "香港", "伦敦", "纽约")
    extracted = "".join(
        chr(64 + nonzero_fraction_digits(final[region])) for region in region_order
    )
    rebuilt_new_york = inner["纽约"] * US_FLUID_OUNCE_L * RATE["milk_per_litre"]
    print(f"new_york_rebuilt_final\t{rebuilt_new_york}")
    print(f"new_york_rebuilt_nonzero_fraction_digits\t{nonzero_fraction_digits(rebuilt_new_york)}")
    print(f"extracted_answer\t{extracted}")


if __name__ == "__main__":
    main()
