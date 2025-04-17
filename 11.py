def calculate_ufp(ilf, eif, ei, eo, eq):
    return ((ilf*10) + (eif*7) + (ei*4) + (eo*5) + (eq*4))
def calculate_afp(ufp, gsc_scores):
    total_gsc_score = sum(gsc_scores)
    vaf = 0.65 + (0.01 * total_gsc_score)
    return ufp * vaf
print("Enter the number of: ")
ilf = int(input("Internal Logical Files (ILF): "))
eif = int(input("External Interface Files (EIF): "))
ei = int(input("External Inputs (EI): "))
eo = int(input("External Outputs (EO): "))
eq = int(input("External Inquiries (EQ): "))
ufp = calculate_ufp(ilf, eif, ei, eo, eq)
print(f"\nUnadjusted Function Points (UFP): {ufp}")
print("\nAssess the degree of influence of each GSC (0-5):")
gsc_scores = []
gsc_names = [
    "Data Communication",
    "Distributed Data Processing",
    "Performance",
    "High Reliability",
    "Security",
    "User Interface",
    "Online Data Entry",
    "Online Data Update",
    "Complex Processing",
    "Transaction Rate",
    "Online Data Processing",
    "Multiple Systems",
    "Ease of Use",
    "Maintainability"
]
for i, name in enumerate(gsc_names):
    try:
        score = int(input(f"{i + 1}. {name}: "))
        if 0 <= score <= 5:
            gsc_scores.append(score)
        else:

            print("Invalid input. Please enter a value between 0 and 5.")
            gsc_scores.append(0)
    except ValueError:
        print("Invalid input. Please enter an integer.")
        gsc_scores.append(0)
afp = calculate_afp(ufp, gsc_scores)
print(f"\nAdjusted Fu.nction Points (AFP): {afp}")