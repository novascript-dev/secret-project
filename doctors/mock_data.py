import os
import django

# Configura a variável de ambiente do Django para encontrar o settings.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

# Inicializa o Django
django.setup()

# Agora você pode importar seu modelo
from doctors.models import Doctor

# Seu código para criar ou manipular os dados aqui

from doctors.models import Doctor

doctors = [
    {
        "id": 1,
        "valor_consulta": 340,
        "nome": "Dr. Ricardo Freire Gurgel",
        "especialidade": "Clínico Geral",
        "imagem": "https://saude-kayamind-minio.aqrour.easypanel.host/kayadoc/media/medic_photos/Ricardo_Gurgel.jpeg",
        "visualizacoes": 407,
        "avaliacao": 4.8,
        "crm": "103621",
        "cidade": "São Paulo, SP",
        "descricao": "Médico formado pela UFRJ, com especializações em Oncologia Ocular, Uso Medicinal da Cannabis e Nutrologia Esportiva pela Unifesp.",
        "patologias": "Epilepsia, Alzheimer, Parkinson, Dores crônicas, Ansiedade, Insônia, Obesidade, Perda de Apetite, Câncer, Autismo, TDAH, Endometriose, Medicina do Esporte, Fibromialgia",
        "atendimento": "Crianças, Adolescentes, Adultos e Idosos",
        "convenio": "Não",
        "retorno": "Até 60 dias",
        "experiencia": "Ampla experiência em Saúde Integrativa, combinando abordagens convencionais e complementares para promover o bem-estar integral dos pacientes.",
        "formacao": [
            {"instituicao": "Universidade Federal do Rio de Janeiro (UFRJ)", "curso": "Medicina"},
            {"instituicao": "Universidade Federal de São Paulo (UNIFESP)", "curso": "Uso Medicinal da Cannabis"}
        ],
        "video_url": "https://www.youtube-nocookie.com/embed/U1x1AUxhqEs?si=-FR1g-c6WbchIWY8"
    },
    {
        "id": 2,
        "valor_consulta": 230,
        "nome": "Dra. Mariana Costa",
        "especialidade": "Neurologista",
        "imagem": "https://saude-kayamind-minio.aqrour.easypanel.host/kayadoc/media/medic_photos/amanda.jpg",
        "avaliacao": 4.8,
        "visualizacoes": 512,
        "crm": "209876",
        "cidade": "Rio de Janeiro, RJ",
        "descricao": "Neurologista com experiência em tratamentos alternativos, incluindo o uso medicinal da cannabis.",
        "patologias": "Epilepsia, Alzheimer, Parkinson, Ansiedade",
        "atendimento": "Adultos e Idosos",
        "convenio": "Sim",
        "retorno": "30 dias",
        "experiencia": "Especialista em neurologia e tratamento de doenças neurodegenerativas com cannabis medicinal.",
        "formacao": [
            {"instituicao": "Universidade de São Paulo (USP)", "curso": "Medicina"},
            {"instituicao": "Harvard Medical School", "curso": "Pesquisa em Cannabis Medicinal"}
        ],
        "video_url": "https://www.youtube-nocookie.com/embed/U1x1AUxhqEs?si=-FR1g-c6WbchIWY8"
    },
    {
        "id": 3,
        "nome": "Dr. João Mendes",
        "especialidade": "Psiquiatra",
        "imagem": "https://saude-kayamind-minio.aqrour.easypanel.host/kayadoc/media/medic_photos/Ricardo_Gurgel.jpeg",
        "visualizacoes": 389,
        "avaliacao": 4.8,
        "crm": "305432",
        "cidade": "Belo Horizonte, MG",
        "descricao": "Psiquiatra com foco em transtornos de ansiedade e depressão, utilizando cannabis medicinal.",
        "patologias": "Depressão, Ansiedade, TDAH, Insônia",
        "atendimento": "Adolescentes e Adultos",
        "convenio": "Não",
        "retorno": "45 dias",
        "experiencia": "Experiência com pacientes psiquiátricos e tratamentos alternativos.",
        "formacao": [
            {"instituicao": "Universidade Federal de Minas Gerais (UFMG)", "curso": "Psiquiatria"}
        ],
        "video_url": "https://www.youtube-nocookie.com/embed/U1x1AUxhqEs?si=-FR1g-c6WbchIWY8"
    },
        {
        "id": 4,
        "valor_consulta": 900,
        "nome": "Dr. Ricardo Nunes Andreozzi",
        "especialidade": "Clínico Geral",
        "imagem": "https://saude-kayamind-minio.aqrour.easypanel.host/kayadoc/media/medic_photos/Ricardo_Gurgel.jpeg",
        "visualizacoes": 407,
        "avaliacao": 4.8,
        "crm": "103621",
        "cidade": "São Paulo, SP",
        "descricao": "Médico formado pela UFRJ, com especializações em Oncologia Ocular, Uso Medicinal da Cannabis e Nutrologia Esportiva pela Unifesp.",
        "patologias": "Epilepsia, Alzheimer, Parkinson, Dores crônicas, Ansiedade, Insônia, Obesidade, Perda de Apetite, Câncer, Autismo, TDAH, Endometriose, Medicina do Esporte, Fibromialgia",
        "atendimento": "Crianças, Adolescentes, Adultos e Idosos",
        "convenio": "Não",
        "retorno": "Até 60 dias",
        "experiencia": "Ampla experiência em Saúde Integrativa, combinando abordagens convencionais e complementares para promover o bem-estar integral dos pacientes.",
        "formacao": [
            {"instituicao": "Universidade Federal do Rio de Janeiro (UFRJ)", "curso": "Medicina"},
            {"instituicao": "Universidade Federal de São Paulo (UNIFESP)", "curso": "Uso Medicinal da Cannabis"}
        ],
        "video_url": "https://www.youtube-nocookie.com/embed/U1x1AUxhqEs?si=-FR1g-c6WbchIWY8"
    },
    {
        "id": 5,
        "valor_consulta": 920,
        "nome": "Dra. Marcela Ribeiro",
        "especialidade": "Neurologista",
        "imagem": "https://saude-kayamind-minio.aqrour.easypanel.host/kayadoc/media/medic_photos/amanda.jpg",
        "avaliacao": 4.8,
        "visualizacoes": 512,
        "crm": "209876",
        "cidade": "Rio de Janeiro, RJ",
        "descricao": "Neurologista com experiência em tratamentos alternativos, incluindo o uso medicinal da cannabis.",
        "patologias": "Epilepsia, Alzheimer, Parkinson, Ansiedade",
        "atendimento": "Adultos e Idosos",
        "convenio": "Sim",
        "retorno": "30 dias",
        "experiencia": "Especialista em neurologia e tratamento de doenças neurodegenerativas com cannabis medicinal.",
        "formacao": [
            {"instituicao": "Universidade de São Paulo (USP)", "curso": "Medicina"},
            {"instituicao": "Harvard Medical School", "curso": "Pesquisa em Cannabis Medicinal"}
        ],
        "video_url": "https://www.youtube-nocookie.com/embed/U1x1AUxhqEs?si=-FR1g-c6WbchIWY8"
    },
    {
        "id": 6,
        "valor_consulta": 830,
        "nome": "Dr. João Brandão",
        "especialidade": "Psiquiatra",
        "imagem": "https://saude-kayamind-minio.aqrour.easypanel.host/kayadoc/media/medic_photos/FOTO.jpg",
        "visualizacoes": 389,
        "avaliacao": 4.8,
        "crm": "305432",
        "cidade": "Belo Horizonte, MG",
        "descricao": "Psiquiatra com foco em transtornos de ansiedade e depressão, utilizando cannabis medicinal.",
        "patologias": "Depressão, Ansiedade, TDAH, Insônia",
        "atendimento": "Adolescentes e Adultos",
        "convenio": "Não",
        "retorno": "45 dias",
        "experiencia": "Experiência com pacientes psiquiátricos e tratamentos alternativos.",
        "formacao": [
            {"instituicao": "Universidade Federal de Minas Gerais (UFMG)", "curso": "Psiquiatria"}
        ],
        "video_url": "https://www.youtube-nocookie.com/embed/U1x1AUxhqEs?si=-FR1g-c6WbchIWY8"
    },
    {
        "id": 7,
        "valor_consulta": 530,
        "nome": "Dr. Lyoto Machida",
        "especialidade": "Médico do esporte",
        "imagem": "https://saude-kayamind-minio.aqrour.easypanel.host/kayadoc/media/medic_photos/FOTO.jpg",
        "visualizacoes": 389,
        "avaliacao": 4.8,
        "crm": "305432",
        "cidade": "Belo Horizonte, MG",
        "descricao": "Psiquiatra com foco em transtornos de ansiedade e depressão, utilizando cannabis medicinal.",
        "patologias": "Depressão, Ansiedade, TDAH, Insônia",
        "atendimento": "Adolescentes e Adultos",
        "convenio": "Não",
        "retorno": "45 dias",
        "experiencia": "Experiência com pacientes psiquiátricos e tratamentos alternativos.",
        "formacao": [
            {"instituicao": "Universidade Federal de Minas Gerais (UFMG)", "curso": "Psiquiatria"}
        ],
        "video_url": "https://www.youtube-nocookie.com/embed/U1x1AUxhqEs?si=-FR1g-c6WbchIWY8"
    },
    {
        "id": 8,
        "valor_consulta": 330,
        "nome": "Dr. Anderson Silva",
        "especialidade": "Médico do Esporte",
        "imagem": "https://saude-kayamind-minio.aqrour.easypanel.host/kayadoc/media/medic_photos/FOTO.jpg",
        "visualizacoes": 389,
        "avaliacao": 4.8,
        "crm": "305432",
        "cidade": "Belo Horizonte, MG",
        "descricao": "Psiquiatra com foco em transtornos de ansiedade e depressão, utilizando cannabis medicinal.",
        "patologias": "Depressão, Ansiedade, TDAH, Insônia",
        "atendimento": "Adolescentes e Adultos",
        "convenio": "Não",
        "retorno": "45 dias",
        "experiencia": "Experiência com pacientes psiquiátricos e tratamentos alternativos.",
        "formacao": [
            {"instituicao": "Universidade Federal de Minas Gerais (UFMG)", "curso": "Psiquiatria"}
        ],
        "video_url": "https://www.youtube-nocookie.com/embed/U1x1AUxhqEs?si=-FR1g-c6WbchIWY8"
    }
]

specialties = [
    "Psiquiatra",
    "Clínico Geral",
    "Neurologista",
    "Médico do Esporte",
]


def bulk_populate():
    doctors_instances = [Doctor(
        id=doctor_data['id'],
        name=doctor_data['name'],
        specialty=doctor_data['specialty'],
        image=doctor_data['image'],
        views=doctor_data['views'],
        rating=doctor_data['rating'],
        crm=doctor_data['crm'],
        city=doctor_data['city'],
        description=doctor_data['description'],
        conditions=doctor_data['conditions'],
        patient_groups=doctor_data['patient_groups'],
        insurance=doctor_data['insurance'],
        follow_up=doctor_data['follow_up'],
        experience=doctor_data['experience'],
        education=doctor_data['education'],
        video_url=doctor_data['video_url'],
        consultation_fee=doctor_data['consultation_fee'],
    ) for doctor_data in doctors]

    Doctor.objects.bulk_create(doctors_instances)


if __name__ == '__main__':
    bulk_populate()