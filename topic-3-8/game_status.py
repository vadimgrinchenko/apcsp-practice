"""Game Status: refactor render_status without changing its behavior."""

def clamp(value, min, max):
    if value < min:
        value = min
    elif value > max:
        value = max
    return value

def make_bar(value, max):
    filled = value * 10 // max
    bar = "["
    for position in range(10):
        if position < filled:
            bar = bar + "#"
        else:
            bar = bar + "-"
    bar = bar + "]"
    return bar

def add_all(scores):
    total = 0
    for score in scores:
        total = total + score
    return total

def find_highest(scores):
    highest = scores[0]
    for score in scores:
        if score > highest:
            highest = score
    return highest

def count_at_least(scores, threshold):
    strong_count = 0
    for score in scores:
        if score >= threshold:
            strong_count = strong_count + 1
    return strong_count

def time(seconds):
    minutes = seconds // 60
    remainder = seconds % 60
    text = str(minutes) + ":"
    if remainder < 10:
        text = text + "0"
    text = text + str(remainder)
    return text

def level_finder(total):
    if total < 250:
        if total < 100:
            level = "Rookie"
        else:
            level = "Skilled"
    else:
        level = "Expert"

    return level

def render_status(name, health, energy, elapsed_seconds, best_seconds, scores):

    shown_health = clamp(health, 0, 100)
    shown_energy = clamp(energy, 0, 60)

    health_bar = make_bar(shown_health, 100)
    energy_bar = make_bar(shown_energy, 60)

    elapsed_text = time(elapsed_seconds)
    best_text = time(best_seconds)

    total = add_all(scores)
    highest = find_highest(scores)
    strong_count = count_at_least(scores, 80)

    level = level_finder(total)

    report = "PLAYER: " + name
    report = report + "\nHealth  " + health_bar + " " + str(shown_health) + "/100"
    report = report + "\nEnergy  " + energy_bar + " " + str(shown_energy) + "/60"
    report = report + "\nLevel:  " + level
    report = report + "\nTime:   " + elapsed_text
    report = report + "\nBest:   " + best_text
    report = report + "\nRecent: total=" + str(total)
    report = report + ", best=" + str(highest) + ", 80+=" + str(strong_count)
    return report

if __name__ == "__main__":
    print(render_status("Nova", 75, 18, 125, 119, [40, 50, 90]))
    print(render_status("Orion", 110, -4, 61, 60, [80, 80, 90]))