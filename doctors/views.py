from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Doctor

def listar_medicos(request):
    filter_by_specialty = request.GET.get("especialidade")
    ordering = request.GET.get("ordenacao", "").strip()
    search_by_name = request.GET.get("q", "").strip().lower()

    # Filtrando os médicos com base nos parâmetros recebidos
    filtered_doctors = Doctor.objects.all()

    if filter_by_specialty and filter_by_specialty != "Todas":
        filtered_doctors = filtered_doctors.filter(specialty=filter_by_specialty)

    if search_by_name:
        filtered_doctors = filtered_doctors.filter(name__icontains=search_by_name)

    # Ordenando os médicos conforme a ordenação pedida
    if ordering == "menor_valor":
        filtered_doctors = filtered_doctors.order_by('consultation_fee')
    elif ordering == "maior_valor":
        filtered_doctors = filtered_doctors.order_by('-consultation_fee')
    elif ordering == "visualizacoes":
        filtered_doctors = filtered_doctors.order_by('-views')

    # Pegando as especialidades únicas para o filtro
    specialties = Doctor.objects.values_list('specialty', flat=True).distinct()

    return render(request, "doctors/list.html", {
        "doctors": filtered_doctors,
        "specialty": filter_by_specialty,
        "specialties": ["Todas"] + list(specialties),
        "search": search_by_name,
        "ordering": ordering,
    })

def detalhes_medico(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    return render(request, "doctors/detail.html", {"doctor": doctor})
