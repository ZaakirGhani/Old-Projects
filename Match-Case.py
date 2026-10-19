#Output Grade A
def MC(CASE):
	match CASE:
		case 150 | 160 | 170 | 180 |190 | 200:
			return ("Grade A")
		case 120 | 130 | 140:
			return ("Grade B")
		case 100 | 110:
			return ("Grade C")
		#_ means any value that isn't on the case list or in other words the wild card case
		case _:
			return ("Fail")

Score = 190

print(MC(Score))