from django.shortcuts import render
import math
from .forms import NumbersForm

def stats_home(request):
    form = NumbersForm()
    context = {'form': form}

    if request.method == "POST":
        form = NumbersForm(request.POST)
        if form.is_valid():
            try:
                user_input = form.cleaned_data['numbers']
                numbers = [float(x.strip()) for x in user_input.split(",") if x.strip()]
                numbers.sort()
                n = len(numbers)

                if n < 2:
                    context['error'] = "Please enter at least two numbers."
                    context['form'] = form
                    return render(request, "statsweb/home.html", context)

                min_val = min(numbers)
                max_val = max(numbers)
                range_val = max_val - min_val
                num_classes = round(1 + 3.322 * math.log10(n))
                class_width = math.ceil(range_val / num_classes)

                intervals, frequencies, tallies, midpoints, fx = [], [], [], [], []

                start = min_val
                for i in range(num_classes):
                    end = start + class_width
                    count = 0
                    tally_str = ""
                    for num in numbers:
                        if (start <= num < end) or (i == num_classes - 1 and num == end):
                            count += 1
                            tally_str += "|" if count % 5 != 0 else "|||| "

                    midpoint = (start + end) / 2
                    fxi = midpoint * count

                    intervals.append((start, end))
                    frequencies.append(count)
                    tallies.append(tally_str.strip())
                    midpoints.append(midpoint)
                    fx.append(round(fxi, 2))
                    start = end

                total_fx = sum(fx)
                mean = total_fx / n

                x_minus_xbar = []
                x_minus_xbar_sq = []
                fx_minus_xbar_sq = []

                for i in range(num_classes):
                    diff = midpoints[i] - mean
                    squared = diff ** 2
                    fx_squared = frequencies[i] * squared

                    x_minus_xbar.append(round(diff, 2))
                    x_minus_xbar_sq.append(round(squared, 2))
                    fx_minus_xbar_sq.append(round(fx_squared, 2))

                cf = []
                total = 0
                for f in frequencies:
                    total += f
                    cf.append(total)

                variance = sum(fx_minus_xbar_sq) / n
                std_dev = variance ** 0.5

                if n % 2 == 0:
                    median = (numbers[n//2 - 1] + numbers[n//2]) / 2
                else:
                    median = numbers[n//2]

                mode_count = 0
                mode = []
                for num in numbers:
                    if numbers.count(num) > mode_count:
                        mode_count = numbers.count(num)

                for num in numbers:
                    if numbers.count(num) == mode_count and num not in mode:
                        mode.append(num)

                table = []
                for i in range(num_classes):
                    table.append({
                        "interval": f"{intervals[i][0]:.2f} - {intervals[i][1]:.2f}",
                        "tally": tallies[i],
                        "f": frequencies[i],
                        "cf": cf[i],
                        "x": f"{midpoints[i]:.2f}",
                        "fx": fx[i],
                        "x_minus_xbar": x_minus_xbar[i],
                        "x_minus_xbar_sq": x_minus_xbar_sq[i],
                        "fx_minus_xbar_sq": fx_minus_xbar_sq[i],
                    })
                
                # Calculate totals
                total_f = sum(frequencies)
                total_fx_val = sum(fx)
                total_x_minus_xbar = sum(x_minus_xbar)
                total_x_minus_xbar_sq = sum(x_minus_xbar_sq)
                total_fx_minus_xbar_sq = sum(fx_minus_xbar_sq)


                context.update({
                    "form": form,
                    "intervals": [  # ← Add this so your old `{% for row in intervals %}` works
                        [
                            table[i]["interval"],
                            table[i]["tally"],
                            table[i]["f"],
                            table[i]["cf"],
                            table[i]["x"],
                            table[i]["fx"],
                            table[i]["x_minus_xbar"],
                            table[i]["x_minus_xbar_sq"],
                            table[i]["fx_minus_xbar_sq"],
                        ] for i in range(len(table))
                    ],
                    "total_f": total_f,
                    "total_fx": round(total_fx_val, 2),
                    "total_x_minus_xbar": round(total_x_minus_xbar, 2),
                    "total_x_minus_xbar_sq": round(total_x_minus_xbar_sq, 2),
                    "total_fx_minus_xbar_sq": round(total_fx_minus_xbar_sq, 2),
                    "mean": round(mean, 2),
                    "median": round(median, 2),
                    "mode": mode,
                    "variance": round(variance, 2),
                    "std_dev": round(std_dev, 2),
                })
            except Exception as e:
                context["error"] = str(e)

    return render(request, 'statsweb/home.html', context)
