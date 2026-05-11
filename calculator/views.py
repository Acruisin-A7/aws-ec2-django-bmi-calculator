from django.shortcuts import render

# Create your views here.

def bmi_calculator(request):
    result = None
    category = None
    height = None
    weight = None
    error = None
    if request.method == 'POST':
        try:
            height = float(request.POST.get('height', 0))
            weight = float(request.POST.get('weight', 0))

            if height <= 0 or weight <= 0:
                error = 'Height and weight must be positive numbers.'
            elif height > 300 or weight > 500:
                error = 'Please enter realistic values.'
            else:
                # BMI formula: weight(kg) / height(m)^2
                height_m = height / 100
                result = round(weight / (height_m ** 2), 1)

                if result < 18.5:
                    category = 'Underweight'
                elif result < 25:
                    category = 'Normal weight'
                elif result < 30:
                    category = 'Overweight'
                else:
                    category = 'Obese'
        except (ValueError, TypeError):
            error = 'Please enter valid numeric values.'

    return render(request, 'calculator/index.html', {
        'result': result,
        'category': category,
        'height': height,
        'weight': weight,
        'error': error,
    })
	
