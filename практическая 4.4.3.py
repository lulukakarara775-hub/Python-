answer = input("Как твои дела? ").lower()
if answer in ["хорошо", "нормально", "отлично"]:
    print("")
elif answer in ["плохо", "не хорошо"] or "…" in answer:
    print("")
else:
    print("")